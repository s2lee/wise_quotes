from django.contrib import admin

# Register your models here.
from .models import WiseQuotes


class WiseQuotesAdmin(admin.ModelAdmin):    
    list_display = ['title', 'like', 'date'] 
    class Meta:
        model = WiseQuotes

admin.site.register(WiseQuotes, WiseQuotesAdmin)