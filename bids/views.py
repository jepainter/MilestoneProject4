from django.shortcuts import render, redirect, reverse
#from artifacts.models import Artifact
from bids.models import Bid, BidLineItem

# Views for managing the bidding
def view_bids(request, id):
    """
    View to get data for bids on artifacts
    """
    
    print("")
    print("## Inside view all bids function ##")
    print("ID: " + str(id))
    
    artifact_id=id
    
    artifact = Bid.objects.filter(artifact_id=id)
    for artifact_info in artifact:
        artifact_name = artifact_info.artifact.name
        reserve_price = artifact_info.artifact.reserve_price
        highest_bid = artifact_info.highest_bid
        bid_id = artifact_info.id
    
    print("Artifact: " + str(artifact))
    print("")
    
    
    bids = BidLineItem.objects.filter(bid_id=bid_id)
    
    print("")
    print("## Bid Event ##")
    print(bids)
    
    for bid in bids:
        artifact_n = bid.bid_id.artifact.name
        highest_b = bid.bid_id.highest_bid
    
    print("")
    print("Bid.Bid_Id: " + str(artifact_n))
    print("Bid.Bid_current: " + str(highest_b))
    
    return render(request, "bids.html", {
        "artifact_id": artifact_id,
        "reserve_price": reserve_price,
        "artifact_name": artifact_name,
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