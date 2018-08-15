from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView
from . import models
from mainpage.models import Section, Category, Brand

class CartView(ListView):

    model = models.Cart
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
        amount = 0

        for obj in cart:

            subtotal_price += float(obj.product.cost) * int(obj.quantity)
            total_price += float(obj.product.cost) * (100. - float(obj.product.sale)) / 100 * int(obj.quantity)
            amount += obj.quantity

        context['subtotal_price'] = subtotal_price
        context['total_price'] = total_price
        context['amount'] = amount
        context['sections'] = Section.objects.all()
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        
        return context