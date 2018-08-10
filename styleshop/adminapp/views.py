from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, View
from . import forms
from shoppage.models import Product
from authapp.mixins import StaffRequired

class MainView(View):

    def get(self, request):

        return render(request, 'adminapp/admin.html', 
        {
            'menu': [
                {'name': 'Товары', 'link': 'product'},
                {'name': 'Брэнды', 'link': 'brand'},
                {'name': 'Секции', 'link': 'section'},
                {'name': 'Категории', 'link': 'category'},
                {'name': 'Пользователи', 'link': 'user'},
            ],
            'title': 'Главная',
            'page_text': 'Добро пожаловать в админ-панель магазина StyleShop. Для просмотра/добавления/редактирования/удаления объектов перейдите на их страницу по ссылке в меню или ниже.'
        })

#------------ Контроллеры товаров ------------#
class CreateProduct(StaffRequired, CreateView):

    model = Product
    form_class = forms.ProductForm
    success_url = '/shop'
    template_name = 'adminapp/form.html'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание товара'
        context['button_txt'] = 'Создать'

        return context

class UpdateProduct(StaffRequired, UpdateView):

    model = Product
    form_class = forms.ProductForm
    success_url = '/shop'
    template_name = 'adminapp/form.html'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изменение товара'
        context['button_txt'] = 'Изменить'

        return context

class DeleteProduct(StaffRequired, DeleteView):

    model = Product
    template_name = 'adminapp/delete.html'
    success_url = '/shop'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['text'] = 'Вы действительно хотите удалить товар?'
        context['title'] = 'Удаление товара'
        context['button_txt'] = 'Удалить'

        return context

#------------ Контроллеры категорий ------------#

#------------ Контроллеры пола ------------#

#------------ Контроллеры секций ------------#

#------------ Контроллеры брэндов ------------#

