# Generated by Django 3.0.6 on 2020-11-15 15:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20201115_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tableimage',
            name='byl',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='tableimage',
            name='firsttime',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 15, 15, 22, 27, 483036, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tableimage',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 15, 15, 22, 27, 482993, tzinfo=utc)),
        ),
    ]