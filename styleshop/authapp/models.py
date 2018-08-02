from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

class ShopUser(AbstractUser):

    age = models.PositiveIntegerField(verbose_name='Возраст',
                                      validators=[
        MaxValueValidator(99, 'Вы слишком стары'),
        MinValueValidator(18, 'Вы слишком молоды')
    ])
    birth_date = models.DateField(verbose_name='Дата рождения')
