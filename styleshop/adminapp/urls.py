from django.urls import path
from . import views

urlpatterns = [
    path('product', views.TableProduct.as_view()),
    path('product/create', views.CreateProduct.as_view()),
    path('product/update/<int:pk>', views.UpdateProduct.as_view()),
    path('product/delete/<int:pk>', views.DeleteProduct.as_view()),
    path('brand', views.TableBrand.as_view()),
    path('brand/create', views.CreateBrand.as_view()),
    path('brand/update/<int:pk>', views.UpdateBrand.as_view()),
    path('brand/delete/<int:pk>', views.DeleteBrand.as_view()),
    path('category', views.TableCategory.as_view()),
    path('category/create', views.CreateCategory.as_view()),
    path('category/update/<int:pk>', views.UpdateCategory.as_view()),
    path('category/delete/<int:pk>', views.DeleteCategory.as_view()),
    path('section', views.TableSection.as_view()),
    path('section/create', views.CreateSection.as_view()),
    path('section/update/<int:pk>', views.UpdateSection.as_view()),
    path('section/delete/<int:pk>', views.DeleteSection.as_view()),
    path('sex', views.TableSex.as_view()),
    path('user', views.TableUser.as_view()),
    path('', views.MainView.as_view())
]