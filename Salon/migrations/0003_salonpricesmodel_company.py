# Generated by Django 2.2.6 on 2019-12-13 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0027_auto_20191213_2336'),
        ('Salon', '0002_auto_20191213_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='salonpricesmodel',
            name='company',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salonprices', to='profiles.BusinessProfile'),
        ),
    ]
