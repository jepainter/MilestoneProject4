from django.shortcuts import render, redirect, reverse, get_object_or_404
#from artifacts.models import Artifact
from bids.models import BidEvent, BidLineItem
from bids.forms import BidDetailsForm
    
# Views for managing the bidding
def view_bids(request, id):
    """
    View to get data for bids on a specific artifact. 
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
    Add a bid on a particular artifact
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