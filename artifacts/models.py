from django.db import models

class Artifact(models.Model):
    """
    This is the model for the artifacts to be sold/auctioned via the webapp
    """
    
    name = models.CharField(max_length=100, default="")
    description = models.TextField()
    reserve_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to="images")
    
    def __str__(self):
        return self.name