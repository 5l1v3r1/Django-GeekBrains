from django.shortcuts import render
from . import forms

def create(request):

    form = forms.ProductForm
    name = 'Товар'

    return render(request, 'adminapp/form.html', {'form': form, 'name': name})
