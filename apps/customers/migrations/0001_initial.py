# Generated by Django 5.0.6 on 2025-02-07 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customers_id', models.AutoField(primary_key=True, serialize=False)),
                ('customers_firstname', models.CharField(default='', max_length=40)),
                ('customers_middlename', models.CharField(default='', max_length=40)),
                ('customers_lastname', models.CharField(default='', max_length=40)),
                ('customers_username', models.CharField(default='', max_length=40)),
                ('customers_email', models.EmailField(max_length=25)),
                ('customers_password', models.CharField(default='', max_length=40)),
                ('customers_phone', models.IntegerField()),
                ('customers_avatar', models.CharField(default='', max_length=40)),
            ],
            options={
                'db_table': 'customers',
                'unique_together': {('customers_email', 'customers_phone')},
            },
        ),
    ]
