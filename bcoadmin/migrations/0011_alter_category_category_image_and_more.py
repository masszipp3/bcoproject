# Generated by Django 4.2.5 on 2023-10-15 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bcoadmin', '0010_alter_category_category_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_image',
            field=models.ImageField(blank=True, null=True, upload_to='category_image/'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='bcoadmin.category'),
        ),
    ]
