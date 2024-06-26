# Generated by Django 4.2 on 2023-06-18 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Product'},
        ),
        migrations.AlterField(
            model_name='product',
            name='price_real',
            field=models.DecimalField(decimal_places=0, editable=False, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='total_sold',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
