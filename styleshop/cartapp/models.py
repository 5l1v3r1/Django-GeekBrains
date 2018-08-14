from django.db import models
from django.conf import settings
from shoppage.models import Product

class Cart(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)


