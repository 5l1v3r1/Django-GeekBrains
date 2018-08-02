from django.shortcuts import render, get_object_or_404
from django.views.generic import View, DetailView
from . import models
from mainpage.models import Section, Category, Brand

class Shop(View):

    def get_page_title(self, items, key):

        for item in items:

            if item.id == key:
                return item.name

    def get_products_with_section_key(self, key):

        products = models.Product.objects.all()
        res = [item for item in products if item.category.section_id == key]

        return res

    def get(self, request, category_key=None, section_key=None, brand_key=None):

        sections = Section.objects.all()
        categories = Category.objects.all()
        brands = Brand.objects.all()
        user = request.user

        page_title = 'Все товары'

        if category_key:
            all_products = models.Product.objects.filter(category_id=category_key)
            page_title = self.get_page_title([i for i in categories], category_key)

        elif section_key:
            all_products = self.get_products_with_section_key(section_key)
            page_title = self.get_page_title([i for i in sections], section_key)

        elif brand_key:
            all_products = models.Product.objects.filter(brand_id=brand_key)
            page_title = self.get_page_title([i for i in brands], brand_key)

        if 'all_products' not in locals():
            all_products = models.Product.objects.all()

        count = len(all_products)

        return render(
            request, 'shoppage/shop.html', 
            {
                'products': all_products,
                'sections': sections,
                'categories': categories,
                'brands': brands,
                'count': count,
                'user': user,
                'page_title': page_title
            }
        )

class ProductDetails(View):
    
    template_name = 'shoppage/single-product-details.html'

    def get(self, request, pk):

        product = models.Product.objects.get(pk=pk)
        sections = Section.objects.all()
        categories = Category.objects.all()
        brands = Brand.objects.all()
        user = request.user

        return render(request, self.template_name, {
            'product': product,
            'sections': sections,
            'categories': categories,
            'brands': brands,
            'user': user
        }) 
