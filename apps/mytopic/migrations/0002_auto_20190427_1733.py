# Generated by Django 2.2 on 2019-04-27 09:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytopic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='created_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='topic',
            name='created_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='创建时间'),
        ),
    ]
