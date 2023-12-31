# Generated by Django 4.2.5 on 2023-10-10 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bcoadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='quantity',
            field=models.DecimalField(decimal_places=3, default=1.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='products',
            name='unit_type',
            field=models.CharField(blank=True, choices=[('kg', 'Kilogram'), ('nos', 'Number'), ('litre', 'Litre')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='suppliers',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
