from django import forms
from reviews.models import ReviewLineItem

class ReviewForm(forms.ModelForm):
    """
    Form to capture review for a purchased artifact
    """
    review_owner_name = forms.CharField(
        required=True,
        label="Name:",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'What name do you want show...'
                })
        )
    review_detail = forms.CharField(
        required=True,
        label="Review:",
        widget=forms.Textarea(
            attrs={
                'cols': 30,
                'rows': 5,
                'placeholder': 'Write your review...'
                })
        )
    
    field_order = ["review_detail", "review_owner_name"]
    
    class Meta:
        model = ReviewLineItem
        fields = {
            "review_detail",
            "review_owner_name",
        }