# Generated by Django 5.1.4 on 2024-12-23 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='buing',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name=' سعر الشراء'),
        ),
    ]