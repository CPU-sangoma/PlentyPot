# Generated by Django 2.2.6 on 2020-01-21 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0027_auto_20191213_2336'),
        ('LiquorStore', '0007_auto_20191229_0057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='liquorsalesmodel',
            name='sale1',
        ),
        migrations.RemoveField(
            model_name='liquorsalesmodel',
            name='sale1des',
        ),
        migrations.RemoveField(
            model_name='liquorsalesmodel',
            name='sale2',
        ),
        migrations.RemoveField(
            model_name='liquorsalesmodel',
            name='sale2des',
        ),
        migrations.RemoveField(
            model_name='liquorsalesmodel',
            name='sale3',
        ),
        migrations.RemoveField(
            model_name='liquorsalesmodel',
            name='sale3des',
        ),
        migrations.RemoveField(
            model_name='liquorsalesmodel',
            name='sale4',
        ),
        migrations.RemoveField(
            model_name='liquorsalesmodel',
            name='sale4des',
        ),
        migrations.RemoveField(
            model_name='liquorsalesmodel',
            name='sale5',
        ),
        migrations.RemoveField(
            model_name='liquorsalesmodel',
            name='sale5des',
        ),
        migrations.RemoveField(
            model_name='liquorsalesmodel',
            name='sale6',
        ),
        migrations.RemoveField(
            model_name='liquorsalesmodel',
            name='sale6des',
        ),
        migrations.RemoveField(
            model_name='liquorsalesmodel',
            name='sale7',
        ),
        migrations.RemoveField(
            model_name='liquorsalesmodel',
            name='sale7des',
        ),
        migrations.RemoveField(
            model_name='liquorsalesmodel',
            name='sale8',
        ),
        migrations.RemoveField(
            model_name='liquorsalesmodel',
            name='sale8des',
        ),
        migrations.CreateModel(
            name='ActualLiqSales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salepic', models.ImageField(null=True, upload_to='LiquorStore/LiquorSale/', verbose_name='1st sale item')),
                ('saledes', models.TextField(null=True, verbose_name='sale description for item1')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ActualLiquor', to='profiles.BusinessProfile')),
            ],
        ),
    ]