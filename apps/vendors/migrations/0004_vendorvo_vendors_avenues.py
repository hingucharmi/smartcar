# Generated by Django 5.0.6 on 2025-02-14 12:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avenues', '0001_initial'),
        ('vendors', '0003_alter_vendorvo_vendors_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendorvo',
            name='vendors_avenues',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='avenues.avenuesvo'),
        ),
    ]
