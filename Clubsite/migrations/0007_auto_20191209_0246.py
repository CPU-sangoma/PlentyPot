# Generated by Django 2.2.6 on 2019-12-09 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Clubsite', '0006_auto_20191207_0352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventspagemodel',
            old_name='status_ep',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='homepagemodel',
            old_name='status_hp',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='tonightmodel',
            old_name='status_tp',
            new_name='status',
        ),
    ]
