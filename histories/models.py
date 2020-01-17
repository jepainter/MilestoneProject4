from django.db import models
from artifacts.models import Artifact

# Models for history and events related to an artifact
class History(models.Model):
    
    artifact = models.ForeignKey(
        Artifact,
        on_delete=models.CASCADE,
        null=False
        )
    
    def __str__(self):
        return "History for: {0} ".format(
            self.artifact.name
            )


class HistoryEvent(models.Model):
    
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
    
    history_id = models.ForeignKey(
        History,
        on_delete=models.CASCADE,
        null=False,
        )
    event_year = models.IntegerField(blank=False)
    event_era = models.CharField(
        max_length=30,
        choices=ERA_CHOICES,
        default="Unassigned",
        blank=False,
        )
    event_description = models.TextField(blank=False)
    
    def __str__(self):
        return "{0} {1}: {2}".format(
            self.event_year,
            self.event_era,
            self.event_description,
            )
    