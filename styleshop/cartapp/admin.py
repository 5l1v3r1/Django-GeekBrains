from django.contrib import admin
from . import models

@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = ('user', 'products_name', 'created',)
    list_filter = ('created',)
    readonly_fields = list_display

    def products_name(self, obj):

        res = '; '.join(['{}, {}'.format(val['name'], val['quantity']) for val in obj.products.values()])
        return res

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ('user', 'products_name', 'created')
    list_filter = ('created',)
    search_fields = ('products',)
    readonly_fields = list_display

    def products_name(self, obj):

        res = '; '.join(['Товар {} в количестве {}'.format(val['name'], val['quantity']) \
            for val in obj.products.values()])
        return res
