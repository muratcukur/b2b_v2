# Generated by Django 3.1.6 on 2021-08-01 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msdepot', '0023_auto_20210802_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ihaleyeni',
            name='fruit_vegetable_kod',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='ihaleyeni',
            name='fruit_vegetable_name',
            field=models.CharField(max_length=30),
        ),
    ]