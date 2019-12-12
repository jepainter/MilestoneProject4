from django.db import models
from categories.models import Category

# Model for artifacts
class Artifact(models.Model):
    
    name = models.CharField(max_length=100, default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, default="3")
    description = models.TextField()
    reserve_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to="images")
    
    def __str__(self):
        return self.name