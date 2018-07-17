from django.db import models
from django.contrib.auth.models import User
from product.models import Product


# Create your models here.
class Comment(models.Model):
    """
        A description of the comment model
        data: text, product(Foreign key),
    """
    text = models.CharField(max_length=400)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
