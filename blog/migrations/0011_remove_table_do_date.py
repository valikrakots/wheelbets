# Generated by Django 3.0.6 on 2020-07-17 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200717_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='do_date',
        ),
    ]
