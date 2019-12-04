from django.contrib import admin
from histories.models import History, HistoryEvent

# Registering History model to be available in admin panel
class HistoryEventAdminInline(admin.TabularInline):
    model = HistoryEvent
    
class HistoryAdmin(admin.ModelAdmin):
    inlines = (HistoryEventAdminInline, )

admin.site.register(History, HistoryAdmin)


