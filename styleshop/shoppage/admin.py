from django.contrib import admin
from . import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'category', 'brand', 'cost', 'sale')
    list_filter = ('category', 'brand')

    search_fields = ('name',)

    fieldsets = (
        ('Information', {
            'fields': ('name', ('category', 'brand', 'sex'),)
        }),
        ('Content', {
            'fields': (('cost', 'sale'), 'images', 'description')
        })
    )
