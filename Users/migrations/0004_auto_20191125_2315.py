# Generated by Django 2.2.6 on 2019-11-25 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_cususer_userpic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cususer',
            name='userpic',
            field=models.ImageField(default='userpics/userpro.jpg', upload_to='userpics'),
        ),
    ]
