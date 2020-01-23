from django import forms
from django.utils.translation import gettext_lazy as _
from histories.models import HistoryEvent

class HistoryEventForm(forms.ModelForm):
    """
    Form to capture detail regarding an event in history of artifact
    """
    event_year = forms.IntegerField(
        required=True,
        min_value=0,
        label="Event Year:",
        widget=forms.NumberInput(
            attrs={'placeholder': 'What was the year...'})
        )
    event_description = forms.CharField(
        required=True,
        label="Event Description:",
        widget=forms.Textarea(
            attrs={
                'cols': 30,
                'rows': 5,
                'placeholder': 'Describe what happened...'
                })
        )
    field_order = ['event_year', 'event_era', 'event_description']
    
    class Meta:
        model = HistoryEvent
        fields = {
            "event_year",
            "event_era",
            "event_description",
        }
        labels = {
            'event_era': _('Event Era:'),
        }