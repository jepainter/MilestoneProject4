from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from django.db.models import Max
#from artifacts.models import Artifact
from bids.models import BidEvent, BidLineItem
from bids.forms import BidDetailsForm
    
# Views for managing the bidding
def view_bids(request, id):
    """
    Get data for bids on a specific artifact. 
    Look up a bid event associated with the artifact id.
    Further look up of associated bids with the bid event id.
    """
    
#    print("")
#    print("## Inside view all bids function ##")
#    print("Artifact_ID: " + str(id))
    
    bid_event = BidEvent.objects.filter(artifact=id)
#    print("Bid Event: " + str(bid_event))
    if bid_event:
#        print("Bid Event Exists")
        for bid_detail in bid_event:
            artifact_name = bid_detail.artifact.name
            artifact_quantity = bid_detail.artifact.quantity
            reserve_price = bid_detail.artifact.reserve_price
            highest_bid = bid_detail.highest_bid
            bid_event_id = bid_detail.id
            bid_event_status = bid_detail.bid_event_status
    
    else:
#        print("Bid event does not exist")
        artifact_name = "Test DS9"
        reserve_price = "404404"
        highest_bid = "404404404"
        bid_event_id = 0
        bid_event_status = "Bidding Not Available"
        
    
    
#    print("")
    
    bids = BidLineItem.objects.filter(bid_event=bid_event_id)
#    print("")
#    print("## Bid Lines ##")
#    print(bids)
    
#    bid_form = BidDetailsForm()
    
    return render(request, "bids.html", {
        "artifact_id": id,
        "artifact_name": artifact_name,
        "artifact_quantity": artifact_quantity,
        "reserve_price": reserve_price,
        "bid_event_id": bid_event_id,
        "bid_event_status": bid_event_status,
        "highest_bid": highest_bid,
        "bids": bids,
#        "bid_form": bid_form,
        }
    )

@login_required
def add_bid(request, id):
    """
    Add a bid on a particular artifact.
    Look up relevent bid event to add bid to.
    Check for if user already have a bid and update if so, else create new
    
    
    FIX FORM VALIDATION ERROR FOR 0.01 Amount submission
    """
    
    if request.method == "POST":
        
#        print("")
#        print("## Inside add bid function ##")
#        print("Id: " + str(id))
        
    #    bid_form = BidDetailsForm(request.POST)
        
    #    print("New bid form detail")
    #    print(bid_form)
    #    if bid_form.is_valid():
        print("")
        print("Bid form valid")
        
        bid_event = BidEvent.objects.get(artifact_id=id)
#            print("Bid Event: " + str(bid_event))
        
        bid_quantity = int(request.POST.get("bid_quantity"))
        bid_amount = float(request.POST.get("bid_amount"))
        print("Bid amount: " + str(bid_amount))
        print("Bid quantity: " + str(bid_quantity))
        
        bid_line_item_exists = BidLineItem.objects.filter(bid_user=request.user.id).filter(bid_event__artifact=id)
        print("Bid line exists? ")
        if bid_line_item_exists:
            print("Yes")
            print(bid_line_item_exists)
            
        else:
            print("No")
            print(bid_line_item_exists)
            
            #highest_bid_status = determine_highest_bid(bid_event.id, bid_amount)
            
            #if highest_bid_status == True:
             #   bid_line_item = BidLineItem(
              #      bid_event = bid_event,
               #     bid_amount = bid_amount,
                #    bid_quantity = bid_quantity,
                 #   bid_user = User.objects.get(id=request.user.id),
                  #  bid_highest = True,
                  #  )
            #else:
            bid_line_item = BidLineItem(
                bid_event = bid_event,
                bid_amount = bid_amount,
                bid_quantity = bid_quantity,
                bid_user = User.objects.get(id=request.user.id),
                )
            
            print("Bid Line Item: " + str(bid_line_item))
            bid_line_item.save()
    
#        else:
#            print("")
#            print("Bid form INVALID")
#            print(bid_form.errors)
#            for error in bid_form.errors:
#                print(error)
#            messages.error(request, "There is a problem with your bid")
            #bid_form.errors(request, "Errors")
        
#        print("")
#        print("Bid Form: " + str(bid_form))    
#        bid_amount = bid_form.cleaned_data["bid_amount"]
#        bid_quantity = request.POST.get("bid_quantity")
        
#        print("Bid Amount: " + str(bid_form.cleaned_data["bid_amount"]))
#        print("Bid Quantity: " + str(bid_form.cleaned_data["bid_quantity"]))
        
