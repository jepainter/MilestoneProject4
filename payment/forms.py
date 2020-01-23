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
        label="Card Number:",
        widget=forms.TextInput(
            attrs={
                'placeholder': "Enter a valid card number..."
                }),
        required=False
        )
    cvv = forms.CharField(
        label="Security Code (CVV):",
        widget=forms.TextInput(
            attrs={
                'placeholder': "Enter the CVV on the back of the card..."
                }),
        required=False
        )
    expiry_month = forms.ChoiceField(
        label="Expiry Month:",
        choices=MONTH_CHOICES,
        required=False
        )
    expiry_year = forms.ChoiceField(
        label="Expiry Year:",
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
    full_name = forms.CharField(
        label="Full Name:",
        widget=forms.TextInput(
            attrs={
                'placeholder': "Who should the receive the purchase..."
                })
        )
    phone_number = forms.CharField(
        label="Phone Number:",
        widget=forms.TextInput(
            attrs={
                'placeholder': "Please add a contact number..."
                })
        )
    address_line1 = forms.CharField(
        label="Address Line 1:",
        widget=forms.TextInput(
            attrs={
                'placeholder': "Please enter the address..."
                })
        )
    address_line2 = forms.CharField(
        label="Address Line 2:",
        widget=forms.TextInput(
            attrs={
                'placeholder': "Please enter the address..."
                })
        )
    town_or_city = forms.CharField(
        label="Town or City:",
        widget=forms.TextInput(
            attrs={
                'placeholder': "Please enter the town or city..."
                })
        )
    postcode = forms.CharField(
        label="Postcode:",
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': "Please enter a postcode..."
                })
        )
    county_or_province_or_state = forms.CharField(
        label="County, Province or State:",
        widget=forms.TextInput(
            attrs={
                'placeholder': "Please enter a county, province or state..."
                })
        )
    country = forms.CharField(
        label="Country:",
        widget=forms.TextInput(
            attrs={
                'placeholder': "Please enter a country..."
                })
        )
    
    field_order = [
        "full_name",
        "phone_number",
        "address_line1",
        "address_line2",
        "town_or_city",
        "postcode",
        "county_or_province_or_state",
        "country",
        ]
        
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