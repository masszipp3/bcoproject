# Generated by Django 4.2.5 on 2023-10-15 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bcoadmin', '0009_remove_products_vendor_products_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_code',
            field=models.CharField(db_index=True, max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_code',
            field=models.CharField(db_index=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_code',
            field=models.CharField(db_index=True, max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category_code',
            field=models.CharField(db_index=True, max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='suppliers',
            name='supplier_code',
            field=models.CharField(db_index=True, max_length=250, unique=True),
        ),
    ]
