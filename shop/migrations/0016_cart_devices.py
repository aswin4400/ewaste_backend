# Generated by Django 2.1.7 on 2019-03-03 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20190303_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='devices',
            field=models.ManyToManyField(to='shop.Device'),
        ),
    ]
