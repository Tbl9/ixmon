#!/usr/bin/python

import netmiko
import json
import pprint

def getJunosPeers(ipaddr, username, password):
	net_connect = netmiko.ConnectHandler(device_type='juniper_junos', ip=ipaddr, username=username, password=password) 
	output = net_connect.send_command("show bgp neighbor | display json")
	dict_output  = json.loads(output)
	returned_list = []
	for peers in dict_output["bgp-information"][0]["bgp-peer"]:
		peer = {}
		peer["peer-address"] = peers["peer-address"][0]["data"]
		peer["peer-as"] = peers["peer-as"][0]["data"]
		peer["peer-state"] = peers["peer-state"][0]["data"]
		returned_list.append(peer)
	return returned_list


if __name__=="__main__":
	vmx7 = "35.163.254.138"
        username = "ntc"
        password = "ntc123"
	print getJunosPeers(vmx7, username, password)	
