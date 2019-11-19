from django.shortcuts import get_object_or_404
from artifacts.models import Artifact

def cart_contents(request):
    """
    Cart contents for items ready to be purchased
    """
    
    cart = request.session.get("cart", {})
    cart_items = []
    total = 0
    artifact_count = 0
    
    for id, quantity in cart.items():
        artifact = get_object_or_404(Artifact, pk=id)
        total += quantity * artifact.purchase_price
        artifact_count += quantity
        cart_items.append({
            "id": id,
            "quantity": quantity,
            "artifact": artifact
        })
        
        return {"cart_items": cart_items, "total": total, "artifact_count": artifact_count}