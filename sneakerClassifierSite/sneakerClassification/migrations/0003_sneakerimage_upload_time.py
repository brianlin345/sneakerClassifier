# Generated by Django 3.0.6 on 2020-05-21 05:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sneakerClassification', '0002_auto_20200520_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='sneakerimage',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date uploaded'),
        ),
    ]