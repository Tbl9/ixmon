#!/usr/bin/python

import netmiko
import json
import pprint

def getJunosPeers(ipaddr):
	net_connect = netmiko.ConnectHandler(device_type='juniper_junos', ip=ipaddr, username='ntc', password='ntc123') 
	output = net_connect.send_command("show bgp neighbor | display json")
	dict_output  = json.loads(output)
	returned_list = []
	for peers in dict_output["bgp-information"][0]["bgp-peer"]:
		peer = {}
		peer["peer-address"] = peers["peer-address"][0]["data"]
		peer["peer-as"] = peers["peer-as"][0]["data"]
		peer["description"] = peers["description"][0]["data"]
		returned_list.append(peer)
	return returned_list


if __name__=="__main__":
	vmx7 = "35.163.254.138"
	getJunosPeers(vmx7)