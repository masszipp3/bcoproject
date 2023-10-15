# Generated by Django 4.2.5 on 2023-10-12 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bcoadmin', '0004_alter_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.ImageField(blank=True, null=True, upload_to='category_image'),
        ),
        migrations.AddField(
            model_name='products',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='product_image'),
        ),
    ]