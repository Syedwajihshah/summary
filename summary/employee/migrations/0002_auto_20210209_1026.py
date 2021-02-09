# Generated by Django 3.0.5 on 2021-02-09 10:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='salary_per_day',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='employee',
            name='total_working_days',
            field=models.IntegerField(default=30),
        ),
        migrations.AddField(
            model_name='historicalemployee',
            name='salary_per_day',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='historicalemployee',
            name='total_working_days',
            field=models.IntegerField(default=30),
        ),
        migrations.AlterField(
            model_name='department',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 10, 26, 49, 22216)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 10, 26, 49, 22778)),
        ),
        migrations.AlterField(
            model_name='historicalemployee',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 10, 26, 49, 22778)),
        ),
    ]