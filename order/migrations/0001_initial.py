# Generated by Django 4.0.2 on 2022-03-23 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('park_name', models.CharField(max_length=64)),
                ('park_type', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_payment', models.CharField(max_length=50, null=True)),
                ('order_garage', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='order.park')),
            ],
            options={
                'db_table': 'order_pay',
            },
        ),
    ]
