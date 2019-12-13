from django.shortcuts import render, redirect, reverse
#from artifacts.models import Artifact
from bids.models import BidEvent, BidLineItem

# Views for managing the bidding
def view_bids(request, id):
    """
    View to get data for bids on a specific artifact. 
    Look up a bid event associated with the artifact id.
    Further look up of associated bids with the bid event id.
    """
    
    print("")
    print("## Inside view all bids function ##")
    print("Artifact_ID: " + str(id))
    
    bid_event = BidEvent.objects.filter(artifact=id)
    for bid_detail in bid_event:
        artifact_name = bid_detail.artifact.name
        reserve_price = bid_detail.artifact.reserve_price
        highest_bid = bid_detail.highest_bid
        bid_event_id = bid_detail.id
    
    print("Bid Event: " + str(bid_event))
    print("")
    
    bids = BidLineItem.objects.filter(bid_event=bid_event_id)
    
    print("")
    print("## Bid Lines ##")
    print(bids)
    
    return render(request, "bids.html", {
        "artifact_id": id,
        "artifact_name": artifact_name,
        "reserve_price": reserve_price,
        "bid_event_id": bid_event_id,
        "highest_bid": highest_bid,
        "bids": bids,
        }
    )

def add_bid(request, id):
    """
    Add a bid on a particular artifact
    """
    
    bids = BidLineItem.objects.filter(artifact_id=id)
    
    return redirect("view_bids", id=id)