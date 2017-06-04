#!/usr/bin/env python

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ixmon.settings")
django.setup()

from jnpr.junos import Device
from lxml import etree
import xmltodict
import poll_insert
from devices.models import Router

def ping_neighbor(router,neighbor):
    print router.ipv4address
    dev = Device(host=router.ipv4address, user='ntc', password='ntc123',
        gather_facts=False)
    dev.open()
    dev.rpc.ping(count='1', host=neighbor)
    xmloutput = dev.rpc.ping(count='3', host=neighbor)
    dev.close()
    output = xmltodict.parse(etree.tostring(xmloutput))
    result={}
    result['min']=output["ping-results"]["probe-results-summary"]["rtt-minimum"]
    result['avg']=output["ping-results"]["probe-results-summary"]["rtt-average"]
    result['max']=output["ping-results"]["probe-results-summary"]["rtt-maximum"]
    return result

def main():
    myRouter = Router.objects.get(hostname="vmx7")
    neighbor = "206.81.80.5"
    print myRouter.hostname
    result = ping_neighbor(myRouter, neighbor)
    poll_insert.addpoll(neighbor,result['min'],result['avg'],result['max'])

if __name__ == '__main__':
    main()
