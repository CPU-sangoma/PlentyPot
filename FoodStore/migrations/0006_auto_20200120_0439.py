# Generated by Django 2.2.6 on 2020-01-20 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FoodStore', '0005_auto_20200120_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actualmenumodel',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actualmenudata', to='profiles.BusinessProfile'),
        ),
    ]