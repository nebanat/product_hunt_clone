from django.forms import ModelForm, TextInput, Textarea, Select
from .models import Product, Category


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'link', 'description', 'categories']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget = TextInput(attrs={
            'class': 'input'
        })
        self.fields['link'].widget = TextInput(attrs={
            'class': 'input'
        })
        self.fields['description'].widget = Textarea(attrs={
            'class': 'textarea'
        })


