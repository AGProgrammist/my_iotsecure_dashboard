# Generated by Django 2.2.12 on 2020-04-25 09:24

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_auto_20200425_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_num',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=11, region=None),
        ),
    ]
