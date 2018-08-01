from django import forms
from django.contrib.auth import authenticate

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
