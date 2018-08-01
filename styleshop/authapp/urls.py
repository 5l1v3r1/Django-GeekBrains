from django.urls import path
import authapp.views as authapp

urlpatterns = [
    path('login/', authapp.LoginView.as_view(), name='login'),
    path('signin/', authapp.SignInView.as_view(), name='signin')
]