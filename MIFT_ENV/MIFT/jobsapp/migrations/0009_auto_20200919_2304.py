# Generated by Django 3.0.7 on 2020-09-19 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0008_auto_20200810_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='category',
        ),
        migrations.AlterField(
            model_name='job',
            name='type',
            field=models.CharField(choices=[('1', 'Fund'), ('2', 'Volunteering')], max_length=10),
        ),
    ]
