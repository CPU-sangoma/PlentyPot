# Generated by Django 2.2.6 on 2019-11-29 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Responses', '0005_auto_20191125_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='picture',
            field=models.ImageField(blank=True, default='empty.png', null=True, upload_to='reviewsmedia'),
        ),
    ]