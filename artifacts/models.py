from django.db import models
from categories.models import Category

# Model for artifact to be listed in database
class Artifact(models.Model):
    
    name = models.CharField(max_length=100, default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, default="3")
    description = models.TextField()
    reserve_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    #sold_out = models.BooleanField(default=False, null=False)
    #bidding_allowed = models.BooleanField(default=False, null=False)
    image = models.ImageField(upload_to="images")
    
    def __str__(self):
        return self.name