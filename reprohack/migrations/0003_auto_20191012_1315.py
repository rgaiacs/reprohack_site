# Generated by Django 2.2.6 on 2019-10-12 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reprohack', '0002_auto_20191012_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='city',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='event',
            name='postcode',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='event',
            name='address',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(default='', max_length=200),
        ),
    ]
