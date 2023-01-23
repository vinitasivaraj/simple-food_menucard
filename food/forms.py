from .models import items
from django import forms

class ItemForm(forms.ModelForm):
    class Meta:
        model=items
        fields=['item_name','item_desc','item_price','item_image']
        labels={"item_name":"Name",'item_desc':"describe","item_price":"Price","item_image":"Add Image"}


