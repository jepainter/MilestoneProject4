from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from artifacts.models import Artifact
from bids.models import BidLineItem, BidEvent
from bids.views import adjust_bidding_quantity, prohibit_further_bidding
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
        owner_id = request.user.id
        
        # Capture order form details
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            
            # Add cart items as line items in order
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
                    owner_id = owner_id,
                    )
                order_line_item.save()
            
            # Add bid cart items as line items in order
            bid_cart = request.session.get("bid_cart", {})
            for id, bid_id in bid_cart.items():
                bid = get_object_or_404(BidLineItem, pk=bid_id)    
                total += bid.bid_quantity * bid.bid_amount
                order_line_item = OrderLineItem(
                    order = order,
                    artifact = bid.bid_event.artifact,
                    quantity = bid.bid_quantity,
                    bid = bid_id,
                    unit_price = bid.bid_amount,
                    owner_id = owner_id,
                    )
                order_line_item.save()
            
            # Execute the charge to a card
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "EUR",
                    description = request.user.email,
                    card = payment_form.cleaned_data["stripe_id"],
                    )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined.")
            
            # Successful payment processes and adjusts quantity of artifacts
            if customer.paid:
                messages.success(request, "You have successfully paid.")
                
                # Adjust or prohibit further purchases/bidding if no items
                cart = request.session.get("cart", {})
                for id, quantity in cart.items():
                    artifact = get_object_or_404(Artifact, pk=id)
                    artifact.quantity -= quantity
                    artifact.save()
                    if artifact.quantity == 0:
                        prohibit_further_bidding(request, id=artifact.id)
                    else:
                        adjust_bidding_quantity(request, id=artifact.id)
                bid_cart = request.session.get("bid_cart", {})
                for id, bid_id in bid_cart.items():
                    bid = get_object_or_404(BidLineItem, pk=bid_id)
                    bid.bid_event.artifact.quantity -= bid.bid_quantity
                    bid.bid_event.artifact.save()
                    bid.bid_paid = True
                    bid.save()
                
                # Clearing of carts
                request.session["cart"] = {}
                request.session["bid_cart"] = {}
                
                return redirect(reverse('artifacts'))
            
            else:
                messages.error(request, "We were unable to process payment.")
        else:
            messages.error(request, "We were unable to process payment.")
    else:
        payment_form = PaymentDetailsForm()
        order_form = OrderDetailsForm()
    
    return render(request, "payment.html", {
        "order_form": order_form,
        "payment_form": payment_form,
        "publishable": settings.STRIPE_PUBLISHABLE
        })


