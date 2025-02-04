from django import forms
from .models import Product

class Productform(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description' , 'price', 'image']
        widgets = {
            'name' : forms.TextInput(),
            'description' : forms.Textarea(),
            'price':  forms.NumberInput(),
            'image': forms.FileInput()
        }
   
   
