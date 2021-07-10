# Generated by Django 2.2.6 on 2019-12-07 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LiquorStore', '0004_auto_20191207_2339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='liquorhomepagemodel',
            name='beer6des',
        ),
        migrations.RemoveField(
            model_name='liquorhomepagemodel',
            name='bottledes',
        ),
        migrations.AddField(
            model_name='liquorhomepagemodel',
            name='beer5des',
            field=models.TextField(null=True, verbose_name='price description for fifth beers/ciders pic'),
        ),
        migrations.AddField(
            model_name='liquorhomepagemodel',
            name='bottle4des',
            field=models.TextField(null=True, verbose_name='price description for forth Liquor/Spirits pic'),
        ),
        migrations.AddField(
            model_name='liquorhomepagemodel',
            name='wine6des',
            field=models.TextField(null=True, verbose_name='price description for sixth wines/champagne pic'),
        ),
        migrations.AlterField(
            model_name='liquorhomepagemodel',
            name='beer1des',
            field=models.TextField(null=True, verbose_name='price description for first beers/ciders pic'),
        ),
        migrations.AlterField(
            model_name='liquorhomepagemodel',
            name='beer2des',
            field=models.TextField(null=True, verbose_name='price description for second beers/ciders pic '),
        ),
        migrations.AlterField(
            model_name='liquorhomepagemodel',
            name='beer3des',
            field=models.TextField(null=True, verbose_name='price description for third beers/ciders pic '),
        ),
        migrations.AlterField(
            model_name='liquorhomepagemodel',
            name='beer4des',
            field=models.TextField(null=True, verbose_name='price description for forth beers/ciders pic '),
        ),
        migrations.AlterField(
            model_name='liquorhomepagemodel',
            name='bottle2des',
            field=models.TextField(null=True, verbose_name='price description for second Liquor/Spirits pic'),
        ),
        migrations.AlterField(
            model_name='liquorhomepagemodel',
            name='wine2des',
            field=models.TextField(null=True, verbose_name='price description for sec wines/champagne pic'),
        ),
    ]
