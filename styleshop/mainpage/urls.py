from django.urls import path
from mainpage.views import Index 

urlpatterns = [
    path('', Index.as_view(), name='main'),
]
