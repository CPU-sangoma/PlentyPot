# Generated by Django 2.2.6 on 2019-11-21 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_auto_20191121_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='profilepic',
            field=models.ImageField(default='CustomerPics/customer.jpg', upload_to='CustomerPics'),
        ),
    ]
