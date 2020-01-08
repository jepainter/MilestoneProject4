from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#from decimal import Decimal
from django.utils import timezone
from artifacts.models import Artifact
from bids.models import BidEvent, BidLineItem
    
# Views for managing the bidding
def view_bids(request, id):
    """
    Get data for bids on a specific artifact. Look up a bid event
    associated with the artifact id. Further look up of associated
    bids with the bid event id.
    """
    
    try:
        bid_event = BidEvent.objects.get(artifact=id)
        artifact = bid_event.artifact
        bids = BidLineItem.objects.filter(bid_event=bid_event)
    except:
        bid_event = ""
        bids = ""
        artifact = Artifact.objects.get(id=id)
    
    return render(request, "bids.html", {
        "artifact": artifact,
        "bid_event": bid_event,
        "bids": bids,
        "datetime": timezone.now(),
        })


@login_required
def add_bid(request, id):
    """
    Add a bid on a particular artifact. Look up relevent bid event 
    to add bid to. Check for if user already have a bid and update
    if so, else create new
    
    FIX FORM VALIDATION ERROR FOR 0.01 Amount submission
    """
    
    bid_time = timezone.now()
    
    if request.method == "POST":
        bid_event = BidEvent.objects.get(artifact_id=id)
        bid_quantity = int(request.POST.get("bid_quantity"))
        bid_amount = float(request.POST.get("bid_amount"))
        
        try:
            bid_line_item = BidLineItem.objects.filter(
                bid_user=request.user.id).get(bid_event__artifact=id)
        except:
            if bid_time < bid_event.bid_event_deadline:
                new_bid_line_item = BidLineItem(
                    bid_event = bid_event,
                    bid_amount = bid_amount,
                    bid_quantity = bid_quantity,
                    bid_user = User.objects.get(id=request.user.id),
                    bid_date_time = bid_time,
                    )
                new_bid_line_item.save()
            else:
                print("Bid after deadline, bid not accepted")

    else:
       print("Else statement for non POST method")
    
    set_highest_bid(bid_event.id)
    
    return redirect("view_bids", id=id)


@login_required
def adjust_bid(request, id):
    """
    Adjust a bid placed from a specific event.
    Zero value inputs will remove the bid from bid event.
    Checks whether bid below reserve price or below previous bid, 
    prevents change to bid.
    
    CHECK type for amount and quantitites for comparisons
    """
    
    bid_time = timezone.now()
    
    if request.method =="POST":
        new_quantity = int(request.POST.get("adjust_quantity"))
        new_amount = float(request.POST.get("adjust_amount"))
        
        try:
            bid_line_item = BidLineItem.objects.get(id=id)
            bid_amount = bid_line_item.bid_amount
            bid_quantity = bid_line_item.bid_quantity
        
            if new_quantity == 0 or new_amount == 0:
                bid_line_item.delete()
            
            elif new_amount < bid_amount:
                if new_quantity > bid_quantity:
                    print("Bid quantity changed and bid amount reduced or equal")
                else: 
                    print("Bid quantity and amount reduced or equal")
            
            elif new_amount == bid_amount:
                if new_quantity > bid_quantity:
                    print("Bid quantity changed")
                else:
                    print("Bid quantity same as previous or reduced")
            
            else:
                if bid_time < bid_line_item.bid_event.bid_event_deadline:
                    print("Bid before deadline")
                    bid_line_item.bid_amount = new_amount
                    bid_line_item.bid_quantity = new_quantity
                    bid_line_item.bid_user = User.objects.get(id=request.user.id)
                    bid_line_item.bid_date_time = bid_time
                    bid_line_item.save()
                else:
                    print("Bid after deadline, no adjustment made")
    
            set_highest_bid(bid_line_item.bid_event.id)
        
        except:
            print("Error with adjusting bid")
    
    return redirect("view_user_bids")


@login_required
def remove_bid(request, id):
    """
    Remove a bid placed by the user
    """
    
    bid_time = timezone.now()
    
    try:
        bid_line_item = BidLineItem.objects.get(id=id)

        if bid_time < bid_line_item.bid_event.bid_event_deadline:
            bid_line_item.delete()
        else:
            print("Bid removed after deadline, not deleted")
        
        set_highest_bid(bid_line_item.bid_event.id)
        
        return redirect("view_bids", id=bid_line_item.bid_event.artifact_id)
        
    except:
        print("Error with removing bid")
    
    return redirect("view_user_bids")


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
def archive_bid(request, id):
    """
    Function to archive bids from MyBids, to prevent display.
    Info kept in Database for record purposes
    """
    
    try:
        bid = BidLineItem.objects.get(id=id)
        bid.bid_archived = True
        bid.save()
    
    except:
        print("Error")
    
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
        print("No bid set with highest flag yet")
    
    new_highest_bid = BidLineItem.objects.filter(
        bid_event=id).order_by('-bid_amount').first()
    new_highest_bid.bid_highest = True
    new_highest_bid.save()
    
    return True