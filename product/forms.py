from django.forms import ModelForm, TextInput, Textarea
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'link', 'description']

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

