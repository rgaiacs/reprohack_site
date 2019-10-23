# Generated by Django 2.2.6 on 2019-10-22 18:58

import datetime
from django.db import migrations, models
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reprohack', '0034_auto_20191022_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='geom',
            field=djgeojson.fields.PointField(default={'coordinates': [0, 0], 'type': 'Point'}),
        ),
        migrations.AlterField(
            model_name='event',
            name='time_end',
            field=models.TimeField(default=datetime.time(16, 0, 36, 743119)),
        ),
        migrations.AlterField(
            model_name='event',
            name='time_start',
            field=models.TimeField(default=datetime.time(10, 0, 36, 743085)),
        ),
    ]