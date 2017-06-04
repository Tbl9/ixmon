# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from .models import Router, Authentication, Exchange

admin.site.register(Router)
admin.site.register(Authentication)
admin.site.register(Exchange)