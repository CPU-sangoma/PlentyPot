# Generated by Django 2.2.6 on 2019-12-05 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_auto_20191203_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='cususer',
            name='TypeOfBus',
            field=models.CharField(default='Guest House', max_length=100, null=True, verbose_name='Type of Buisness'),
        ),
    ]
