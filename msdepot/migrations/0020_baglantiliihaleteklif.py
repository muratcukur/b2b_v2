# Generated by Django 3.1.6 on 2021-07-12 21:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('msdepot', '0019_auto_20210712_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaglantiliIhaleTeklif',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ihale_teklif_date', models.DateTimeField(auto_now_add=True)),
                ('month', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('planlanan_hedef_tonaj', models.FloatField(blank=True, default=None, null=True)),
                ('baglantiliihaleid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='msdepot.baglantiliurunihalesi')),
                ('tedarikci', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
