from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormView
from .forms import CommentForm
from product.models import Product


# Create your views here.
class CommentFormView(FormView):
    form_class = CommentForm

    def get_success_url(self):
        return self.request.POST.get('next', '/')+'#comment-form'

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.request.POST.get('product'))
        form.instance.product = product
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
