#!/usr/bin/env python

# Credit: Much of this started with code from https://github.com/nemith/peeringbuddy/blob/master/peeringbuddy.py

import requests
import pprint
import argparse

def pdb_query_net(asn):
    r = requests.get(
        "https://www.peeringdb.com/api/net?asn={}&depth=2".format(asn))
    return r.json()['data'][0]
'''
def pdb_query_net(ix):
    r = requests.get(
        "https://www.peeringdb.com/api/net?ix={}&depth=2".format(asn))
'''
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--myasn", type=int, required=True)
    parser.add_argument("--theirasn", type=int, required=True)
    parser.add_argument("--ixid", type=int, required=False)
    args = parser.parse_args()

    mydata = pdb_query_net(args.myasn)
    theirdata = pdb_query_net(args.theirasn)

    #pprint.pprint(mydata)

    mylans = []
    mydict = {}
    for lan in mydata['netixlan_set']:
        mylans.append(lan['ix_id'])
        mydict[lan['ix_id']]=lan['ipaddr4']
    #print mylans
    #print mydict

    theirlans = []
    theirdict = {}
    for lan in theirdata['netixlan_set']:
        theirlans.append(lan['ix_id'])
        theirdict[lan['ix_id']]=lan['ipaddr4']
    #print theirlans
    
    lans = list(set(mylans).intersection(theirlans))

    #print(lans)

    for ix in lans:
        print "LAN: " + str(ix) + " Our IP: " + mydict[ix] + " Their IP: " + theirdict[ix]


if __name__ == "__main__":
    main()
