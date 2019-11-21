from django.contrib import admin
from payment.models import Order, OrderLineItem

# Register model for management in admin view
class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem
    
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )

admin.site.register(Order, OrderAdmin)