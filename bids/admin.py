from django.contrib import admin
from bids.models import Bid, BidLineItem

# Registering Bid model to be available in admin panel
class BidLineAdminInline(admin.TabularInline):
    model = BidLineItem

class BidAdmin(admin.ModelAdmin):
    inlines = (BidLineAdminInline, )

admin.site.register(Bid, BidAdmin)
