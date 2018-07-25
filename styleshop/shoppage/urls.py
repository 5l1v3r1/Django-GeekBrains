
from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.shop),
    path('shop/category/<int:category_key>', views.shop),
    path('shop/section/<int:section_key>', views.shop),
    path('shop/brand/<int:brand_key>', views.shop),
    path('<int:primary_key>/', views.single_product_details),
]
