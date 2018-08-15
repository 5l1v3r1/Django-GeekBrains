from django.contrib import admin
from . import models

@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = ('user', 'product', 'quantity', 'created',)
    list_filter = ('created',)
