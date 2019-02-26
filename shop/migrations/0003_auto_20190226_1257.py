# Generated by Django 2.1.7 on 2019-02-26 12:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190226_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='model_number',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='device',
            name='model_numer',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='device',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]
