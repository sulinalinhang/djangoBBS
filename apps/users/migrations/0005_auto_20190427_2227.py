# Generated by Django 2.2 on 2019-04-27 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190426_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='static/pic/tbxd.jpg', upload_to='image/%Y/%m'),
        ),
    ]
