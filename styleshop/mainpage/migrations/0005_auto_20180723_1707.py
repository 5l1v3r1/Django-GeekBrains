# Generated by Django 2.0.7 on 2018-07-23 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_auto_20180723_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='sex',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
