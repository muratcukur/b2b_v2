# Generated by Django 3.1.6 on 2021-08-01 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ms_a101_bolges', '0013_auto_20210704_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localsupplierorder',
            name='destination_bolge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='localsupplierorder',
            name='price',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
