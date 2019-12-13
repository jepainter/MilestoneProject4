from django.db import models
from artifacts.models import Artifact

# Models for bidding related to an artifact
class BidEvent(models.Model):
    """
    Model for general bidding information assicated to a specific artifact
    """
    
    artifact = models.ForeignKey(Artifact, on_delete=models.CASCADE, null=False)
    highest_bid = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return "Bid Event Id: {0} for Artifact Id: {1} - Artifact Name: {2} - Reserve Price: {3} - Highest Bid: {4}".format(
            self.id,
            self.artifact.id,
            self.artifact.name,
            self.artifact.reserve_price,
            self.highest_bid,
            )

class BidLineItem(models.Model):
    """
    Model for specific bid placed by user on specific artifact
    
    Check acces to artifact object via bid id
    """
    
    bid_event = models.ForeignKey(BidEvent, on_delete=models.CASCADE, null=False)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    bid_quantity = models.IntegerField(null=False, default=1)
    #user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return "Bid Line Id: {0} for Bid Event Id: {1} by Bidder:  with Bid: {2} of Quantity: {3}".format(
            self.id,
            self.bid_event.id,
            #self.user_id,
            self.bid_amount,
            self.bid_quantity,
            )




