# Generated by Django 2.0.7 on 2018-07-11 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matrix_app', '0011_auto_20180711_1331'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SocialLink',
            new_name='SocialMedia',
        ),
        migrations.AlterModelOptions(
            name='socialmedia',
            options={'verbose_name': 'Sosial sebeke', 'verbose_name_plural': 'Sosial Sebekeler'},
        ),
    ]