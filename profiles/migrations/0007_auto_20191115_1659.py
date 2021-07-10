# Generated by Django 2.2.6 on 2019-11-15 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20191113_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessprofile',
            name='latitude',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='longitude',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='type_of_business',
            field=models.CharField(choices=[('Guest House', 'Guest House'), ('Club', 'Club/Pub'), ('Cosmatics', 'Cosmatics'), ('Salon', 'Salon'), ('BarberShop', 'Barber Shop'), ('Food', 'Food'), ('Liquor Store', 'liquor store'), ('Pharmacy', 'Pharmacy'), ('Dentist', 'Dentist')], default='tob', max_length=200),
        ),
    ]
