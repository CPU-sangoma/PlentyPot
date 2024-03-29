# Generated by Django 2.2.6 on 2019-11-18 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_auto_20191116_0338'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessprofile',
            name='Product1',
            field=models.ImageField(default='product.jpg', upload_to='profileproducts'),
        ),
        migrations.AddField(
            model_name='businessprofile',
            name='Product2',
            field=models.ImageField(default='product.jpg', upload_to='profileproducts'),
        ),
        migrations.AddField(
            model_name='businessprofile',
            name='Product3',
            field=models.ImageField(default='product.jpg', upload_to='profileproducts'),
        ),
        migrations.AddField(
            model_name='businessprofile',
            name='Product4',
            field=models.ImageField(default='product.jpg', upload_to='profileproducts'),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='Complete',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='logo',
            field=models.ImageField(default='business.jpg', upload_to='businesslogos'),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='recommendations',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
