# Generated by Django 2.2.6 on 2019-11-27 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0014_auto_20191121_0315'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessprofile',
            name='business_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='businessprofile',
            name='fax',
            field=models.IntegerField(default=232123),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='businessprofile',
            name='office_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='businessprofile',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
    ]
