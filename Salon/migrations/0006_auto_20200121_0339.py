# Generated by Django 2.2.6 on 2020-01-21 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Salon', '0005_auto_20200121_0017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actualsalonmodel',
            old_name='style1des',
            new_name='styledes',
        ),
        migrations.RenameField(
            model_name='actualsalonmodel',
            old_name='style1pic',
            new_name='stylepic',
        ),
    ]
