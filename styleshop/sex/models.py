from django.db import models

class Sex(models.Model):

    name = models.CharField(max_length=10)
