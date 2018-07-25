from django.shortcuts import render, get_object_or_404
from . import models
from mainpage.models import Section, Category, Brand

def get(what_to_return, product):
    
    if what_to_return == 'category':
        return product.category.id
    
    elif what_to_return == 'section':
        return product.category.section.id
    
    else:
        return product.brand.id

def get_products(all_products, key, field_name):

    products = list()

    for product in all_products:

        if get(field_name, product) == key:
            products.append(product)

    return products

def get_page_title(items, key):

    for item in items:

        if item.id == key:
            return item.name

def shop(request, category_key=None, section_key=None, brand_key=None):

    all_products = models.Product.objects.all()
    sections = Section.objects.all()
    categories = Category.objects.all()
    brands = Brand.objects.all()

    page_title = 'Все товары'

    if category_key:
        all_products = get_products(all_products, category_key, 'category')
        page_title = get_page_title([i for i in categories], category_key)

        # products = list()

        # for product in all_products:
        #     if product.category.id == category_key:
        #         products.append(product)

        # all_products = products
        
        # for category in categories:
        #     if category.id == category_key:
        #         page_title = str(category.name)
        #         break
    
    elif section_key:
        all_products = get_products(all_products, section_key, 'section')
        page_title = get_page_title([i for i in sections], section_key)

        # products = list()

        # for product in all_products:
        #     if product.category.section.id == section_key:
        #         products.append(product)

        # all_products = products
        
        # for section in sections:
        #     if section.id == section_key:
        #         page_title = str(section.name)
        #         break

    elif brand_key:
        all_products = get_products(all_products, brand_key, 'brand')
        page_title = get_page_title([i for i in brands], brand_key)

    count = len(all_products)

    return render(
        request, 'shoppage/shop.html', 
        {
            'products': all_products,
            'sections': sections,
            'categories': categories,
            'brands': brands,
            'count': count,
            'page_title': page_title
        }
    )

def single_product_details(request, primary_key):

    product = get_object_or_404(models.Product, id=primary_key)

    return render(
        request, 'shoppage/single-product-details.html', 
        {'product': product}
    )
