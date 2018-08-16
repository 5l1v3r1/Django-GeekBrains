from django.contrib import admin
from . import models

@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = ('user', 'products', 'created',)
    list_filter = ('created',)
    readonly_fields = list_display
