# Generated by Django 3.1.6 on 2021-08-02 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msdepot', '0026_auto_20210802_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meyvesebzeyeni',
            name='fruit_vegetable_kod_yeni',
            field=models.IntegerField(default=12345),
            preserve_default=False,
        ),
    ]