from django.contrib import admin
from reviews.models import Review, ReviewLineItem

# Registering Review model to be available in admin panel
class ReviewLineAdminInline(admin.TabularInline):
    model = ReviewLineItem
    
class ReviewAdmin(admin.ModelAdmin):
    inlines = (ReviewLineAdminInline, )

admin.site.register(Review, ReviewAdmin)
