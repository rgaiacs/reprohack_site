# Generated by Django 2.2.6 on 2019-10-22 18:55

import datetime
from django.db import migrations, models
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reprohack', '0033_auto_20191022_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='geom',
            field=djgeojson.fields.PointField(verbose_name={'coordinates': [0, 0], 'type': 'Point'}),
        ),
        migrations.AlterField(
            model_name='event',
            name='time_end',
            field=models.TimeField(default=datetime.time(16, 0, 55, 617327)),
        ),
        migrations.AlterField(
            model_name='event',
            name='time_start',
            field=models.TimeField(default=datetime.time(10, 0, 55, 617295)),
        ),
    ]
