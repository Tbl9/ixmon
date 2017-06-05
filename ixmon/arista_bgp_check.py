#!/usr/bin/python

from jsonrpclib import Server
import ssl, pprint



def ignore_ssl():
    try:
            _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
            # Legacy Python that doesn't verify HTTPS certificates by default
                pass
    else:
                    # Handle target environment that doesn't support HTTPS verification
                        ssl._create_default_https_context = _create_unverified_https_context


def arista_bgpstatus(routerip, user, passw):
    ignore_ssl()
    while True:
	routerut = Server( "https://{user}:{passw}@{routerip}/command-api".format(user=user, passw=passw, routerip=routerip) )
	bgpstatus = routerut.runCmds( 1, [ "show ip bgp summary" ] )
	print 'Local ASN:' , bgpstatus[0]["vrfs"]["default"]["asn"]
	peerip = bgpstatus[0]["vrfs"]["default"]["peers"].iterkeys()
	for peer in peerip :
		print 'Peer IP address: ', peer
		peerasn = bgpstatus[0]["vrfs"]["default"]["peers"][peer]
		for keys in peerasn.iterkeys():
			if keys == 'asn':
				print 'Peer ASN: ', peerasn[keys]
	        peerstate = bgpstatus[0]["vrfs"]["default"]["peers"][peer]
		for keys in peerstate.iterkeys():
			if keys == 'peerState':
				print 'Peer State:', peerstate[keys]
	break						
if __name__ == '__main__':

	user = 'ntc'
	passw = 'ntc123'
	routerip = '10.0.0.11'
	arista_bgpstatus(routerip, user, passw)
