# Generated by Django 2.0.7 on 2018-07-17 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrix_app', '0019_auto_20180717_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=250, verbose_name='Mesaj'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Ad'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=10, verbose_name='Telefon'),
        ),
    ]
