from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from . import forms
from shoppage import models as sp
from mainpage import models as mp
from authapp import models as aa
from authapp.mixins import StaffRequired

class Table(StaffRequired, ListView):

    template_name = 'adminapp/admin.html'
    context_object_name = 'query'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['menu'] = [
            {'name': 'Товары', 'link': 'product'},
            {'name': 'Брэнды', 'link': 'brand'},
            {'name': 'Секции', 'link': 'section'},
            {'name': 'Категории', 'link': 'category'},
            {'name': 'Пользователи', 'link': 'user'},
        ]

        return context

class Create(StaffRequired, CreateView):
    
    template_name = 'adminapp/form.html'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание объекта'
        context['button_txt'] = 'Создать'

        return context

class Update(StaffRequired, UpdateView):
    
    template_name = 'adminapp/form.html'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изменение объекта'
        context['button_txt'] = 'Изменить'

        return context

class Delete(StaffRequired, DeleteView):
    
    template_name = 'adminapp/delete.html'
    context_object_name = 'query'
    del_word = None
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['text'] = 'Вы действительно хотите удалить объект?'
        context['title'] = 'Удаление объекта'
        context['button_txt'] = 'Удалить'
        if self.del_word:
            context['attention'] = 'Удаление {} повлечет удаление всех связанных товаров'.format(self.del_word)

        return context

class MainView(StaffRequired, View):

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
class Product:
    model = sp.Product

class TableProduct(Product, Table):

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['new_name'] = 'товар'
        context['title'] = 'Товары'
        context['table_fields'] = ['Название', 'Категория', 'Брэнд', 'Цена', 'Скидка', 'Удаление']

        return context

class CreateProduct(Product, Create):

    form_class = forms.ProductForm
    success_url = '/ssadmin/product'

class UpdateProduct(Product, Update):
   
    form_class = forms.ProductForm
    success_url = '/ssadmin/product'

class DeleteProduct(Product, Delete):
   
    success_url = '/ssadmin/product'

#------------ Контроллеры категорий ------------#
class Category:
    model = mp.Category

class TableCategory(Category, Table):
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['new_name'] = 'категорию'
        context['title'] = 'Категории'
        context['table_fields'] = ['Название', 'Секция', 'Пол', 'Удаление']

        return context

class CreateCategory(Category, Create):
    
    form_class = forms.CategoryForm
    success_url = '/ssadmin/category'

class UpdateCategory(Category, Update):
    
    form_class = forms.CategoryForm
    success_url = '/ssadmin/category'

class DeleteCategory(Category, Delete):
    
    success_url = '/ssadmin/category'
    del_word = 'категории'

#------------ Контроллеры пола ------------#
class TableSex(Table):
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['title'] = 'Пол'
        context['table_fields'] = ['Название']

        return context

#------------ Контроллеры секций ------------#
class Section:
    model = mp.Section

class TableSection(Section, Table):
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['new_name'] = 'секцию'
        context['title'] = 'Секции'
        context['table_fields'] = ['Название', 'Логотип', 'Удаление']

        return context

class CreateSection(Section, Create):
    
    form_class = forms.SectionForm
    success_url = '/ssadmin/section'

class UpdateSection(Section, Update):
    
    form_class = forms.SectionForm
    success_url = '/ssadmin/section'

class DeleteSection(Section, Delete):
    
    success_url = '/ssadmin/section'
    del_word = 'секции'

#------------ Контроллеры брэндов ------------#
class Brand:
    model = mp.Brand

class TableBrand(Brand, Table):
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['new_name'] = 'брэнд'
        context['title'] = 'Брэнды'
        context['table_fields'] = ['Название', 'Логотип', 'Удаление']

        return context

class CreateBrand(Brand, Create):
    
    form_class = forms.BrandForm
    success_url = '/ssadmin/brand'

class UpdateBrand(Brand, Update):
    
    form_class = forms.BrandForm
    success_url = '/ssadmin/brand'

class DeleteBrand(Brand, Delete):
    
    success_url = '/ssadmin/brand'
    del_word = 'брэнда'

#------------ Контроллеры пользователей ------------#
class User:
    model = aa.ShopUser

class TableUser(User, Table):
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['title'] = 'Пользователи'
        context['table_fields'] = ['Имя', 'Возраст', 'Почта', 'День рождения', 'Время регистрации']

        return context
