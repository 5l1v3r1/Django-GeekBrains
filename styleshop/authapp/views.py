from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import FormView
from . import forms

class LoginView(FormView):

    template_name = 'authapp/login.html'
    success_url = '/'
    form_class = forms.LoginForm

    def post(self, request):

        form = self.form_class(request.POST)

        if form.is_valid():
            
            login(request, form.user)

            return  redirect(self.success_url)
        
        return render(request, self.template_name, {'form': form})

class SignInView(FormView):

    template_name = 'authapp/signin.html'
    form_class = forms.SignInForm
    success_url = '/'
