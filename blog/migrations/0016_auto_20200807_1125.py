# Generated by Django 3.0.6 on 2020-08-07 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_table_success'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='success',
            field=models.CharField(max_length=100),
        ),
    ]
