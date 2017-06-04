import os
import django
from jnpr.junos import Device

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ixmon.settings")
django.setup()

from devices.models import Router

def ping_neighbor(router,neighbor):
    print router.ipv4address
    dev = Device(host=router.ipv4address, user='ntc', password='ntc123',
        gather_facts=False)
    dev.open()
    # print dev.cli("")


def main():
    myRouter = Router.objects.get(hostname="vmx7")
    neighbor = "208.23.43.51"
    print myRouter.hostname
    ping_neighbor(myRouter, neighbor)

if __name__ == '__main__':
    main()
