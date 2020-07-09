# Generated by Django 3.0.7 on 2020-06-27 12:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(default=None, upload_to='posts')),
                ('txt', models.TextField(default=datetime.datetime(2020, 6, 27, 17, 34, 57, 828817))),
                ('my_date', models.DateTimeField(default=datetime.datetime(2020, 6, 28, 17, 34, 57, 828817))),
                ('img', models.ImageField(default=None, upload_to='photos')),
            ],
        ),
    ]