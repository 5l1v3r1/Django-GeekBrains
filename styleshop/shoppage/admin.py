from django.contrib import admin
from django.template.loader import render_to_string
from . import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'picture', 'category', 'brand', 'quantity', 'cost', 'sale')
    list_filter = ('category', 'brand')

    search_fields = ('name',)

    fieldsets = (
        ('Information', {
            'fields': (('name', 'quantity'), ('category', 'brand', 'sex'),)
        }),
        ('Content', {
            'fields': (('cost', 'sale'), 'images', 'description')
        })
    )

    def picture(self, obj):

        return render_to_string('shoppage/admin/picture.html', {'image': obj.images})
