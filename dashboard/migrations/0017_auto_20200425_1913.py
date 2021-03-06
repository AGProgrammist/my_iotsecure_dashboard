# Generated by Django 2.2.12 on 2020-04-25 11:13

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_auto_20200425_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_num',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=11, region=None),
        ),
    ]
