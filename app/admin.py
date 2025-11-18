from django.contrib import admin
from .models import Items

# Register your models here.

class ItemsAdmin(admin.ModelAdmin):
    list_display = ('price', 'quantity', 'description')

admin.site.register(Items, ItemsAdmin)