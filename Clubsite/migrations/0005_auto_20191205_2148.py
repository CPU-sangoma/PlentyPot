# Generated by Django 2.2.6 on 2019-12-05 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Clubsite', '0004_auto_20191205_1557'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepagemodel',
            old_name='status',
            new_name='status_hp',
        ),
        migrations.RemoveField(
            model_name='homepagemodel',
            name='status_tp',
        ),
    ]
