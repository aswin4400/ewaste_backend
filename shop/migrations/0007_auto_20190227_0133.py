# Generated by Django 2.1.7 on 2019-02-27 01:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_device_manufacturer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.RemoveField(
            model_name='device',
            name='price',
        ),
        migrations.AddField(
            model_name='banner',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banner_device', to='shop.Device'),
        ),
        migrations.AddField(
            model_name='banner',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banner_seller', to=settings.AUTH_USER_MODEL),
        ),
    ]
