from django.shortcuts import render, HttpResponseRedirect, redirect
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, View, DeleteView
from cartapp.models import Cart
from mainpage.models import Section, Category, Brand
from shoppage.models import Product

class CartView(ListView):

    model = Cart
    template_name = 'cartapp/cart.html'
    context_object_name = 'cart'

    def get_queryset(self, **kwargs):
        
        if self.request.user.is_anonymous:
            return None

        return super().get_queryset().filter(user=self.request.user)

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

class CartCreate(View):

    def get(self, request, pk):

        if request.user.is_anonymous:
            return render(request, 'cartapp/cart.html', {
                'errors': ['Для добавления товара в корзину необходимо авторизоваться']
            })

        product = Product.objects.get(pk=pk)
        old_cart_product = Cart.objects.filter(user=request.user, product=product)

        if old_cart_product:

            if product.quantity - old_cart_product[0].quantity != 0:
                old_cart_product[0].quantity += 1
                old_cart_product[0].save()

            else:
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        else:
            new_cart_product = Cart(user=request.user, product=product, quantity=1)
            new_cart_product.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class CartDelete(DeleteView):
    
    model = Cart
    success_url = '/cart'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
