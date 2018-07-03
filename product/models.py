from django.db import models


# Create your models here.
class Product(models.Model):
    """
        A description of the product model
        data: name, description, website(optional),
    """
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=250)
    link = models.URLField(default='')
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class Comment(models.Model):
    """
        A description of the comment model
        data: text, product(Foreign key),
    """
    text = models.CharField(max_length=400)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

