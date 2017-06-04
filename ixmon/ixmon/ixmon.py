import os
import django
from jnpr.junos import Device
from lxml import etree
import xmltodict

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ixmon.settings")
django.setup()

from devices.models import Router

def ping_neighbor(router,neighbor):
    print router.ipv4address
    dev = Device(host=router.ipv4address, user='ntc', password='ntc123',
        gather_facts=False)
    dev.open()
    print dev.rpc.ping(count='1', host=neighbor)
    xmloutput = dev.rpc.ping(count='3', host=neighbor)
    output = xmltodict.parse(etree.tostring(xmloutput))
    print(output)
    #print etree.tostring(xmloutput)

def main():
    myRouter = Router.objects.get(hostname="vmx7")
    neighbor = "4.2.2.2"
    print myRouter.hostname
    ping_neighbor(myRouter, neighbor)

if __name__ == '__main__':
    main()
