# Generated by Django 2.2.6 on 2019-11-29 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Responses', '0006_auto_20191129_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='picture',
            field=models.ImageField(blank=True, default='empty.jpg', null=True, upload_to='reviewsmedia'),
        ),
    ]