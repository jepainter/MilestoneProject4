from django.db import models
from categories.models import Category

# Model for artifact to be listed in database
class Artifact(models.Model):
    """
    Model for artifact
    """
    name = models.CharField(max_length=100, default="")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=False,
        default="")
    description = models.TextField(null=False)
    reserve_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False)
    purchase_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False)
    quantity = models.IntegerField(null=False, default=0)
    image = models.ImageField(upload_to="images")
    
    def __str__(self):
        return self.name