# Generated by Django 4.0.2 on 2022-03-23 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('emp_name', models.CharField(max_length=50)),
                ('emp_dob', models.DateField()),
                ('emp_email', models.EmailField(max_length=50)),
                ('emp_password', models.CharField(max_length=30)),
                ('emp_phone', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
