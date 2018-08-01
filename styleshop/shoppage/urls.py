
from django.urls import path
from shoppage.views import Shop, ProductDetails

urlpatterns = [
    path('category/<int:category_key>', Shop.as_view()),
    path('section/<int:section_key>', Shop.as_view()),
    path('brand/<int:brand_key>', Shop.as_view()),
    path('', Shop.as_view()),
    path('<int:pk>/', ProductDetails.as_view()),
]
