from django.contrib import admin
from artifacts.models import Artifact

# Registering Artifact model to be available in admin panel
admin.site.register(Artifact)