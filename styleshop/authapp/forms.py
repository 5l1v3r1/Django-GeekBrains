from django import forms
from django.contrib.auth import authenticate
from authapp.models import ShopUser

class LoginForm(forms.Form):

    username = forms.CharField(max_length=20, required=True, label='Логин',
               widget=forms.widgets.TextInput(attrs={'class': 'input100'}))

    password = forms.CharField(max_length=20, required=True, label='Пароль',
               widget=forms.widgets.PasswordInput(attrs={'class': 'input100'}))

    def find_user_in_db(self):

        print('-'*100)
        print(self)

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        return authenticate(username=username, password=password)

    def clean(self, *args, **kwargs):

        self.user = self.find_user_in_db()

        if not self.user:
            raise forms.ValidationError('Неверный логин или пароль!')
        
        super(LoginForm, self).clean(*args, **kwargs)

class SignInForm(forms.ModelForm):

    password_confirm = forms.CharField(min_length=8, max_length=20, label='Подтвердите пароль', required=True,
                                       widget=forms.widgets.PasswordInput(attrs={'class': 'input100'}))

    class Meta:

        model = ShopUser

        fields = ['username', 'age', 'birth_date', 'email','password']

        widgets = {
            'username': forms.widgets.TextInput(attrs={'class': 'input100'}),
            'password': forms.widgets.PasswordInput(attrs={'class': 'input100'}),
            'age': forms.widgets.NumberInput(attrs={'class': 'input100'}),
            'birth_date': forms.widgets.DateInput(attrs={'class': 'input100'}),
            'email': forms.widgets.EmailInput(attrs={'class': 'input100'})
        }

        labels = {
            'username': 'Логин',
            'password': 'Пароль',
            'birth_date': 'Дата рождения (ГГГГ-ММ-ДД)',
            'email': 'Электронная почта'
        }

    def clean_password_confirm(self):

        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password != password_confirm:
            raise forms.ValidationError('Введенные пароли не совпадают')

        return self.cleaned_data

    def save(self, commit=True):

        password = self.cleaned_data.get('password')
        user = super(SignInForm, self).save(commit=False)
        user.set_password(password)

        if commit:
            user.save()

        return user
