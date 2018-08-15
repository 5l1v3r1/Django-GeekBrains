from django.shortcuts import render
from django.views.generic import View
from . import models
from cartapp.models import Cart

class Index(View):

    def get(self, request):

        sections = models.Section.objects.all()
        brands = models.Brand.objects.all()
        categories = models.Category.objects.all()
        amount = 0
        
        if not request.user.is_anonymous:
            cart = Cart.objects.filter(user=self.request.user)
            if cart:
                for obj in cart:
                    amount += obj.quantity

        return render(
            request, 'mainpage/index.html', 
            {
                'sections': sections, 
                'brands': brands,
                'categories': categories,
                'amount': amount
            }
        )
