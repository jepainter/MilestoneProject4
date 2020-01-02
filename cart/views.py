from django.shortcuts import render, redirect, reverse
from artifacts.models import Artifact
from bids.models import BidLineItem

# Views to render the cart contents and adjust
def view_cart(request):
    """
    Contents of cart is rendered to html
    """
#   cart = {}
#    request.session["cart"] = cart
#    bid_cart = {}
#    request.session["bid_cart"] = bid_cart
    
    return render(request, "cart.html")

def add_to_cart(request, id):
    """
    Add quantity to the specific product in the cart
    """
    
    print("")
    print("## Inside add purchase to cart function ##")
    print("Artifact Id: " + str(id))
    
    #cart_second = {}
    
    #request.session["cart_second"] = cart_second
    
    quantity = int(request.POST.get("quantity"))
    #artifact = Artifact.objects.get(pk=id)
    #price = float(artifact.purchase_price)
    
    #print("artifact: " + str(artifact))
    #print("price: " + str(price))
    
    cart = request.session.get("cart", {})
    
    cart[id] = cart.get(id, quantity)
#    cart[id] = {
        #"price": float(artifact.purchase_price),
 #       "quantity": int(request.POST.get("quantity")),
        #"bid": ""
 #   }
    print("Cart Contents: " + str(cart))
    
    request.session["cart"] = cart
    
    print("## Exiting add purchase to cart function ##")
    print("")
    
    return redirect(reverse("view_cart"))
    
def adjust_cart(request, id):
    """
    Adjust contents of the cart
    """
    quantity = int(request.POST.get("quantity"))
    cart = request.session.get("cart", {})
    
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session["cart"] = cart
    
    return redirect(reverse("view_cart"))
    
def remove_item_from_cart(request, id):
    """
    Remove an item from the cart without adjusting quantity
    """
    
    cart = request.session.get("cart", {})
    #bid_cart = request.session.get("bid_cart", {})
    #bid_cart.pop(id)
    cart.pop(id)
    
    request.session["cart"] = cart
    #request.session["bid_cart"] = bid_cart
    
    return redirect(reverse("view_cart"))

def add_bid_to_cart(request, id):
    """
    Process successful bid to add to cart
    """
    print("")
    print("## Inside add bid to cart function ##")
    print("Bid Line Id: " + str(id))
    
    bid_line_item = BidLineItem.objects.get(pk=id)
    print("Bid Line Item: "+ str(bid_line_item))
    
  #  artifact = bid_line_item.bid_event.artifact.id    
  #  print("Artifact: "+ str(artifact))
    
    bid_cart = request.session.get("bid_cart", {})
    
   # bid_cart[bid_line_item.bid_event.artifact.id] = {
#        "bid": bid_line_item.id
#    }
    
    bid_cart[bid_line_item.bid_event.artifact.id] = bid_cart.get(bid_line_item.bid_event.artifact.id, id)
    print("Bid_Cart Contents: " + str(bid_cart))
    
    request.session["bid_cart"] = bid_cart
    
    print("## Exiting add bid to cart function ##")
    print("")
    
    return redirect(reverse("view_cart"))
    
def remove_bid_from_cart(request, id):
    """
    Remove an bid from the cart for later payment
    """
    
    bid_cart = request.session.get("bid_cart", {})
    bid_cart.pop(id)
    
    request.session["bid_cart"] = bid_cart
    
    return redirect(reverse("view_cart"))