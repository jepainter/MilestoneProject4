from django.contrib import admin
from categories.models import Category

# Registering Category model to be available in admin panel
admin.site.register(Category)
