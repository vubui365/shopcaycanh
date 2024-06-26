# Generated by Django 4.2 on 2023-06-18 19:40

from django.db import migrations, models
import django.utils.timezone
import shop.custom_field


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_options_alter_product_price_real_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('message', models.TextField()),
                ('contacted', shop.custom_field.CustomBooleanFieldContact()),
                ('message_admin', models.TextField(blank=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Contact',
            },
        ),
    ]
