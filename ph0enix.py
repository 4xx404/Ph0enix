# -*- coding: utf-8 -*-
from sys import *
import requests
import time

class bcolors:
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'

def banner():
	print(bcolors.RED + "+[+[+[ Ph0enix v1.0 ]+]+]+"),
	print(bcolors.GREEN + '''
 ____  _     ____  _____ _      _ ___  _
/  __\/ \ /|/  _ \/  __// \  /|/ \\  \//
|  \/|| |_||| / \||  \  | |\ ||| | \  / 
|  __/| | ||| \_/||  /_ | | \||| | /  \ 
\_/   \_/ \|\____/\____\\_/  \|\_//__/\\ ''')

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
	print('+[+[+[ Searching for username: '+username+' ]+]+]+')
	print('+[+[+[ Ph0enix v1 is working... ]+]+]+\n')
	count = 0
	for w,u in sites.items():
		r = requests.get(u)
		if r.status_code == 200:
			if username in r.text:
                            print('MATCH: {} in {}:{}'.format(username,w,u))
		            count+= 1
		count2str=str(count)
	total= str(len(sites))
	print('FINISHED: A total of '+count2str+' MATCHES found out of '+total+' websites.')

if __name__=='__main__':
    if len(argv)<2:
        print("Please provide an username.")
        exit(0)
    else:
        username=argv[1]
    banner()
    sites=getUserURLS(username)
    search(username,sites)
