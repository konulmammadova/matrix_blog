# Generated by Django 2.0.7 on 2018-07-17 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrix_app', '0016_auto_20180717_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('sub_title', models.CharField(max_length=300)),
                ('bg_image', models.ImageField(default='about-bg.jpg', upload_to='')),
                ('content', models.TextField()),
            ],
        ),
    ]
