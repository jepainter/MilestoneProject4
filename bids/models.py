from django.db import models
from django.contrib.auth.models import User
from artifacts.models import Artifact

# Models for bidding related to an artifact
class BidEvent(models.Model):
    """
    Model for general bidding information assicated to a specific artifact
    """
    
    artifact = models.ForeignKey(Artifact, on_delete=models.CASCADE, null=False)
    artifact_purchased = models.BooleanField(null=False, default=False)
    bid_event_deadline = models.DateTimeField(null=True)
    
    def __str__(self):
        return "Bid Event Id: {0} for Artifact Name: {1} with Reserve Price: {2}".format(
            self.id,
            self.artifact.name,
            self.artifact.reserve_price,
            )


class BidLineItem(models.Model):
    """
    Model for specific bid placed by user on specific artifact
    """
    
    bid_event = models.ForeignKey(
        BidEvent, on_delete=models.CASCADE, null=False)
    bid_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=False)
    bid_quantity = models.IntegerField(
        null=False, default=1)
    bid_note = models.CharField(max_length=100, default="No note")
    bid_user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, default=1)
    bid_highest = models.BooleanField(
        null=False, default=False)
    bid_paid = models.BooleanField(
        null=False, default=False)
    bid_date_time = models.DateTimeField(
        null=True)
    bid_archived = models.BooleanField(
        null=False, default=False)
    
    def __str__(self):
        return "Bid Line Id: {0} for Bid Event Id: {1} by Bidder: {2}".format(
            self.id,
            self.bid_event.id,
            self.bid_user,
            )




