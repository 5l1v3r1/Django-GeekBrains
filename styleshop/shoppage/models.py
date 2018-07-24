from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=20)
    section = models.ForeignKey('mainpage.Section', on_delete=models.CASCADE)
    category = models.ForeignKey('mainpage.Category', on_delete=models.CASCADE)
    sex = models.ForeignKey('mainpage.Sex', on_delete=models.CASCADE)
    images = models.ImageField(upload_to='product/{}'.format(name))

    def __str__(self):
        return ' - '.join([self.name, str(self.category)])
