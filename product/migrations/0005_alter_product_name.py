# Generated by Django 5.1.4 on 2025-01-31 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_product_image_product_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='product', max_length=200),
        ),
    ]
