
from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.shop),
    path('<int:primary_key>/', views.single_product_details),
]
