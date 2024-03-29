# Generated by Django 2.2.6 on 2019-12-13 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0027_auto_20191213_2336'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalonPricesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style1pic', models.ImageField(null=True, upload_to='Salon/Prices', verbose_name='upload 1st pic of the styles you are offering')),
                ('style1des', models.TextField(verbose_name='full details of the first style you are offering, include the price and variations')),
                ('style2pic', models.ImageField(null=True, upload_to='Salon/Prices', verbose_name='upload 2nd pic of the styles you are offering')),
                ('style2des', models.TextField(verbose_name='full details of the 2nd style you are offering, include the price and variations')),
                ('style3pic', models.ImageField(null=True, upload_to='Salon/Prices', verbose_name='upload 3rd pic of the styles you are offering')),
                ('style3des', models.TextField(verbose_name='full details of the 3rd style you are offering, include the price and variations')),
                ('style4pic', models.ImageField(null=True, upload_to='Salon/Prices', verbose_name='upload 4th pic of the styles you are offering')),
                ('style4des', models.TextField(verbose_name='full details of the 4th style you are offering, include the price and variations')),
                ('style5pic', models.ImageField(null=True, upload_to='Salon/Prices', verbose_name='upload 5th pic of the styles you are offering')),
                ('style5des', models.TextField(verbose_name='full details of the 5th style you are offering, include the price and variations')),
                ('style6pic', models.ImageField(null=True, upload_to='Salon/Prices', verbose_name='upload 6th pic of the styles you are offering')),
                ('style6des', models.TextField(verbose_name='full details of the 6th style you are offering, include the price and variations')),
                ('style7pic', models.ImageField(null=True, upload_to='Salon/Prices', verbose_name='upload 7th pic of the styles you are offering')),
                ('style7des', models.TextField(verbose_name='full details of the 7th style you are offering, include the price and variations')),
                ('style8pic', models.ImageField(null=True, upload_to='Salon/Prices', verbose_name='upload 8th pic of the styles you are offering')),
                ('style8des', models.TextField(verbose_name='full details of the 8th style you are offering, include the price and variations')),
                ('style9pic', models.ImageField(null=True, upload_to='Salon/Prices', verbose_name='upload 9th pic of the styles you are offering')),
                ('style9des', models.TextField(verbose_name='full details of the 9th style you are offering, include the price and variations')),
            ],
        ),
        migrations.CreateModel(
            name='SalonHomeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BannerImage', models.ImageField(null=True, upload_to='Salon/Home', verbose_name='upload an attractive banner image to impress visitors')),
                ('image1', models.ImageField(null=True, upload_to='Salon/Home', verbose_name='upload an image to add style and a personal touch to your home page')),
                ('image2', models.ImageField(null=True, upload_to='Salon/Home', verbose_name='upload an attractive banner image to impress visitors')),
                ('image3', models.ImageField(null=True, upload_to='Salon/Home', verbose_name='upload an attractive banner image to impress visitors')),
                ('example1', models.ImageField(null=True, upload_to='Salon/Home', verbose_name='upload an example of your best work')),
                ('example2', models.ImageField(null=True, upload_to='Salon/Home', verbose_name='upload an example of your best work')),
                ('example3', models.ImageField(null=True, upload_to='Salon/Home', verbose_name='upload an example of your best work')),
                ('example4', models.ImageField(null=True, upload_to='Salon/Home', verbose_name='upload an example of your best work')),
                ('example5', models.ImageField(null=True, upload_to='Salon/Home', verbose_name='upload an example of your best work')),
                ('team1pic', models.ImageField(null=True, upload_to='Salon/Home', verbose_name='upload a picture of the first team member')),
                ('team1Name', models.CharField(max_length=100, verbose_name=' the name of the first team member')),
                ('team1des', models.TextField(verbose_name="tell your visitors more about the first team member's speciality include contact info ")),
                ('team2pic', models.ImageField(null=True, upload_to='Salon/Home', verbose_name='upload a picture of the second team member')),
                ('team2Name', models.CharField(max_length=100, verbose_name=' the name of the second team member')),
                ('team2des', models.TextField(verbose_name="tell your visitors more about the first team member's speciality include contact info ")),
                ('team3pic', models.ImageField(null=True, upload_to='Salon/Home', verbose_name='upload a picture of the third team member')),
                ('team3Name', models.CharField(max_length=100, verbose_name=' the name of the third team member')),
                ('team3des', models.TextField(verbose_name="tell your visitors more about the third team member's speciality include contact info ")),
                ('team4pic', models.ImageField(null=True, upload_to='Salon/Home', verbose_name='upload a picture of the fourth team member')),
                ('team4Name', models.CharField(max_length=100, verbose_name=' the name of the fourth team member')),
                ('team4des', models.TextField(verbose_name="tell your visitors more about the fourth team member's speciality include contact info ")),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='salonhome', to='profiles.BusinessProfile')),
            ],
        ),
    ]
