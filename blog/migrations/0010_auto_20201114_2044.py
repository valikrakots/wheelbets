# Generated by Django 3.0.6 on 2020-11-14 17:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20201114_1931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tableimage',
            name='recom',
        ),
        migrations.AddField(
            model_name='table',
            name='str',
            field=models.TextField(default='e', max_length=10000000000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tableimage',
            name='firsttime',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 14, 17, 44, 31, 348511, tzinfo=utc)),
        ),
    ]