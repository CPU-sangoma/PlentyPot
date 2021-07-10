# Generated by Django 2.2.6 on 2019-12-05 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_cususer_typeofbus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cususer',
            name='TypeOfBus',
            field=models.CharField(choices=[('Guest House', 'Guest House'), ('Club', 'Club/Pub'), ('Cosmatics', 'Cosmatics'), ('Salon', 'Salon'), ('BarberShop', 'Barber Shop'), ('Food', 'Food'), ('Liquor Store', 'liquor store')], default='Guest House', max_length=100, null=True, verbose_name='Type of Buisness'),
        ),
    ]
