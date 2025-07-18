from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['store',]

    def __init__(self, *args, **kwargs):
        store = kwargs.pop('store', None)
        super().__init__(*args, **kwargs)

        if store is None and self.instance.pk:
            store = self.instance.store

        if store is not None:
            self.fields['category'].queryset = Category.objects.filter(store=store)
        else:
            self.fields['category'].queryset = Category.objects.none()

class RequestForm(forms.ModelForm):
    class Meta:
        model = StoreRequest
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        exclude = ['store',]