# Generated by Django 3.0.6 on 2020-11-14 17:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20201114_2044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table',
            old_name='str',
            new_name='stre',
        ),
        migrations.AlterField(
            model_name='tableimage',
            name='firsttime',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 14, 17, 47, 20, 803732, tzinfo=utc)),
        ),
    ]
