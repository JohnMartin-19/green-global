# Generated by Django 5.0.2 on 2024-02-20 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
        ('products', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product_id',
        ),
        migrations.AddField(
            model_name='order',
            name='product_id',
            field=models.ManyToManyField(blank=True, null=True, to='products.product'),
        ),
    ]