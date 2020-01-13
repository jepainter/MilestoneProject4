from django import forms
from reviews.models import ReviewLineItem

class ReviewForm(forms.ModelForm):
    """
    Form to capture review for a purchased artifact
    """
    class Meta:
        model = ReviewLineItem
        fields = {
            "review_detail",
            "review_owner_name",
        }