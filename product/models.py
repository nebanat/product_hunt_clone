import uuid
from django.db import models
from django.contrib.auth.models import User

app_label = 'product'


# Create your models here.
class Product(models.Model):
    """
        A description of the product model
        data: name, description, website(optional),
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=250)
    link = models.URLField(default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
