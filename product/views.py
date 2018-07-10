from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views import View, generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import ProductForm
from .models import Product


@method_decorator(login_required, name='dispatch')
class ProductCreateView(View):
    """
        view for product creation
    """
    form_class = ProductForm
    initial = {'key': 'value'}
    template_name = 'product/create.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # clean up data
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            link = form.cleaned_data['link']

            # creates a new product
            new_product = Product(name=name, description=description, link=link)
            new_product.save()

            messages.success(request, 'Product created successfully')
            return HttpResponseRedirect(reverse('product:create'))


class ProductListView(generic.ListView):
    model = Product
    template_name = 'product/index.html'
