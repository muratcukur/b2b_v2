# Generated by Django 3.1.6 on 2021-07-01 08:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ms_a101_bolges', '0008_auto_20210701_1136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='depotorder',
            name='due_week',
        ),
        migrations.RemoveField(
            model_name='depotorder',
            name='unit',
        ),
        migrations.AddField(
            model_name='depotorder',
            name='teslim_tarihi',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
