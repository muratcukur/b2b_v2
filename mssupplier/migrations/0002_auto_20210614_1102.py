# Generated by Django 3.1.6 on 2021-06-14 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mssupplier', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplierstock',
            old_name='yearly_stock_capacity',
            new_name='yearly_sales_capacity',
        ),
    ]
