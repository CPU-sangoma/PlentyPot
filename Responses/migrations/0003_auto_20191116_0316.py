# Generated by Django 2.2.6 on 2019-11-16 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Responses', '0002_reviews_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='picture',
            field=models.ImageField(blank=True, default='empty', null=True, upload_to='static/reviewsmedia'),
        ),
    ]