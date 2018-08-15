from django.shortcuts import render, get_object_or_404
from django.views.generic import View, DetailView, ListView
from django.core.paginator import Paginator
from . import models
from mainpage.models import Section, Category, Brand
from cartapp.models import Cart

class ShopList(ListView):

    model = models.Product
    template_name = 'shoppage/shop.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['amount'] = Cart.total_amount(self.request)
        context['sections'] = Section.objects.all()
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        context['page_title'] = 'Все товары'
        
        return context

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

        if category_key:
            all_products = models.Product.objects.filter(category_id=category_key)
            page_title = self.get_page_title([i for i in categories], category_key)

        elif section_key:
            all_products = self.get_products_with_section_key(section_key)
            page_title = self.get_page_title([i for i in sections], section_key)

        elif brand_key:
            all_products = models.Product.objects.filter(brand_id=brand_key)
            page_title = self.get_page_title([i for i in brands], brand_key)

        paginator = Paginator(all_products, 6)
        page = request.GET.get('page')
        if not page:
            page = 1
            
        all_products = paginator.get_page(page)
        
        return render(
            request, 'shoppage/shop.html', 
            {
                'page_obj': all_products,
                'sections': sections,
                'categories': categories,
                'brands': brands,
                'page_title': page_title,
                'amount': Cart.total_amount(request)
            }
        )

class ProductDetails(DetailView):
    
    model = models.Product
    template_name = 'shoppage/single-product-details.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        
        context['amount'] = Cart.total_amount(self.request)
        context['sections'] = Section.objects.all()
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()

        return context
