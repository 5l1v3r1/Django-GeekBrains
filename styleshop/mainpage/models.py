
from django.db import models

class Section(models.Model):

    name = models.CharField(max_length=20)

    image = models.ImageField(upload_to='sections/')

    def __str__(self):
        return self.name
