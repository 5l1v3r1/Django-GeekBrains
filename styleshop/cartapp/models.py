from django.db import models
from django.conf import settings
from shoppage.models import Product
from styleshop import lib

class Cart(models.Model):
    """Для обращения к словарю товаров необходимо вызвать cart.products, так как cart - единственный объект корзины\n
Для обращения к конкретному товару по ключу необходимо вызвать cart.products[str(key)]\n
Сама структура имеет вид:\n
cart = {
    'id': ...,
    'user': ...,
    'products': {
        'ключ товара': {
            'id': product.id,
            'name': product.name,
            'category': product.category.name,
            'sex': product.sex.name,
            'brand': product.brand.name,
            'image': product.images.name,
            'cost': float(product.cost),
            'sale': product.sale,
            'quantity': 1,
        },
        ...
    },
}"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = lib.DictField()
    created = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def total_amount(request):
        
        if not request.user.is_anonymous:
            
            cart = Cart.objects.get(user=request.user)
            amount = sum([cart.products[obj]['quantity'] for obj in cart.products if cart.products])
            return amount

        return None

# class Delivery(models.Model):

#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
#     cart = models.ForeignKey(Cart, on_delete=models.DO_NOTHING)
#     country = models.CharField(max_length=30, required=True)
#     city = models.CharField(max_length=30, required=True)
#     address = models.CharField(max_lenght=60, required=True)
#     terms_and_conitions = models.BooleanField(default=False)
