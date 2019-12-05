from django import forms
from histories.models import HistoryEvent

class HistoryEventForm(forms.ModelForm):
    """
    Form to capture detail regarding an event in history of artifact
    """
    class Meta:
        model = HistoryEvent
        fields = {
            "event_year",
            "event_era",
            "event_description",
        }