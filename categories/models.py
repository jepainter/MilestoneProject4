from django.db import models

# Model for categories under which artifacts fall
class Category(models.Model):
    
    category_name = models.CharField(max_length=50, null=False)
    category_description = models.TextField(null=False)
    image = models.ImageField(upload_to="images/categories")
    
    def __str__(self):
        return self.category_name
