# Generated by Django 5.0.6 on 2025-02-15 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_alter_bookingvo_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingvo',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='bookingvo',
            name='start_date',
            field=models.DateField(),
        ),
    ]
