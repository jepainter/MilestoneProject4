from django.shortcuts import render, redirect, reverse, get_object_or_404
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
    print("Bid Event: " + str(bid_event))
    if bid_event:
        print("Bid Event Exists")
        for bid_detail in bid_event:
            artifact_name = bid_detail.artifact.name
            reserve_price = bid_detail.artifact.reserve_price
            highest_bid = bid_detail.highest_bid
            bid_event_id = bid_detail.id
    
    else:
        print("Bid event does not exist")
        artifact_name = "Test DS9"
        reserve_price = "404404"
        highest_bid = "404404404"
        bid_event_id = 2
        
    
    
#    print("")
    
    bids = BidLineItem.objects.filter(bid_event=bid_event_id)
    
#    print("")
#    print("## Bid Lines ##")
#    print(bids)
    
    bid_form = BidDetailsForm()
    
    return render(request, "bids.html", {
        "artifact_id": id,
        "artifact_name": artifact_name,
        "reserve_price": reserve_price,
        "bid_event_id": bid_event_id,
        "highest_bid": highest_bid,
        "bids": bids,
        "bid_form": bid_form,
        }
    )

def add_bid(request, id):
    """
    Add a bid on a particular artifact.
    Look up relevent bid event to add bid to.
    
    
    FIX FORM VALIDATION ERROR FOR 0.01 Amount submission
    """
    
    if request.method == "POST":
        
        print("")
        print("## Inside add bid function ##")
        print("Id: " + str(id))
        
        bid_form = BidDetailsForm(request.POST)
        if bid_form.is_valid():
            print("")
            print("Bid form valid")
            
            bid_event = BidEvent.objects.get(artifact_id=id)
            print("Bid Event: " + str(bid_event))
            
            bid_line_item = BidLineItem(
                bid_event = bid_event,
                bid_amount = bid_form.cleaned_data["bid_amount"],
                bid_quantity = bid_form.cleaned_data["bid_quantity"],
                )
            
            print("Bid Line Item: " + str(bid_line_item))
            bid_line_item.save()
    
        else:
            print("")
            print("Bid form INVALID")
        
        print("")
        print("Bid Form: " + str(bid_form))    
#        bid_amount = bid_form.cleaned_data["bid_amount"]
#        bid_quantity = request.POST.get("bid_quantity")
        
        print("Bid Amount: " + str(bid_form.cleaned_data["bid_amount"]))
        print("Bid Quantity: " + str(bid_form.cleaned_data["bid_quantity"]))
        
        print("## Exiting add bid function ##")
        print("")
    
    else:
       # bid_form = BidDetailsForm()
       print("Else statement for non POST method")
    
    return redirect("view_bids", id=id)

def adjust_bid(request, id):
    """
    Adjust a bid placed from a specific event.
    Zero value inputs will remove the bid from bid event.
    """
    
    print("")
    print("## Inside the adjust a bid function ##")
    print("Bid Line ID: " + str(id))
    
    new_quantity = int(request.POST.get("quantity"))
    new_amount = float(request.POST.get("amount"))
    
    print("New Quantity: " + str(new_quantity))
    print("New Amount: " + str (new_amount))
    
    bid_line_item = BidLineItem.objects.get(id=id)
    
    print("")
    print("Bid Line Detail: " + str(bid_line_item))
    print()
    
    if new_quantity == 0 or new_amount == 0:
        print("")
        print("Deleting bid line item")
        bid_line_item.delete()
        print("Bid Line Detail: " + str(bid_line_item))
        
    else:
        print("")
        print("Inserting new quantit or amount")
        
        bid_line_item.bid_amount = new_amount
        bid_line_item.bid_quantity = new_quantity
        bid_line_item.save()
        print("Revised bid: " + str(bid_line_item))
        print
    
    
    
    print("## Exiting the adjust bid function ##")
    
    return redirect("view_bids", id=id)
    