# Generated by Django 2.1.2 on 2018-12-03 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0011_remove_order_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]