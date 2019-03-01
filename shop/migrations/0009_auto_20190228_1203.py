# Generated by Django 2.1.7 on 2019-02-28 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20190228_1109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=10)),
                ('hw_specification', models.TextField()),
                ('sw_specification', models.TextField()),
                ('support_notes', models.TextField()),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.RemoveField(
            model_name='component',
            name='specs',
        ),
        migrations.AddField(
            model_name='component',
            name='specification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Specification'),
        ),
    ]