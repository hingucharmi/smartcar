# Generated by Django 5.0.6 on 2025-02-04 12:49

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions_plan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionsplanvo',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
