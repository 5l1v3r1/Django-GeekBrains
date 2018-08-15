from django.db import models
from django.conf import settings
from shoppage.models import Product

class Cart(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def total_amount(request):
        
        if not request.user.is_anonymous:
            
            cart = Cart.objects.filter(user=request.user)
            # amount = sum(list(map(lambda obj: obj.quantity, cart)))
            amount = sum([obj.quantity for obj in cart])
            return amount

        return None
