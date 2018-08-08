from django.contrib import admin
from django.template.loader import render_to_string
from . import models

@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'picture')

    def picture(self, obj):

        return render_to_string('mainpage/admin/picture.html', {'image': obj.image})

admin.site.register(models.Section)
admin.site.register(models.Sex)
admin.site.register(models.Category)
