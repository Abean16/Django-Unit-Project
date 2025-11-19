from django.contrib import admin
from .models import Items

# Register your models here.

class ItemsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'image', 'category')

admin.site.register(Items, ItemsAdmin)