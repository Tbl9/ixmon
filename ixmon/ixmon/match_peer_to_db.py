import requests,django,os, argparse

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ixmon.settings")
django.setup()

from devices.models import Router,Exchange
from peers.models import Peer

def get_peer_data(asn):
    r = requests.get('https://peeringdb.com/api/net?asn={}&depth=2'.format(asn))
    return r.json()['data'][0]


def find_matching_exchanges(remote_asn_data, list_of_matches, asn):

    for remote_exchange in remote_asn_data['netixlan_set']:
        if remote_exchange['ix_id'] in list_of_matches:
            ###Insert check to determine if we peer here
            ###if we peer do email or something
            matching_exchange = Exchange.objects.get(peering_db_id=remote_exchange['ix_id'])
            print "Matching exchange - {}".format(matching_exchange.name)

            peerlist = Peer.objects.filter(ipv4address=remote_exchange['ipaddr4'])

            for peer in peerlist:
                print "Peering - TRUE - {}".format(peer.ipv4address)


    return list_of_matches


def get_exchange_id_list():
    ix_id_list = []
    for local_exchange in Exchange.objects.all():
        ix_id_list.append(local_exchange.peering_db_id)
    return ix_id_list


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--asn")
    args = parser.parse_args()

    peerdata = get_peer_data(args.asn)

    ourix = get_exchange_id_list()
    matchlist = find_matching_exchanges(peerdata, ourix, args.asn)


if __name__ == '__main__':
    main()

