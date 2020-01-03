from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from artifacts.models import Artifact
from bids.models import BidLineItem
from payment.forms import PaymentDetailsForm, OrderDetailsForm
from payment.models import OrderLineItem
import stripe

# Views to render relevant html
stripe.api_key = settings.STRIPE_SECRET

@login_required
def payment(request):
    if request.method == "POST":
        order_form = OrderDetailsForm(request.POST)
        payment_form = PaymentDetailsForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            
            cart = request.session.get("cart", {})
            total = 0
            for id, quantity in cart.items():
                artifact = get_object_or_404(Artifact, pk=id)
                total += quantity * artifact.purchase_price
                order_line_item = OrderLineItem(
                    order = order,
                    artifact = artifact,
                    quantity = quantity,
                    bid = "",
                    unit_price = artifact.purchase_price,
                    )
                order_line_item.save()
            
            
            bid_cart = request.session.get("bid_cart", {})
            for id, bid_id in bid_cart.items():
                bid = BidLineItem.objects.get(pk=bid_id)    
                total += bid.bid_quantity * bid.bid_amount
                order_line_item = OrderLineItem(
                    order = order,
                    artifact = bid.bid_event.artifact,
                    quantity = bid.bid_quantity,
                    bid = bid_id,
                    unit_price = bid.bid_amount,
                    )
                order_line_item.save()
            
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "EUR",
                    description = request.user.email,
                    card = payment_form.cleaned_data["stripe_id"],
                    )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined.")
            
            if customer.paid:
                messages.error(request, "You have successfully paid.")
                cart = request.session.get("cart", {})
                print("")
                print("### Inside in payment function, processing reduction in stock")
                for id, quantity in cart.items():
                    artifact = get_object_or_404(Artifact, pk=id)
                    print("Artifact Quantity:" + str(artifact.quantity))
                    artifact.quantity -= quantity
                    print("New Artifact Quantity: " + str(artifact.quantity))
                    artifact.save()
                
                bid_cart = request.session.get("bid_cart", {})
                for id, bid_id in bid_cart.items():
                    bid = get_object_or_404(BidLineItem, pk=bid_id)
                    print("Artifact Bid Quantity:" + str(bid.bid_event.artifact.quantity))
                    bid.bid_event.artifact.quantity -= bid.bid_quantity
                    print("New Artifact Bid Quantity: " + str(bid.bid_event.artifact.quantity))
                    bid.bid_event.artifact.save()
                    bid.bid_paid = True
                    bid.save()
                
                request.session["cart"] = {}
                request.session["bid_cart"] = {}
                return redirect(reverse('artifacts'))
            else:
                messages.error(request, "We were unable to process payment1.")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to process payment2.")
    else:
        payment_form = PaymentDetailsForm()
        order_form = OrderDetailsForm()
    
    return render(request, "payment.html", {
        "order_form": order_form,
        "payment_form": payment_form,
        "publishable": settings.STRIPE_PUBLISHABLE
        })