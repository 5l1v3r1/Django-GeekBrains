
from django.urls import path
from shoppage.views import Shop, ProductDetails

urlpatterns = [
    path('shop/', Shop.as_view()),
    path('shop/category/<int:category_key>', Shop.as_view()),
    path('shop/section/<int:section_key>', Shop.as_view()),
    path('shop/brand/<int:brand_key>', Shop.as_view()),
    path('<int:pk>/', ProductDetails.as_view()),
]
