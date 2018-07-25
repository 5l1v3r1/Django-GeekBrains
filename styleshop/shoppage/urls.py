
from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.shop),
    path('<str:primary_key>/', views.single_product_details),
]
