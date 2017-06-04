import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ixmon.settings")
django.setup()

from devices.models import Router

def main():

    myRouter = Router.objects.get(hostname="vmx7")

    print myRouter.hostname



if __name__ == '__main__':
    main()
