from django.urls import path
from . import views

urlpatterns = [
    path('product/create', views.CreateProduct.as_view(), name='create_product'),
    path('product/update/<int:pk>', views.UpdateProduct.as_view()),
    path('product/delete/<int:pk>', views.DeleteProduct.as_view()),
]