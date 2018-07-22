"""styleshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp

urlpatterns = [
    path('', mainapp.index),
    path('index/', mainapp.index),
    path('blog/', mainapp.blog),
    path('checkout/', mainapp.checkout),
    path('contact/', mainapp.contact),
    path('regular-page/', mainapp.regular_page),
    path('shop/', mainapp.shop),
    path('single-blog/', mainapp.single_blog),
    path('single-product-details/', mainapp.single_product_details),
    path('admin/', admin.site.urls),
]
