# Generated by Django 2.2.6 on 2019-12-01 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_auto_20191127_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessprofile',
            name='fax',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]