# Generated by Django 2.1.2 on 2018-12-24 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0032_orderitem_toppings'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]