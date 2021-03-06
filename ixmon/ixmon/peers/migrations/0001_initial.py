# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-04 20:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Peer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('asn', models.CharField(max_length=100)),
                ('ipv4address', models.CharField(max_length=100)),
                ('ipv6address', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.IntegerField()),
                ('ping_min', models.FloatField()),
                ('ping_max', models.FloatField()),
                ('ping_avg', models.FloatField()),
                ('peer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peers.Peer')),
            ],
        ),
    ]
