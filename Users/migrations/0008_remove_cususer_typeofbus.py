# Generated by Django 2.2.6 on 2019-12-05 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0007_auto_20191205_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cususer',
            name='TypeOfBus',
        ),
    ]
