from django.db import models
from artifacts.models import Artifact

# Models for bidding related to an artifact
class Bid(models.Model):
    """
    Model for general bidding information assicated to a specific artifact
    """
    
    artifact = models.ForeignKey(Artifact, on_delete=models.CASCADE, null=False)
    highest_bid = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return "{0} - {1} ID: {2} - Reserve Price: {3} - Highest Bid: {4}".format(
            self.id,
            self.artifact.name,
            self.artifact.id,
            self.artifact.reserve_price,
            self.highest_bid,
            )

class BidLineItem(models.Model):
    """
    Model for specific bid placed by user on specific artifact
    
    Check acces to artifact object via bid id
    """
    
    bid_id = models.ForeignKey(Bid, on_delete=models.CASCADE, null=False)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    #user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return "Bid ID: {0} - Bidder:  - Bid: {1}".format(
            self.bid_id,
            #self.user_id,
            self.bid_amount,
            )




