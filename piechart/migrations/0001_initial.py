# Generated by Django 4.0.2 on 2022-03-23 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('population', models.IntegerField()),
                ('area', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'population',
            },
        ),
    ]
