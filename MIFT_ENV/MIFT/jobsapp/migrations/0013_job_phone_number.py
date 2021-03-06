# Generated by Django 3.0.7 on 2020-10-11 13:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0012_auto_20201011_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.", regex='^\\+?1?\\d{8,10}$')]),
        ),
    ]
