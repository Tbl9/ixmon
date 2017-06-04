import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ixmon.settings")
django.setup()

from peers.models import Poll, Peer


def addpoll(peerip, min, max, avg):
    myPeer = Peer.objects.get(ipv4address=peerip)
    myPoll = Poll(peer=myPeer, ping_min=min, ping_max=max, ping_avg=avg)
    myPoll.save()


def main():

    m = addpoll('206.81.80.30', 10, 100, 12)


if __name__ == '__main__':
    main()
