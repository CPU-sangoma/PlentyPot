# Generated by Django 2.2.6 on 2019-11-12 22:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0003_auto_20191112_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessprofile',
            name='Complete',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='businessprofile',
            name='latitude',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='businessprofile',
            name='longitude',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='business_name',
            field=models.CharField(default='businessName', max_length=100),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='logo',
            field=models.ImageField(default='business.jpg', upload_to='static/businesslogos'),
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilepic', models.ImageField(default='customer.jpg', upload_to='static/CustomerPic')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
