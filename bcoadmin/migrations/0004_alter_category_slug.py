# Generated by Django 4.2.5 on 2023-10-12 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bcoadmin', '0003_products_min_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
