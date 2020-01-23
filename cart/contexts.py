from django.shortcuts import get_object_or_404
from artifacts.models import Artifact
from bids.models import BidLineItem

def cart_contents(request):
    """
    Cart contents for items ready to be purchased
    """
    total = 0
    artifact_count = 0
    
    # Primary cart for outright purchase of items
    cart = request.session.get("cart", {})
    cart_items = []
    for id, quantity in cart.items():
        artifact = get_object_or_404(Artifact, pk=id)
        total += quantity * artifact.purchase_price
        artifact_count += quantity
        cart_items.append({
            "id": id,
            "quantity": quantity,
            "artifact": artifact,
        })
    
    # Secondary cart for managing successful bids
    bid_cart = request.session.get("bid_cart", {})
    bid_cart_items = []
    for id, bid_id in bid_cart.items():
        bid = get_object_or_404(BidLineItem, pk=bid_id)    
        total += bid.bid_quantity * bid.bid_amount
        artifact_count += bid.bid_quantity
        bid_cart_items.append({
            "id": id,
            "bid_id": bid_id,
            "quantity": bid.bid_quantity,
            "artifact": bid.bid_event.artifact,
            "bid_amount" : bid.bid_amount,
        })
        
    return {
        "cart_items": cart_items,
        "bid_cart_items": bid_cart_items,
        "total": total,
        "artifact_count": artifact_count
    }