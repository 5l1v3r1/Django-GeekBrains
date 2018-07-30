from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator

class ShopUser(AbstractUser):

    name = models.CharField(max_length=20, verbose_name='Имя')
    surname = models.CharField(max_length=20, verbose_name='Фамилия')
    age = models.PositiveIntegerField(validators=[MaxValueValidator(100)],
                                      verbose_name='Возраст')
    birth_date = models.DateField(auto_now=False, auto_now_add=False, 
                                  verbose_name='Дата рождения')
    avatar = models.ImageField(upload_to='avatars/', blank=True)
