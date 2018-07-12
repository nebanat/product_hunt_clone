from django.urls import reverse
from django.contrib import messages
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView

from .forms import ProductForm
from .models import Product


@method_decorator(login_required, name='dispatch')
class ProductCreateView(FormView):
    """
        view for creating a new product
    """
    form_class = ProductForm
    template_name = 'product/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Product created successfully')
        return reverse('product:create')


class ProductDetailView(generic.DetailView):
    context_object_name = 'product'
    model = Product
    template_name = 'product/single_detail.html'


class ProductListView(generic.ListView):
    context_object_name = 'products'
    model = Product
    template_name = 'product/index.html'

