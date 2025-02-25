# Generated by Django 5.1.5 on 2025-01-28 11:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    operations = [
        migrations.CreateModel(
            name='FloorsVO',
            fields=[
                ('floors_id', models.AutoField(db_column='floors_id', null=None, primary_key=True, serialize=False)),
                ('floors_name', models.CharField(db_column='floors_name', default='', max_length=25)),
                ('floors_plan', models.CharField(db_column='floors_plan', default='')),
                ('floors_slot_price', models.DecimalField(db_column='floors_slot_price', decimal_places=2, max_digits=20)),
                ('floors_avenues_id', models.ForeignKey(db_column='floors_avenues_id', on_delete=django.db.models.deletion.CASCADE, to='avenues.avenuesvo')),
            ],
            options={
                'db_table': 'floor_table',
                'unique_together': {('floors_name', 'floors_plan')},
            },
        ),
    ]
