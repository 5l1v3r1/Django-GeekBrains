from django.shortcuts import render
from . import models

def index(request):

    sections = models.Section.objects.all()
    
    return render(request, 'mainpage/index.html', {'sections': sections})
