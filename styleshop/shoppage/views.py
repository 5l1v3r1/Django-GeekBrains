from django.shortcuts import render
from . import models

def shop(request):

    products = models.Product.objects.all()

    return render(request, 'shoppage/shop.html', {'products': products})

def single_product_details(request):

    pass
