# Generated by Django 2.2.12 on 2020-05-23 13:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0024_device_access_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='deviceandcommand',
            name='isEnable',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='deviceandcommand',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]