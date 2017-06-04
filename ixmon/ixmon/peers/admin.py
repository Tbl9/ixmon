# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Peer, Poll

admin.site.register(Peer)
admin.site.register(Poll)