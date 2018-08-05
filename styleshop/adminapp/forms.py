from django import forms
from shoppage.models import Product

class ProductForm(forms.ModelForm):

    class Meta:

        model = Product

        fields = ['name', 'category', 'brand', 'sex', 'cost', 'sale', 'images', 'description']

        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'input100'}),
            'category': forms.widgets.Select(attrs={'class': 'input100'}), 
            'brand': forms.widgets.Select(attrs={'class': 'input100'}),
            'sex': forms.widgets.Select(attrs={'class': 'input100'}),
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
