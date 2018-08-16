from django.shortcuts import render, HttpResponseRedirect, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, View, DeleteView, FormView
from cartapp.models import Cart
from mainpage.models import Section, Category, Brand
from shoppage.models import Product
# from cartapp.forms import DeliveryForm

class CartView(ListView):

    model = Cart
    template_name = 'cartapp/cart.html'
    context_object_name = 'cart'

    def get_queryset(self, **kwargs):
        
        if self.request.user.is_anonymous:
            return None

        return super().get_queryset().get(user=self.request.user)

    def get_context_data(self, **kwargs):

        if self.request.user.is_anonymous:

            context = {'errors': ['Для доступа к корзине требуется вход в систему']}

            return context

        context = super().get_context_data(**kwargs)

        cart = context['cart']
        subtotal_price = 0
        total_price = 0

        for obj in cart:

            subtotal_price += float(obj.product.cost) * int(obj.quantity)
            total_price += float(obj.product.cost) * (100. - float(obj.product.sale)) / 100 * int(obj.quantity)

        context['subtotal_price'] = subtotal_price
        context['total_price'] = total_price
        context['amount'] = Cart.total_amount(self.request)
        context['sections'] = Section.objects.all()
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        
        return context

class CartAdd(View):

    def add_product(self, product, dictionary):

        dictionary[product.id] = {
            'id': product.id,
            'name': product.name,
            'category': product.category.name,
            'sex': product.sex.name,
            'brand': product.brand.name,
            'image': product.images.name,
            'cost': float(product.cost),
            'sale': product.sale,
            'quantity': 1,
        }

        return dictionary

    def get(self, request, pk):

        if request.user.is_anonymous:
            return render(request, 'cartapp/cart.html', {
                'errors': ['Для добавления товара в корзину необходимо авторизоваться']
            })

        product = Product.objects.get(pk=pk)
        cart = Cart.objects.get(user=request.user)
        
        print('-'*200)
        print('IN ADD_TO_CART')
        print(cart.products)

        if str(product.id) in cart.products:
            
            if product.quantity - cart.products[str(product.id)]['quantity'] != 0:
                cart.products[str(product.id)]['quantity'] += 1
                print('-'*200)
                print('AFTER CHANGING QUANTITY')
                print(cart.products)
                print('-'*200)
                cart.save()
                return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))

            return render(self.request, 'cartapp/cart.html', {
                'errors': ['На складе больше нет товара {}'.format(product.name)]
            })

        self.add_product(product, cart.products)
        
        print('-'*200)
        print('AFTER ADDING')
        print(cart.products)
        print('-'*200)

        cart.save()

        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
        
class CartDelete(DeleteView):
    
    model = Cart
    success_url = '/cart'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

# class DeliveryView(FormView):
    
#     form_class = DeliveryForm
#     template_name = 'cartapp/checkout.html'
#     success_url = '/'
