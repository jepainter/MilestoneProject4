from django.db import models
from artifacts.models import Artifact

class Order(models.Model):
    """
    Model for managing payments
    """
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    address_line1 = models.CharField(max_length=50, blank=False)
    address_line2 = models.CharField(max_length=50, blank=False)
    town_or_city = models.CharField(max_length=50, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    county_or_province_or_state = models.CharField(max_length=50, blank=False)
    country = models.CharField(max_length=50, blank=False)
    date = models.DateField()
    
    def __str__(self):
        return "{0} - {1} - {2}".format(self.id, self.date, self.full_name)
        
class OrderLineItem(models.Model):
    """
    Model for managing individual line items of order
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    artifact = models.ForeignKey(Artifact, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(blank=False)
    bid = models.CharField(max_length=20, blank=True)
    owner_id = models.CharField(max_length=10, blank=False, default="1")
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=False)
    
    def __str__(self):
        return "{0} - {1} at {2} each".format(
            self.quantity,
            self.artifact.name,
            self.unit_price
            ) 