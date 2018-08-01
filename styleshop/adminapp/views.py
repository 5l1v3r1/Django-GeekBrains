from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.http import QueryDict
from . import forms
from shoppage.models import Product

class CreateProduct(CreateView):

    model = Product
    form_class = forms.ProductForm
    success_url = '/shop'
    template_name = 'adminapp/form.html'
