# -*- coding: utf-8 -*-
from sys import *
import requests
import time, os, sys

class bcolors:
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'

def banner():
	os.system('clear')
	print(bcolors.RED + '''
.------..------..------..------..------..------..------..------..------.
|'''+bcolors.GREEN+'''P'''+bcolors.RED+'''.--. ||'''+bcolors.GREEN+'''H'''+bcolors.RED+'''.--. ||'''+bcolors.GREEN+'''0'''+bcolors.RED+'''.--. ||'''+bcolors.GREEN+'''E'''+bcolors.RED+'''.--. ||'''+bcolors.GREEN+'''N'''+bcolors.RED+'''.--. ||'''+bcolors.GREEN+'''I'''+bcolors.RED+'''.--. ||'''+bcolors.GREEN+'''X'''+bcolors.RED+'''.--. ||'''+bcolors.GREEN+'''V'''+bcolors.RED+'''.--. ||'''+bcolors.GREEN+'''1'''+bcolors.RED+'''.--. |
| :/\: || :/\: || :/\: || (\/) || :(): || (\/) || :/\: || :(): || :/\: |
| (__) || (__) || :\/: || :\/: || ()() || :\/: || (__) || ()() || (__) |
| "--"'''+bcolors.GREEN+'''P'''+bcolors.RED+'''|| "--"'''+bcolors.GREEN+'''H'''+bcolors.RED+'''|| "--"'''+bcolors.GREEN+'''0'''+bcolors.RED+'''|| "--"'''+bcolors.GREEN+'''E'''+bcolors.RED+'''|| "--"'''+bcolors.GREEN+'''N'''+bcolors.RED+'''|| "--"'''+bcolors.GREEN+'''I'''+bcolors.RED+'''|| "--"'''+bcolors.GREEN+'''X'''+bcolors.RED+'''|| "--"'''+bcolors.GREEN+'''V'''+bcolors.RED+'''|| "--"'''+bcolors.GREEN+'''1'''+bcolors.RED+'''|
`------'`------'`------'`------'`------'`------'`------'`------'`------'
	''')

def getUserURLS(username):
	urlsfile=open("urls.txt","r")
	content=urlsfile.read().split("\n")[0:-1]
	sites={}
	for line in content:
        	website=line.split(':',1)[0]
        	url=line.split(':',1)[1].replace("[USER]",username)
        	sites[website]=url
	return sites

def search(username,sites):
	print(bcolors.YELLOW + '[' + bcolors.GREEN + '+' + bcolors.YELLOW + '] ' + bcolors.GREEN + '			Ph0enix v1 is working...		     ' + bcolors.YELLOW + '[' + bcolors.GREEN + '+' + bcolors.YELLOW + ']')
	print(bcolors.GREEN + '\nSearching for username: ' + bcolors.RED + username + "\n")
	print(bcolors.GREEN + 'Matches may not always be specific to the user you are looking.\nFor example, someone else could have used the same username elsewhere.\n')
	count = 0
	for w,u in sites.items():
		r = requests.get(u)
		if r.status_code == 200:
			if username in r.text:
				print(bcolors.GREEN + 'MATCH: ' + bcolors.RED + username + bcolors.GREEN + ' in ' + bcolors.RED + w + bcolors.GREEN + ':' + bcolors.RED + u)
				count += 1
				count2str=str(count)
	total= str(len(sites))
	print(bcolors.RED + '\nFINISHED:' + bcolors.GREEN + ' A total of ' + bcolors.RED + count2str + ' MATCHES' + bcolors.GREEN + ' found out of ' + bcolors.RED + total + ' websites\n' + bcolors.GREEN)

if __name__=='__main__':
	if len(argv)<2:
	        print(bcolors.RED + "ERROR: " + bcolors.GREEN + "Please provide an username.")
	        exit(0)
	else:
	        username=argv[1]
	banner()
	sites=getUserURLS(username)
	search(username,sites)
