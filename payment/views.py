from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from artifacts.models import Artifact
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
                    quantity = quantity
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
                request.session["cart"] = {}
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