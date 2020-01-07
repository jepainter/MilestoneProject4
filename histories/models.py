from django.db import models
from artifacts.models import Artifact

# Models for history and events related to an artifact
class History(models.Model):
    """
    Model for history associated with a specific artifact
    """
    
    artifact = models.ForeignKey(Artifact, on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return "{0} - {1}: {2}".format(
            self.id,
            self.artifact.id,
            self.artifact.name
        )
    


class HistoryEvent(models.Model):
    """
    Model for specific event within a history
    """
    
    ERA_CHOICES = [
        ("Gregorian", (
                ("BC","BC"),
                ("AC","AC"),
            )
        ),
        ("Ages", (
                ("bronze", "Bronze Age"),
                ("iron", "Iron Age"),
                ("middle", "Middle Age"),
                ("atomic", "Atomic Age"),
                ("space", "Space Age"),
                ("information", "Information Age"),
            )
        ),
        ("Unassigned","Unassigned"),
        ]
    
    history_id = models.ForeignKey(History, on_delete=models.CASCADE, null=False)
    #artifact = models.ForeignKey(Artifact, on_delete=models.CASCADE, null=False)
    event_year = models.IntegerField(blank=False)
    event_era = models.CharField(max_length=50, choices=ERA_CHOICES, default="Unassigned")
    event_description = models.TextField(blank=False)
    
    def __str__(self):
        return "{0} - {1} {2}: {3}".format(
            self.history_id,
     #       self.artifact.id,
            self.event_year,
            self.event_era,
            self.event_description,
        )
    