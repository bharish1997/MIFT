# Generated by Django 3.1 on 2020-10-11 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20201002_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phno',
            field=models.TextField(default=1, max_length=12),
            preserve_default=False,
        ),
    ]