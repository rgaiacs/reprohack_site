# Generated by Django 2.2.6 on 2019-10-17 12:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reprohack', '0021_auto_20191017_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time_end',
            field=models.TimeField(default=datetime.time(16, 0, 34, 314193)),
        ),
        migrations.AlterField(
            model_name='event',
            name='time_start',
            field=models.TimeField(default=datetime.time(10, 0, 34, 314144)),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
