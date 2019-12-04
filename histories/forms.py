from django import forms
from histories.models import History

class HistoryEventForm(forms.Form):
    """
    Form to capture detail regarding history of artifact
    """
    era_choices = [
        "BC", "AC", "Stone Age", "Bronze Age", "Iron Age",
        "Machine Age", "Atomic Age", "Space Age", "Information Age"
        ]
        
    class Meta:
        model = History
        fields = {
            "event_description",
            "event_year",
            "event_era",
        }