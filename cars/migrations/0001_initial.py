# Generated by Django 3.1.5 on 2021-02-03 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Brand Name')),
                ('country', models.CharField(max_length=50, verbose_name='Country')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
                'db_table': 'brands',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Car Model')),
                ('generation', models.CharField(blank=True, max_length=30, null=True, verbose_name='Generation')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='cars.brand', verbose_name='Brand')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
                'db_table': 'cars',
            },
        ),
        migrations.CreateModel(
            name='CarItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('production_date', models.DateField(verbose_name='Date of Production')),
                ('color', models.CharField(max_length=20, verbose_name='Color')),
                ('model_year', models.CharField(max_length=4, verbose_name='Model year')),
                ('transmission', models.CharField(choices=[('A', 'Automate'), ('M', 'Manual'), ('R', 'Robot'), ('V', 'Variator')], default='A', max_length=1, verbose_name='Transmission')),
                ('vin', models.CharField(max_length=30, verbose_name='VIN')),
                ('status', models.CharField(choices=[('A', 'Available'), ('S', 'Sold'), ('R', 'Reserved'), ('O', 'Ordered')], default='A', max_length=1, verbose_name='Status')),
                ('cylinders', models.CharField(choices=[('A', '4'), ('B', '5'), ('C', '6'), ('D', '8'), ('E', '12')], default='A', max_length=1, verbose_name='Cylinders')),
                ('price', models.CharField(max_length=8, verbose_name='Price')),
                ('trim', models.CharField(max_length=20, verbose_name='Trim')),
                ('engine_volume', models.CharField(max_length=20, verbose_name='Engine Volume')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_items', to='cars.car', verbose_name='Car')),
            ],
            options={
                'verbose_name': 'Car Item',
                'verbose_name_plural': 'Cars Items',
                'db_table': 'cars_items',
            },
        ),
    ]
