# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Authentication(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Router(models.Model):
    vendor_choices = (
        ('junos', 'Junos'),
        ('arista', 'Arista'),
    )
    hostname = models.CharField(max_length=100)
    ipv4address = models.CharField(max_length=100)
    enabled = models.BooleanField(default=True)
    auth = models.ForeignKey(Authentication)
    vendor = models.CharField(max_length=10, choices=vendor_choices, default="Junos")

    def __unicode__(self):
        return self.hostname


class Exchange(models.Model):
    name = models.CharField(max_length=100)
    device = models.ForeignKey(Router)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    peering_db_id = models.IntegerField()


    def __unicode__(self):
        return self.name