# Generated by Django 2.2.6 on 2019-12-13 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0026_auto_20191208_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessprofile',
            name='type_of_business',
            field=models.CharField(choices=[('Club', 'Club/Pub'), ('Cosmetics', 'Cosmetics'), ('Food', 'Food'), ('LiquorStore', 'liquor store'), ('Salon', 'Salon')], max_length=200, null=True),
        ),
    ]
