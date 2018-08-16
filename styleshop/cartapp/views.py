from django.shortcuts import render, HttpResponseRedirect, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, View, DeleteView, FormView
from cartapp.models import Cart, Order
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
        products = cart.products
        subtotal_price = 0
        total_price = 0

        for val in products.values():

            subtotal_price += float(val['cost']) * int(val['quantity'])
            total_price += float(val['cost']) * (100. - float(val['sale'])) / 100 * int(val['quantity'])

        context['cart'] = products
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
                'errors_quantity': ['Для добавления товара в корзину необходимо авторизоваться']
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
                'errors_quantity': ['На складе больше нет товара {}'.format(product.name)]
            })

        self.add_product(product, cart.products)
        
        print('-'*200)
        print('AFTER ADDING')
        print(cart.products)
        print('-'*200)

        cart.save()

        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
        
class CartDelete(View):

    def get(self, request, pk):

        cart = Cart.objects.get(user=request.user)
        del(cart.products[str(pk)])
        cart.save()

        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))

class OrderView(View):

    def dispatch(self, request, *args, **kwargs):
        
        cart = Cart.objects.get(user=request.user)

        for val in cart.products.values():

            product = Product.objects.get(id=val['id'])
            
            if product.quantity < val['quantity']:
                return render(request, 'cartapp/cart.html', {
                    'error_quantity': 'Товара {} в количестве {} больше нет на складе'.format(
                        val['name'], val['quantity'])
                })

        return super(OrderView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        
        cart = Cart.objects.get(user=request.user)

        for val in cart.products.values():

            product = Product.objects.get(id=val['id'])
            product.quantity -= val['quantity']
            product.save()

        Order(user=request.user, products=cart.products).save()

        cart.products = dict()
        cart.save()

        return render(request, 'cartapp/cart.html', {'success_text': 'Благодарим за заказ'})
