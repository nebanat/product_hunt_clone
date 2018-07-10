from django.shortcuts import render
from django.http import HttpResponse


# Create your auth_views here.
def index(request):
    return render(request, 'product/index.html')
