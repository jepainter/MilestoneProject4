from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from decimal import Decimal
from artifacts.models import Artifact
from bids.models import BidEvent, BidLineItem
    
# Views for managing the bidding
@login_required
def view_user_bids(request):
    """
    Function to view bids of logged in user
    """
    user_bids = BidLineItem.objects.filter(bid_user=request.user.id)
    if user_bids:
        bidder = user_bids[0].bid_user
    else:
        bidder = User.objects.get(id=request.user.id)
    
    return render(request, "mybids.html", {
        "user": bidder,
        "bids": user_bids,
        "datetime": timezone.now()
        })


@login_required
def add_bid(request, id):
    """
    Add a bid on a particular artifact. Look up relevent bid event 
    to add bid to. Check for if user already have a bid and update
    if so, else create new
    """
    bid_time = timezone.now()
    if request.method == "POST":
        try:
            bid_event = BidEvent.objects.get(artifact_id=id)
            bid_quantity = int(request.POST.get("bid_quantity"))
            bid_amount = Decimal(request.POST.get("bid_amount"))
            if bid_time < bid_event.bid_event_deadline:
                if bid_amount < bid_event.artifact.reserve_price:
                    messages.error(
                        request,
                        "Sorry, your bid is below the reserve price."
                        )
                else:
                    new_bid_line_item = BidLineItem(
                        bid_event = bid_event,
                        bid_amount = bid_amount,
                        bid_quantity = bid_quantity,
                        bid_user = User.objects.get(id=request.user.id),
                        bid_date_time = bid_time,
                        )
                    new_bid_line_item.save()
                    messages.success(
                        request,
                        "Your bid has been accepted."
                        )
            else:
                messages.error(
                    request,
                    "Sorry, your bid was submitted after the deadline."
                    )
            # Call helper function to determine highest bid        
            set_highest_bid(bid_event.id)
        except:
            messages.error(
                request,
                "Sorry, no bid event exists for this artifact."
                )

    return redirect("view_artifact", id=id)


@login_required
def adjust_bid(request, id):
    """
    Adjust a bid placed from a specific event.
    Zero value inputs will remove the bid from bid event.
    Checks whether bid below reserve price or below previous bid, 
    prevents change to bid.
    """
    bid_time = timezone.now()
    if request.method =="POST":
        try:
            bid_line_item = BidLineItem.objects.get(id=id)
            new_quantity = int(request.POST.get("adjust_quantity"))
            new_amount = Decimal(request.POST.get("adjust_amount"))
            if bid_time < bid_line_item.bid_event.bid_event_deadline:
                if new_quantity == 0 or new_amount == 0:
                    bid_line_item.delete()
                    messages.success(
                        request,
                        "Your bid have been removed."
                        )
                elif new_amount < bid_line_item.bid_event.artifact.reserve_price:
                    messages.error(
                        request,
                        "Sorry, your bid is below the reserve price."
                        )
                else:
                    bid_line_item.bid_amount = new_amount
                    bid_line_item.bid_quantity = new_quantity
                    bid_line_item.bid_date_time = bid_time
                    bid_line_item.save()
                    messages.success(
                        request,
                        "Your bid has been adjusted."
                        )
            else:
                messages.error(
                    request,
                    "Sorry, your bid was submitted after the deadline."
                    )
            # Call to helper function to set the highest bid
            set_highest_bid(bid_line_item.bid_event.id)
        except:
            messages.error(
                request,
                "Sorry, your bid could not be found for this artifact."
                )
    
    return redirect("view_user_bids")


@login_required
def remove_bid(request, id):
    """
    Remove a bid placed by the user, by checking if within the deadline,
    else prevent removal.
    """
    bid_time = timezone.now()
    try:
        bid_line_item = BidLineItem.objects.get(id=id)
        if bid_time < bid_line_item.bid_event.bid_event_deadline:
            bid_line_item.delete()
            messages.success(
                request,
                "Your bid have been removed."
                )
        else:
            messages.error(
                request,
                "Sorry, you cannot remove a bid after the bidding is closed."
                )
        # Call to helper function to set the highest bid
        set_highest_bid(bid_line_item.bid_event.id)
        
        return redirect("view_user_bids")
        
    except:
        messages.error(
            request,
            "Sorry, your bid could not be found for this artifact."
            )
    
    return redirect("view_user_bids")


@login_required
def archive_bid(request, id):
    """
    Function to archive bids from MyBids, to prevent display.
    Info kept in Database for record purposes
    """
    try:
        bid = BidLineItem.objects.get(id=id)
        bid.bid_archived = True
        bid.save()
        messages.success(
            request,
            "Your old bid have been archived."
            )
    except:
        messages.error(
            request,
            "Sorry, your bid could not be archived."
            )
    
    return redirect(reverse("view_user_bids"))
    
    
def set_highest_bid(id):
    """
    Function to reset highest bid in an event
    if a new bid or adjusted bid is higher or 
    if existing highest bid is deleted
    """
    try:
        existing_highest_bid = BidLineItem.objects.filter(
            bid_event=id).get(bid_highest=True)
        existing_highest_bid.bid_highest = False 
        existing_highest_bid.save()
    except:
        pass
    new_highest_bid = BidLineItem.objects.filter(
        bid_event=id).order_by('-bid_amount').first()
    if new_highest_bid != None:
        if new_highest_bid.bid_event.artifact.quantity == 0:
            pass
        else:
            new_highest_bid.bid_highest = True
            new_highest_bid.save()
    
    return True


def prohibit_further_bidding(request, id):
    """
    Function to prevent further bidding if items are purchased outright
    and quantity is not available.  This will mark all active bids as not
    being the highest bid.
    """
    try:
        existing_highest_bid = BidLineItem.objects.filter(
            bid_event__artifact=id).get(bid_highest=True)
        existing_highest_bid.bid_highest = False 
        existing_highest_bid.bid_event.bid_event_deadline = timezone.now()
        existing_highest_bid.bid_event.save()
        existing_highest_bid.save()
    except:
        try:
            bid_event = BidEvent.objects.get(artifact=id)
            bid_event.bid_event_deadline = timezone.now()
            bid_event.save()
        except:
            pass
    
    return True


def adjust_bidding_quantity(request, id):
    """
    Function to adjust bidding quantities for users, if stock levels
    are less than bid quantity.
    """
    bids = BidLineItem.objects.filter(bid_event__artifact=id)
    for bid in bids:
        if bid.bid_quantity > bid.bid_event.artifact.quantity:
            bid.bid_note = "Bid quantity adjusted down due to stock availability."
            bid.bid_quantity = bid.bid_event.artifact.quantity
            bid.save()
            
    return True