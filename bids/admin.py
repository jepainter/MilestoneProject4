from django.contrib import admin
from bids.models import BidEvent, BidLineItem

# Registering Bid model to be available in admin panel
class BidLineAdminInline(admin.TabularInline):
    model = BidLineItem

class BidEventAdmin(admin.ModelAdmin):
    inlines = (BidLineAdminInline, )

admin.site.register(BidEvent, BidEventAdmin)
