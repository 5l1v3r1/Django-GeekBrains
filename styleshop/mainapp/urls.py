from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout),
    path('contact/', views.contact),
    path('shop/', views.shop),
    path('single-product-details/', views.single_product_details),
]