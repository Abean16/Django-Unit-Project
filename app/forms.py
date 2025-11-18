from django import forms
from .models import Items

class ItemsModelForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['price', 'quantity', 'description']