#        print("## Exiting add bid function ##")
#        print("")

    else:
       #bid_form = BidDetailsForm()
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
    
    print("")
    print("## Inside the adjust a bid function ##")
    print("Bid Line ID: " + str(id))

    if request.method =="POST":
        
        try:
            new_quantity = int(request.POST.get("adjust_quantity"))
            new_amount = float(request.POST.get("adjust_amount"))
            Decimal
            print("New Quantity: ")
            print(type(new_quantity))
            print("New Amount: ")
            print(type(new_amount))
        
        except:
            print("Error with data capture")
        
        bid_line_item = BidLineItem.objects.get(id=id)
        bid_amount = bid_line_item.bid_amount
        bid_quantity = bid_line_item.bid_quantity
        
        print("Bid Quantity: ")
        print(type(bid_quantity))
        print("Bid Amount: ")
        print(type(bid_amount))
        
        
    #    print("")
    #    print("Bid Line Detail: " + str(bid_line_item))
    #    print()
        
        if new_quantity == 0 or new_amount == 0:
    #        print("")
    #        print("Deleting bid line item")
    #        artifact_id = bid_line_item.bid_event.artifact_id
    #        print("Artifact Id: " + str(artifact_id))
            bid_line_item.delete()
    #        print("Bid Line Detail: " + str(bid_line_item))
            
    #    elif new_amount < bid_line_item.bid_event.artifact.reserve_price:
    #        print("Bid below reserve prices")
    #        print("Reserve price: " + str(bid_line_item.bid_event.artifact.reserve_price))
        
        elif new_amount < bid_amount:
            if new_quantity > bid_quantity:
                print("Bid quantity changed and bid amount reduced or equal")
                print("Previous bid: " + str(bid_line_item.bid_amount))
                print("New bid: " + str(new_amount))
                print("Previous quantity: " + str(bid_line_item.bid_quantity))
                print("New quantity: " + str(new_quantity))
            else: 
                print("Bid quantity and amount reduced or equal")
                print("Previous bid: " + str(bid_line_item.bid_amount))
                print("New bid: " + str(new_amount))
                print("Previous quantity: " + str(bid_line_item.bid_quantity))
                print("New quantity: " + str(new_quantity))
        
        elif new_amount == bid_amount:
            if new_quantity > bid_quantity:
                print("Bid quantity changed")
                print("Previous quantity: " + str(bid_line_item.bid_quantity))
                print("New quantity: " + str(new_quantity))
            else:
                print("Bid quantity same as previous or reduced")
                print("Previous quantity: " + str(bid_line_item.bid_quantity))
                print("New quantity: " + str(new_quantity))
        
        else:
    #        print("")
    #        print("Inserting new quantity or amount")
            
           #previous_highest_bid = BidLineItem.objects.filter(bid_event=bid_line_item.bid_event).filter(bid_highest=True)
            
            #if not previous_highest_bid:
            #    print("No previous highest bid")
            #    bid_line_item.bid_highest = True
            
            #else:
            #    print("Previous highest bid found")
            #    print("Previous highest bid: " + str(previous_highest_bid))
            #    for bid_info in previous_highest_bid:
            #        if bid_info.bid_amount <= new_amount:
            #            bid_info.bid_highest = False
            #            bid_info.save()
            #            bid_line_item.bid_highest = True
            #            print("Changed current bid to highest")
                    
            #        else:
            #            bid_line_item.bid_highest = False
            #            print("Did not change current bid to highest")
            
#            highest_bid_status = determine_highest_bid(bid_line_item.bid_event.id ,new_amount)
            
#            if highest_bid_status == True:
#                print("Changing current bid to highest")
#                bid_line_item.bid_highest = True
#            else:
#                print("Not changing current bid to highest")
#                bid_line_item.bid_highest = False
                
            
            bid_line_item.bid_amount = new_amount
            bid_line_item.bid_quantity = new_quantity
            bid_line_item.bid_user = User.objects.get(id=request.user.id)
            bid_line_item.save()
    #        print("Revised bid: " + str(bid_line_item))
    #        artifact_id = bid_line_item.bid_event.artifact_id
    #        print("Artifact Id: " + str(artifact_id))
        
        print("Bid Event: " + str(bid_line_item.bid_event.id))
        print("Bid New Amount: " + str(new_amount))
        
        print("## Exiting the adjust bid function ##")
    
    set_highest_bid(bid_line_item.bid_event.id)
    
    
    return redirect("view_user_bids")

@login_required
def remove_bid(request, id):
    """
    Remove a bid placed by the user
    """
    
   # if request.method == "POST":
    
    bid_line_item = BidLineItem.objects.get(id=id)
    print("")
    print("## Inside delete bid function ##")
    print("Bid Line Item: " + str(bid_line_item))
    print("Bid highest: " + str(bid_line_item.bid_highest))
    print("Bid Event: " + str(bid_line_item.bid_event.id))
    
    
    #if bid_line_item.bid_highest == True:
     #   highest_bid = BidLineItem.objects.filter(bid_event=bid_line_item.bid_event).order_by('-bid_amount').first()
      #  print("Highest bid: " + str(highest_bid))
       # highest_bid.bid_highest = True
        #highest_bid.save()
    
    bid_line_item.delete()
    print("")
    print("After delete")
    print("Bid Line Item: " + str(bid_line_item))
    
    set_highest_bid(bid_line_item.bid_event.id)
    
    return redirect("view_bids", id=bid_line_item.bid_event.artifact_id)

@login_required
def view_user_bids(request):
    """
    Function to view bids of logged in user
    """
    
    bidder = User.objects.get(id=request.user.id)
    
    
    user_bids = BidLineItem.objects.filter(bid_user=bidder)
    
    print("")
    print("## Inside view my bids function ##")
    print("User: " + str(bidder))
    print("Username: " + str(bidder.username))
    print("User ID: " + str(bidder.id))
    print("")
    print("Bids: " + str(user_bids))
    
    
    return render(request, "mybids.html", {"user": bidder, "bids": user_bids})
    

def set_highest_bid(id):
    """
    Function to reset highest bid in an event
    if a new bid or adjusted bid is higher or 
    if existing highest bid is deleted
    """
    
    print("")
    print("## Inside determine highest bid function ##")
    
    try:
        existing_highest_bid = BidLineItem.objects.filter(bid_event=id).get(bid_highest=True)
        print("Setting existing highest bid to false")
        print(existing_highest_bid)
        existing_highest_bid.bid_highest = False 
        existing_highest_bid.save()
    
    except:
        print("No bid set with highest flag yet")
    
    print("Looking up new highest bid and setting to true")
    new_highest_bid = BidLineItem.objects.filter(bid_event=id).order_by('-bid_amount').first()
    new_highest_bid.bid_highest = True
    print(new_highest_bid)
    new_highest_bid.save()
    
    return True