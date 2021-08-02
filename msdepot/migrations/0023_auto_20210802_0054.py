# Generated by Django 3.1.6 on 2021-08-01 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('msdepot', '0022_auto_20210802_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ihaleyeni',
            name='fruit_vegetable_kod',
            field=models.ForeignKey(db_column='fruit_vegetable_kod_yeni', on_delete=django.db.models.deletion.CASCADE, related_name='fruit_vegetable_kod', to='msdepot.meyvesebzeyeni'),
        ),
        migrations.AlterField(
            model_name='ihaleyeni',
            name='fruit_vegetable_name',
            field=models.ForeignKey(db_column='fruit_vegetable_name_yeni', on_delete=django.db.models.deletion.CASCADE, related_name='fruit_vegetable_name', to='msdepot.meyvesebzeyeni'),
        ),
    ]