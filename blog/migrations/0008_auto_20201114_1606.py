# Generated by Django 3.0.6 on 2020-11-14 13:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20201114_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tableimage',
            name='photo',
        ),
        migrations.AlterField(
            model_name='tableimage',
            name='firsttime',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 14, 13, 6, 42, 790547, tzinfo=utc)),
        ),
    ]
