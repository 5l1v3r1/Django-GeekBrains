# Generated by Django 2.0.7 on 2018-07-24 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='section',
        ),
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ImageField(upload_to='products'),
        ),
    ]
