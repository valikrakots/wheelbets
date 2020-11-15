# Generated by Django 3.0.6 on 2020-11-15 13:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20201115_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='tableimage',
            name='byl',
            field=models.CharField(default='no', max_length=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tableimage',
            name='firsttime',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 15, 13, 36, 35, 82152, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tableimage',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 15, 13, 36, 35, 82108, tzinfo=utc)),
        ),
    ]