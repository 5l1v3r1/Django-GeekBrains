from django.views.generic import CreateView, UpdateView, DeleteView
from . import forms
from shoppage.models import Product
from authapp.mixins import StaffRequired

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
