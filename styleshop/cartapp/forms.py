# from django import forms
# from cartapp.models import Delivery
# from shoppage.models import Product

# class DeliveryForm(forms.Form):

#     first_name = forms.CharField(max_length=20,
#         required=True, default=user.first_name)
#     last_name = forms.CharField(max_length=20,
#         required=True, default=user.last_name)
#     email = forms.EmailField(default=user.email)

#     def __init__(self, *args, **kwargs):

#         user = self.request.user
#         super(DeliveryForm, self).__init__(*args, **kwargs)

#     class Meta:

#         model = Delivery

#         fields = ('first_name', 'last_name', 'country', 'city', 'address', 
#             'email', 'terms_and_conitions')

#         widgets = {
#             'first_name': None,
#             'last_name': None,
#             'country': None,
#             'city': None,
#             'address': None,
#             'email': None,
#             'terms_and_conitions': None,
#         }

#         labels = {
#             'first_name': 'Имя',
#             'last_name': 'Фамилия',
#             'country': 'Страна',
#             'city': 'Город',
#             'address': 'Адрес',
#             'email': 'Электронная почта',
#             'terms_and_conitions': 'Условия политики конфиденциальности',
#         }


