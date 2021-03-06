# Generated by Django 3.1.5 on 2021-02-03 23:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=40, verbose_name='Description')),
                ('date_creation', models.DateTimeField(max_length=14, verbose_name='Order Date/Time')),
                ('date_completion', models.DateTimeField(max_length=13, verbose_name='Completion Date/Time')),
                ('sales_tax', models.FloatField(max_length=10, verbose_name='Sales Tax')),
                ('discount', models.FloatField(max_length=10, verbose_name='Discount')),
                ('trade_in', models.FloatField(blank=True, max_length=10, null=True, verbose_name='Trade In')),
                ('total_price', models.FloatField(max_length=10, verbose_name='Total Price')),
                ('payment', models.CharField(max_length=20, verbose_name='Payment method')),
                ('transaction_status', models.CharField(max_length=20, verbose_name='Transaction Status')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car', verbose_name='Car')),
                ('client', models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='clients.client', verbose_name='Client')),
                ('employee', models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Employee')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'db_table': 'orders',
            },
        ),
    ]
