# Generated by Django 2.1.2 on 2018-12-08 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0026_auto_20181208_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='orders',
        ),
        migrations.AddField(
            model_name='address',
            name='orders',
            field=models.ManyToManyField(to='items.Order'),
        ),
    ]
