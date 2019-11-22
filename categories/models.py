from django.db import models

# Model for categories under which artifacts fall
class Category(models.Model):
    
    category_name = models.CharField(max_length=50, default="")
    category_description = models.TextField(default="")
    image = models.ImageField(upload_to="images/categories")
    
    def __str__(self):
        return self.category_name
