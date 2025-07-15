from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['store',]

class RequestForm(forms.ModelForm):
    class Meta:
        model = StoreRequest
        fields = '__all__'
