from django import forms
#from bids.models import BidEvent

class BidDetailsForm(forms.Form):
    """
    Form for capturing a bid 
    related to a specific artifact 
    by a specific user. 
    """
    
    bid_amount = forms.DecimalField(
        label="Bid Amount",
        max_digits=10,
        min_value=0.00,
        decimal_places=2,
        required=True
        )
    
    bid_quantity = forms.IntegerField(
        label="Bid Quantity",
        min_value=1,
        required=True,
        )
    