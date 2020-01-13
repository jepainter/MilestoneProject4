from django.db import models
from artifacts.models import Artifact

# Models for reviews of items purchased by a user
class Review(models.Model):
    
    artifact = models.ForeignKey(
        Artifact,
        on_delete=models.CASCADE,
        null=False
        )
    
    def __str__(self):
        return "Review for: {0} ".format(
            self.artifact.name
            )


class ReviewLineItem(models.Model):
    
    review_id = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        null=False
        )
    review_date = models.DateField()
    review_owner_name = models.CharField(max_length=50, blank=False)
    review_owner_id = models.CharField(max_length=10, blank=False)
    review_detail = models.TextField(blank=False)
    
    def __str__(self):
        return "Review by: {0}".format(
            self.review_owner_name,
            )