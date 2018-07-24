from django.shortcuts import render
from . import models
from mainpage.models import Section, Category, Brand

def shop(request):

    products = models.Product.objects.all()
    sections = Section.objects.all()
    categories = Category.objects.all()
    brands = Brand.objects.all()

    return render(
        request, 'shoppage/shop.html', 
        {
            'products': products,
            'sections': sections,
            'categories': categories,
            'brands': brands,
        }
    )

def single_product_details(request):

    return render(request, 'shoppage/single-product-details.html')
