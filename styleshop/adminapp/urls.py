from django.urls import path
from . import views

urlpatterns = [
    path('create/product', views.CreateProduct.as_view(), name='create_product')
]