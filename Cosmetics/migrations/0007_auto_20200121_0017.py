# Generated by Django 2.2.6 on 2020-01-20 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cosmetics', '0006_auto_20200120_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actualcoswork',
            name='Workpic',
            field=models.ImageField(blank=True, null=True, upload_to='Cosmetics/Workpage', verbose_name='Upload the picture of the first item on your menu'),
        ),
    ]
