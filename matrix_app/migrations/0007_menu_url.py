# Generated by Django 2.0.7 on 2018-07-11 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrix_app', '0006_auto_20180711_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
