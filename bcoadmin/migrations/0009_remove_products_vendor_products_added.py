# Generated by Django 4.2.5 on 2023-10-13 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bcoadmin', '0008_products_product_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='vendor',
        ),
        migrations.AddField(
            model_name='products',
            name='Added',
            field=models.CharField(default='Admin', max_length=250),
        ),
    ]