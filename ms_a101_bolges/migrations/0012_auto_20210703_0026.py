# Generated by Django 3.1.6 on 2021-07-02 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('msdepot', '0001_initial'),
        ('ms_a101_bolges', '0011_depotorder_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depotorder',
            name='fruit_vegetable_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='msdepot.meyvesebzeyeni'),
        ),
    ]
