# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime


class Peer(models.Model):
    name = models.CharField(max_length=100)
    asn = models.CharField(max_length=100)
    ipv4address = models.CharField(max_length=100)
    ipv6address = models.CharField(max_length=1000)
    exchange = models.ForeignKey('devices.Exchange')

    def __unicode__(self):
        return self.name


class Poll(models.Model):
    peer = models.ForeignKey(Peer)
    timestamp = models.IntegerField()
    ping_min = models.FloatField()
    ping_max = models.FloatField()
    ping_avg = models.FloatField()
