# Generated by Django 3.0.6 on 2020-06-19 13:34

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_table_change_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='change_date',
            field=models.DateTimeField(default=blog.models.one_day_hence),
        ),
        migrations.AlterField(
            model_name='table',
            name='date',
            field=models.DateTimeField(default=blog.models.one_minute_hence),
        ),
    ]