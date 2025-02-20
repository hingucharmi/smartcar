# Generated by Django 5.0.6 on 2025-02-12 09:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0002_alter_customers_customers_phone'),
        ('subscriptions_plan', '0002_alter_subscriptionsplanvo_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionsVO',
            fields=[
                ('subscriptions_id', models.AutoField(null=None, primary_key=True, serialize=False)),
                ('start_ts', models.CharField(default='', max_length=25)),
                ('end_ts', models.CharField(default='')),
                ('subscriptions_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('subscriptions_validity', models.DecimalField(decimal_places=2, max_digits=20)),
                ('subscriptions_customers_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customers')),
                ('subscriptions_subscriptionsplans_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='subscriptions_plan.subscriptionsplanvo')),
            ],
            options={
                'db_table': 'subscriptions',
            },
        ),
    ]
