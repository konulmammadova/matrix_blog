# Generated by Django 2.0.7 on 2018-08-11 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrix_app', '0033_auto_20180811_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='token',
            name='name',
            field=models.CharField(default='o7cBV1oN24p6XM9r3NP7', max_length=20),
        ),
    ]