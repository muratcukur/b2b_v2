# Generated by Django 3.1.6 on 2021-06-12 12:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ms_a101_bolges', '0002_delete_userprofile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DepotOrder',
            new_name='DepotOrders',
        ),
    ]
