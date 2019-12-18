from django.shortcuts import render, redirect, reverse

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
    
    return redirect(reverse("index"))

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
    cart.pop(id)
    
    request.session["cart"] = cart
    
    return redirect(reverse("view_cart"))