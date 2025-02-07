# Generated by Django 5.0.3 on 2024-05-14 10:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LocationMaster',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('location_name', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'location_master',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=256)),
                ('product_desc', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cust_id', models.AutoField(primary_key=True, serialize=False)),
                ('cust_name', models.CharField(max_length=256)),
                ('cust_no', models.CharField(max_length=256)),
                ('shop_name', models.CharField(max_length=256)),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location_nm', related_query_name='location_nms', to='Coldy.locationmaster')),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_qty', models.IntegerField()),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('order_status', models.CharField(max_length=256)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer', related_query_name='customers', to='Coldy.customer')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', related_query_name='products', to='Coldy.product')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
    ]
