# Generated by Django 2.2.6 on 2019-10-17 09:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reprohack', '0020_auto_20191017_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time_end',
            field=models.TimeField(default=datetime.time(16, 0, 2, 685699)),
        ),
        migrations.AlterField(
            model_name='event',
            name='time_start',
            field=models.TimeField(default=datetime.time(10, 0, 2, 685668)),
        ),
    ]
