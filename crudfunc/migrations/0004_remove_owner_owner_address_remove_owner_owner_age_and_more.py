# Generated by Django 4.0.2 on 2022-02-22 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudfunc', '0003_alter_owner_owner_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='owner_address',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='owner_age',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='owner_contact',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='owner_dob',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='owner_email',
        ),
    ]