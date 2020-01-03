from django import forms
from payment.models import Order

class PaymentDetailsForm(forms.Form):
    """
    Form for capturing payment details.  Fields set to required=False for
    security reasons, security dealt with by Stripe JavaScript.  This
    prevents info to be sent in plain text
    """
    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2039)]
    
    credit_card_number = forms.CharField(
        label="Card number",
        required=False
        )
    cvv = forms.CharField(
        label="Security code (CVV)",
        required=False
        )
    expiry_month = forms.ChoiceField(
        label="Expiry month",
        choices=MONTH_CHOICES,
        required=False
        )
    expiry_year = forms.ChoiceField(
        label="Expiry year",
        choices=YEAR_CHOICES,
        required=False
        )
    stripe_id = forms.CharField(
        widget=forms.HiddenInput
        )

class OrderDetailsForm(forms.ModelForm):
    """
    Form for capturing delivery address details,
    inherits from the Order model.    
    """
    class Meta:
        model = Order
        fields = {
            "full_name",
            "phone_number",
            "address_line1",
            "address_line2",
            "town_or_city",
            "postcode",
            "county_or_province_or_state",
            "country",
            }