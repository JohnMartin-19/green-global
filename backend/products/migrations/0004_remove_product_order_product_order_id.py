# Generated by Django 5.0.2 on 2024-02-20 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_product_id'),
        ('products', '0003_product_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='order',
        ),
        migrations.AddField(
            model_name='product',
            name='order_id',
            field=models.ManyToManyField(to='orders.order'),
        ),
    ]