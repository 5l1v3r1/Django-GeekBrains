from django.urls import path
from . import views

urlpatterns = [
    path('product', views.TableProduct.as_view()),
    path('product/create', views.CreateProduct.as_view(), name='create_product'),
    path('product/update/<int:pk>', views.UpdateProduct.as_view()),
    path('product/delete/<int:pk>', views.DeleteProduct.as_view()),
    # path('brand'),
    # path('brand/create'),
    # path('brand/update/<int:pk>'),
    # path('brand/delete/<int:pk>'),
    # path('sex'),
    # path('sex/create'),
    # path('sex/update/<int:pk>'),
    # path('sex/delete/<int:pk>'),
    # path('category'),
    # path('category/create'),
    # path('category/update/<int:pk>'),
    # path('category/delete/<int:pk>'),
    # path('section'),
    # path('section/create'),
    # path('section/update/<int:pk>'),
    # path('section/delete/<int:pk>'),
    # path('user'),
    path('', views.MainView.as_view())
]