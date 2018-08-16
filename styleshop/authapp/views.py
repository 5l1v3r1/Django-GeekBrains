from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import login, logout
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms, mixins

class LoginView(mixins.AnonRequired, FormView):

    template_name = 'authapp/login.html'
    success_url = '/'
    form_class = forms.LoginForm

    def post(self, request):

        form = self.form_class(request.POST)

        if form.is_valid():
            
            login(request, form.user)

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        return render(request, self.template_name, {'form': form})

class LogoutView(LoginRequiredMixin, TemplateView):

    template_name='authapp/logout.html'
    success_url='/'
    main_url='/'

    def post(self, request):

        logout(request)

        return redirect(self.success_url)

class SignInView(mixins.AnonRequired, FormView):

    template_name = 'authapp/signin.html'
    form_class = forms.SignInForm
    success_url = '/'

    def post(self, request):

        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save()
            login(request, user)

            return redirect(self.success_url)

        return render(request, self.template_name, {'form': form})
