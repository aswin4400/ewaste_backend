# Generated by Django 2.1.7 on 2019-03-02 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20190302_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='price',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
