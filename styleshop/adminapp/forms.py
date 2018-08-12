from django import forms
from shoppage.models import Product
from mainpage.models import Sex, Brand, Section, Category

class ProductForm(forms.ModelForm):

    class Meta:

        model = Product

        fields = ['name', 'category', 'brand', 'sex', 'cost', 'sale', 'images', 'description']

        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'input100'}),
            'category': forms.widgets.Select(attrs={'class': 'input100', 'style': 'padding-left: 5px'}), 
            'brand': forms.widgets.Select(attrs={'class': 'input100', 'style': 'padding-left: 5px'}),
            'sex': forms.widgets.Select(attrs={'class': 'input100', 'style': 'padding-left: 5px'}),
            'cost': forms.widgets.NumberInput(attrs={'class': 'input100'}),
            'sale': forms.widgets.NumberInput(attrs={'class': 'input100'}),
            'images': forms.widgets.ClearableFileInput(),
            'description': forms.widgets.Textarea(attrs={'class': 'input100'})
        }

        labels = {
            'name': 'Название',
            'category': 'Категория', 
            'brand': 'Брэнд',
            'sex': 'Пол',
            'cost': 'Цена',
            'sale': 'Размер скидки',
            'images': 'Фотография',
            'description': 'О товаре'
        }

class BrandForm(forms.ModelForm):

    class Meta:

        model = Brand

        fields = ['name', 'image']

        labels = {
            'name': 'Название', 
            'image':'Логотип'
        }

        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'input100'}),
            'image': forms.widgets.ClearableFileInput()
        }

# class SexForm(forms.ModelForm):

#     class Meta:

#         model = Sex

#         fields = ['name']

#         labels = {
#             'name': 'Название', 
#         }

#         widgets = {
#             'name': forms.widgets.TextInput(attrs={'class': 'input100'}),
#         }

class SectionForm(forms.ModelForm):

    class Meta:

        model = Section

        fields = ['name']

        labels = {
            'name': 'Название', 
        }

        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'input100'}),
        }

class CategoryForm(forms.ModelForm):

    class Meta:

        model = Category

        fields = ['name', 'section', 'sex']

        labels = {
            'name': 'Название', 
            'section': 'Секция', 
            'sex': 'Пол'
        }

        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'input100'}),
            'section': forms.widgets.Select(attrs={'class': 'input100', 'style': 'padding-left: 5px'}),
            'sex': forms.widgets.Select(attrs={'class': 'input100', 'style': 'padding-left: 5px'}),
        }
