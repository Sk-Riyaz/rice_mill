# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 17:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rice_mill', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bag_types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bag_type', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('vehicle_no', models.CharField(max_length=100)),
                ('no_of_bags', models.IntegerField()),
                ('weighment', models.IntegerField()),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='rice_variety',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rice_type', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='broker',
            name='username',
        ),
        migrations.AddField(
            model_name='broker',
            name='broker_name',
            field=models.TextField(default='unknown', max_length=256, unique=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='_rice_variety',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rice_mill.rice_variety'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='bag_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rice_mill.bag_types'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='broker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rice_mill.broker'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
