# Generated by Django 5.1.6 on 2025-02-08 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visual', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Ваше имя')),
                ('email', models.EmailField(max_length=100, verbose_name='Ваша почта')),
                ('phone', models.CharField(max_length=60, verbose_name='Ваш номер')),
                ('message', models.TextField(verbose_name='Ваше сообщение')),
            ],
            options={
                'verbose_name': 'Форм',
                'verbose_name_plural': 'Форм',
            },
        ),
        migrations.AlterField(
            model_name='upimages',
            name='star1',
            field=models.ImageField(blank=True, default='none', null=True, upload_to='up_images/'),
        ),
        migrations.AlterField(
            model_name='upimages',
            name='star2',
            field=models.ImageField(blank=True, default='none', null=True, upload_to='up_images/'),
        ),
        migrations.AlterField(
            model_name='upimages',
            name='star3',
            field=models.ImageField(blank=True, default='none', null=True, upload_to='up_images/'),
        ),
        migrations.AlterField(
            model_name='upimages',
            name='star4',
            field=models.ImageField(blank=True, default='none', null=True, upload_to='up_images/'),
        ),
    ]
