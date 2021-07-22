# Generated by Django 3.1.6 on 2021-07-04 12:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('msdepot', '0013_ihaleikincitur_ihale_end_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='IhaleIkinciTurTeklif',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ihale_teklif_date', models.DateTimeField(auto_now_add=True)),
                ('fiyat', models.FloatField()),
                ('ihale_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='msdepot.ihaleyeni')),
                ('tedarikci', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
