
from django.db import models

class Section(models.Model):

    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='sections/')

    def __str__(self):
        return self.name

class Brand(models.Model):

    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='brands/')

    def __str__(self):
        return self.name

class Sex(models.Model):

    name = models.CharField(max_length=10)
    hidden = models.BooleanField()

    def __str__(self):
        return self.name

class Category(models.Model):

    name = models.CharField(max_length=20)
    sex = models.ForeignKey('mainpage.Sex', on_delete=models.CASCADE)
    section = models.ForeignKey('mainpage.Section', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
