from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        # inner class to provide django with info of what we want
        model = Item
        fields = ('name', 'done')
