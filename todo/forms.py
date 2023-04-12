from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    # Meta inner class gives the form information about itself.
    # Such, which fields to include and how to display an error msg.
    class Meta:
        model = Item
        fields = ["name", "done"]
