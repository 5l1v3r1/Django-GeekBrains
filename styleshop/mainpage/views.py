from django.shortcuts import render
from . import models

def index(request):

    sections = models.Section.objects.all()
    brands = models.Brand.objects.all()
    
    return render(request, 'mainpage/index.html', {'sections': sections, 'brands': brands})
