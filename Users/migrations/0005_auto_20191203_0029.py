# Generated by Django 2.2.6 on 2019-12-02 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_auto_20191125_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cususer',
            name='userpic',
            field=models.ImageField(default='userpics/userpro.png', upload_to='userpics'),
        ),
    ]
