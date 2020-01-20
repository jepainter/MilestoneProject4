from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from artifacts.models import Artifact
from bids.models import BidLineItem

# Views to render the cart contents and adjust
def view_cart(request):
    """
    Contents of cart is rendered to html
    """
    
    return render(request, "cart.html")


def add_to_cart(request, id):
    """
    Add quantity to the specific product in the cart
    """
    
    quantity = int(request.POST.get("quantity"))
    cart = request.session.get("cart", {})
    cart[id] = cart.get(id, quantity)
    request.session["cart"] = cart
    
    return redirect(reverse("view_cart"))

    
def adjust_cart(request, id):
    """
    Adjust existing contents of the cart
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
    Remove an item from the cart without need to adjust quantity
    """
    
    cart = request.session.get("cart", {})
    cart.pop(id)
    request.session["cart"] = cart
    
    return redirect(reverse("view_cart"))


def add_bid_to_cart(request, id):
    """
    Process successful bid to add to secondary cart
    """
    
    bid_line_item = BidLineItem.objects.get(pk=id)
    if bid_line_item.bid_event.artifact.quantity != 0:
        bid_cart = request.session.get("bid_cart", {})
        bid_cart[bid_line_item.bid_event.artifact.id] = bid_cart.get(
            bid_line_item.bid_event.artifact.id, id)
        request.session["bid_cart"] = bid_cart
    else:
        messages.error(
            request,
            "Sorry, the artifact has been purchased by someone else."
            )
    
    return redirect(reverse("view_cart"))

    
def remove_bid_from_cart(request, id):
    """
    Remove an bid from the secondary cart for later payment
    """
    
    bid_cart = request.session.get("bid_cart", {})
    bid_cart.pop(id)
    request.session["bid_cart"] = bid_cart
    
    return redirect(reverse("view_cart"))