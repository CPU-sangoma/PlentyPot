# Generated by Django 2.2.6 on 2019-12-05 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0023_auto_20191203_0029'),
        ('Clubsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagemodel',
            name='Banner',
            field=models.ImageField(null=True, upload_to='club/HomePage/', verbose_name='big banner image to be displayed on your home page'),
        ),
        migrations.AlterField(
            model_name='homepagemodel',
            name='ResDjs1',
            field=models.ImageField(null=True, upload_to='club/HomePage/', verbose_name='Resdjs1 pic'),
        ),
        migrations.AlterField(
            model_name='homepagemodel',
            name='ResDjs2',
            field=models.ImageField(null=True, upload_to='club/HomePage/', verbose_name='Resdjs2 pic'),
        ),
        migrations.AlterField(
            model_name='homepagemodel',
            name='ResDjs3',
            field=models.ImageField(null=True, upload_to='club/HomePage/', verbose_name='Resdjs3 pic'),
        ),
        migrations.AlterField(
            model_name='homepagemodel',
            name='ResDjs4',
            field=models.ImageField(null=True, upload_to='club/HomePage/', verbose_name='Resdjs4 pic'),
        ),
        migrations.AlterField(
            model_name='homepagemodel',
            name='company',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='clubhome', to='profiles.BusinessProfile'),
        ),
        migrations.AlterField(
            model_name='homepagemodel',
            name='fifGpic',
            field=models.ImageField(null=True, upload_to='club/HomePage/', verbose_name='5th gallery pic'),
        ),
        migrations.AlterField(
            model_name='homepagemodel',
            name='frthGpic',
            field=models.ImageField(null=True, upload_to='club/HomePage/', verbose_name='fourth gallery pic'),
        ),
        migrations.AlterField(
            model_name='homepagemodel',
            name='fstGpic',
            field=models.ImageField(null=True, upload_to='club/HomePage/', verbose_name='fst gallery pic'),
        ),
        migrations.AlterField(
            model_name='homepagemodel',
            name='secGpic',
            field=models.ImageField(null=True, upload_to='club/HomePage/', verbose_name='sec gallery pic'),
        ),
        migrations.AlterField(
            model_name='homepagemodel',
            name='sixthGpic',
            field=models.ImageField(null=True, upload_to='club/HomePage/', verbose_name='6th gallery pic'),
        ),
        migrations.AlterField(
            model_name='homepagemodel',
            name='svthGpic',
            field=models.ImageField(null=True, upload_to='club/HomePage/', verbose_name='svthGpic gallery pic'),
        ),
        migrations.AlterField(
            model_name='homepagemodel',
            name='trdGpic',
            field=models.ImageField(null=True, upload_to='club/HomePage/', verbose_name='third gallery pic'),
        ),
        migrations.CreateModel(
            name='TonightModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Currentpic1', models.ImageField(blank=True, null=True, upload_to='club/TonightPage', verbose_name='show visitors whats happening now')),
                ('Currentpic2', models.ImageField(blank=True, null=True, upload_to='club/TonightPage', verbose_name='show visitors whats happening now')),
                ('Currentpic3', models.ImageField(blank=True, null=True, upload_to='club/TonightPage', verbose_name='show visitors whats happening now')),
                ('Currentpic4', models.ImageField(blank=True, null=True, upload_to='club/TonightPage', verbose_name='show visitors whats happening now')),
                ('Specials', models.TextField()),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='clubTonight', to='profiles.BusinessProfile')),
            ],
        ),
        migrations.CreateModel(
            name='EventsPageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MainEventpic', models.ImageField(null=True, upload_to='club/EventsPage')),
                ('name_of_main_event', models.TextField(verbose_name='name of main event')),
                ('upcomming_event1', models.ImageField(upload_to='club/EventsPage', verbose_name='upcoming event 1')),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='clubEvents', to='profiles.BusinessProfile')),
            ],
        ),
    ]
