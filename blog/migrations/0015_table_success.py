# Generated by Django 3.0.6 on 2020-08-07 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_remove_table_success'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='success',
            field=models.CharField(default='n', max_length=1),
            preserve_default=False,
        ),
    ]
