# Generated by Django 3.0.6 on 2020-11-14 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201113_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='cars')),
            ],
        ),
    ]
