# Generated by Django 5.0.3 on 2024-06-25 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
    ]
