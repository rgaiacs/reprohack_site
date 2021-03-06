# Generated by Django 2.2.6 on 2019-10-07 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('event_title', models.CharField(max_length=200)),
                ('event_description', models.TextField()),
                ('event_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('event_time_start', models.TimeField()),
                ('event_time_end', models.TimeField()),
                ('event_address', models.TextField()),
                ('event_location', models.TextField()),
                ('lat', models.IntegerField()),
                ('lon', models.IntegerField()),
                ('event_submission_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('event_registration_url', models.URLField()),
                ('event_host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
