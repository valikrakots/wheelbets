# Generated by Django 3.0.6 on 2021-01-27 19:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20210127_2059'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='Imager',
        ),
        migrations.AlterField(
            model_name='tableimage',
            name='firsttime',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 27, 19, 8, 24, 222747, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tableimage',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 27, 19, 8, 24, 222720, tzinfo=utc)),
        ),
    ]