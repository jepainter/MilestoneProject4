from django.shortcuts import get_object_or_404
from artifacts.models import Artifact
from bids.models import BidLineItem

def cart_contents(request):
    """
    Cart contents for items ready to be purchased
    """
    
    cart = request.session.get("cart", {})
    bid_cart = request.session.get("bid_cart", {})
    cart_items = []
    bid_cart_items = []
    total = 0
    artifact_count = 0
    
    for id, quantity in cart.items():
  #      print(id)
  #      print(cart[id])
  #      print(cart[id]['price'])
  #      print(cart[id]['quantity'])
  #      print(cart[id]['bid'])
        artifact = get_object_or_404(Artifact, pk=id)
        total += quantity * artifact.purchase_price
        artifact_count += quantity
        cart_items.append({
            "id": id,
            "quantity": quantity,
            "artifact": artifact,
#            "price": cart[id]['price'], 
        })
            
    print("Cart Items: " + str(cart_items))
    
#    cart_second = request.session.get("cart_second", {})
#    cart_items_two = []
  #  print("Cart second: " + str(cart_second))
    
    for id, bid_id in bid_cart.items():
  #      print(id)
  #      print(cart_second[id])
  #      print(cart_second[id]['price'])
  #      print(cart_second[id]['quantity'])
        bid = BidLineItem.objects.get(pk=bid_id)    
        #artifact = get_object_or_404(Artifact, pk=id)
        total += bid.bid_quantity * bid.bid_amount
        artifact_count += bid.bid_quantity
        bid_cart_items.append({
            "id": id,
            "bid_id": bid_id,
            "quantity": bid.bid_quantity,
            "artifact": bid.bid_event.artifact,
            "bid_amount" : bid.bid_amount,
        })
    
    print("Bid Cart Items: " + str(bid_cart_items))
    
        
    return {
        "cart_items": cart_items,
        "bid_cart_items": bid_cart_items,
        "total": total,
        "artifact_count": artifact_count
    }