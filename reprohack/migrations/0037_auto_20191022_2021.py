# Generated by Django 2.2.6 on 2019-10-22 20:21

import datetime
from django.db import migrations, models
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reprohack', '0036_auto_20191022_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='geom',
            field=djgeojson.fields.PointField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='time_end',
            field=models.TimeField(default=datetime.time(16, 0, 40, 786063)),
        ),
        migrations.AlterField(
            model_name='event',
            name='time_start',
            field=models.TimeField(default=datetime.time(10, 0, 40, 786030)),
        ),
    ]
