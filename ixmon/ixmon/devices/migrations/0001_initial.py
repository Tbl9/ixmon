# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-04 19:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authentication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Router',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=100)),
                ('ipv4address', models.CharField(max_length=100)),
                ('enabled', models.BooleanField(default=True)),
                ('vendor', models.CharField(choices=[('junos', 'Junos'), ('arista', 'Arista')], default='Junos', max_length=2)),
                ('auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.Authentication')),
            ],
        ),
    ]
