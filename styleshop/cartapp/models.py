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

# class Delivery(models.Model):

#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
#     cart = models.ForeignKey(Cart, on_delete=models.DO_NOTHING)
#     country = models.CharField(max_length=30, required=True)
#     city = models.CharField(max_length=30, required=True)
#     address = models.CharField(max_lenght=60, required=True)
#     terms_and_conitions = models.BooleanField(default=False)
