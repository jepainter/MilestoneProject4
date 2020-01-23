from django.db import models
from artifacts.models import Artifact

# Models for reviews of items purchased by a user
class Review(models.Model):
    """
    Review instance for a specific artifact
    """
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
    """
    Review line for multiple reviews where more than one artifact
    is purchased by different users
    """
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