# Generated by Django 2.0.7 on 2018-08-11 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrix_app', '0036_auto_20180811_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='name',
            field=models.CharField(default='dWmgeTHHdXmk9PJRaDN1', max_length=20),
        ),
    ]