# Generated by Django 2.0.7 on 2018-08-11 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrix_app', '0039_auto_20180811_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='name',
            field=models.CharField(default='UOsX6M3iSH4Pt1DDTZVg', max_length=20),
        ),
    ]