# Generated by Django 2.2.6 on 2019-12-07 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0024_auto_20191205_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiquorSalesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale1', models.ImageField(null=True, upload_to='LiquorStore/LiquorSale/', verbose_name='1st sale item')),
                ('sale2', models.ImageField(null=True, upload_to='LiquorStore/LiquorSale/', verbose_name='2nd sale item')),
                ('sale3', models.ImageField(null=True, upload_to='LiquorStore/LiquorSale/', verbose_name='3rd sale item')),
                ('sale4', models.ImageField(null=True, upload_to='LiquorStore/LiquorSale/', verbose_name='4th sale item')),
                ('sale5', models.ImageField(null=True, upload_to='LiquorStore/LiquorSale/', verbose_name='5th sale item')),
                ('sale6', models.ImageField(null=True, upload_to='LiquorStore/LiquorSale/', verbose_name='6th sale item')),
                ('sale7', models.ImageField(null=True, upload_to='LiquorStore/LiquorSale/', verbose_name='7th sale item')),
                ('sale8', models.ImageField(null=True, upload_to='LiquorStore/LiquorSale/', verbose_name='8th sale item')),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profiles.BusinessProfile')),
            ],
        ),
        migrations.CreateModel(
            name='LiquorHomePageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bannerImage', models.ImageField(null=True, upload_to='LiquorStore/LiquorHome/', verbose_name='upload a big banner Image for your Home Page')),
                ('beer1', models.ImageField(null=True, upload_to='LiquorStore/LiquorHome/', verbose_name='first pic under beers and cider')),
                ('beer2', models.ImageField(null=True, upload_to='LiquorStore/LiquorHome/', verbose_name='second pic under beers and cider')),
                ('beer3', models.ImageField(null=True, upload_to='LiquorStore/LiquorHome/', verbose_name='third pic under beers and cider')),
                ('beer4', models.ImageField(null=True, upload_to='LiquorStore/LiquorHome/', verbose_name='fourth pic under beers and cider')),
                ('beer5', models.ImageField(null=True, upload_to='LiquorStore/LiquorHome/', verbose_name='fifth pic under beers and cider')),
                ('beer7', models.ImageField(null=True, upload_to='LiquorStore/LiquorHome/', verbose_name='7th pic under beers and cider')),
                ('beer8', models.ImageField(null=True, upload_to='LiquorStore/LiquorHome/', verbose_name='8th pic under beers and cider')),
                ('bottle1', models.ImageField(null=True, upload_to='LiquorStore/LiquorHome/', verbose_name='first pic under spirits and Vodkas')),
                ('bottle2', models.ImageField(null=True, upload_to='LiquorStore/LiquorHome/', verbose_name='second pic under spirits and Vodkas')),
                ('bottle3', models.ImageField(null=True, upload_to='LiquorStore/LiquorHome/', verbose_name='third pic under spirits and Vodkas')),
                ('bottle4', models.ImageField(null=True, upload_to='LiquorStore/LiquorHome/', verbose_name='fourth pic under spirits and Vodkas')),
                ('bottle5', models.ImageField(null=True, upload_to='LiquorStore/LiquorHome/', verbose_name='first pic under spirits and Vodkas')),
                ('bottle6', models.ImageField(null=True, upload_to='LiquorStore/LiquorHome/', verbose_name='sixth pic under spirits and Vodkas')),
                ('bottle7', models.ImageField(null=True, upload_to='LiquorStore/LiquorHome/', verbose_name='7th pic under spirits and Vodkas')),
                ('bottle8', models.ImageField(null=True, upload_to='LiquorStore/LiquorHome/', verbose_name='8th pic under spirits and Vodkas')),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='liquorhome', to='profiles.BusinessProfile')),
            ],
        ),
    ]
