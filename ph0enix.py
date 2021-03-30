# -*- coding: utf-8 -*-

import requests
import time, os, sys

class bc:
	GC = '\033[1;39m'
	BC = '\033[1;34m'
	RC = '\033[1;31m'

author = bc.BC + "\n Author: " + bc.RC + "4" + bc.GC + "x" + bc.BC + "x" + bc.RC + "4" + bc.GC + "0" + bc.BC + "4\n"
version = bc.BC + " Version: " + bc.RC + "2" + bc.GC + "." + bc.BC + "0\n"
github = bc.BC + " Github: " + bc.RC + "h" + bc.GC + "t" + bc.BC + "t" + bc.RC + "p" + bc.GC + "s" + bc.BC + ":" + bc.RC + "/" + bc.GC + "/" + bc.BC + "g" + bc.RC + "i" + bc.GC + "t" + bc.BC + "h" + bc.RC + "u" + bc.GC + "b" + bc.BC + "." + bc.RC + "c" + bc.GC + "o" + bc.BC + "m" + bc.RC + "/" + bc.GC + "4" + bc.BC + "x" + bc.RC + "x" + bc.GC + "4" + bc.BC + "0" + bc.RC + "4\n"

banner = bc.RC + '''
 .------..------..------..------..------..------..------..------..------.
 |'''+bc.GC+'''P'''+bc.RC+'''.--. ||'''+bc.GC+'''H'''+bc.RC+'''.--. ||'''+bc.GC+'''0'''+bc.RC+'''.--. ||'''+bc.GC+'''E'''+bc.RC+'''.--. ||'''+bc.GC+'''N'''+bc.RC+'''.--. ||'''+bc.GC+'''I'''+bc.RC+'''.--. ||'''+bc.GC+'''X'''+bc.RC+'''.--. ||'''+bc.GC+'''V'''+bc.RC+'''.--. ||'''+bc.GC+'''2'''+bc.RC+'''.--. |
 | :/\: || :/\: || :/\: || (\/) || :(): || (\/) || :/\: || :(): || :/\: |
 | (__) || (__) || :\/: || :\/: || ()() || :\/: || (__) || ()() || (__) |
 | "--"'''+bc.GC+'''P'''+bc.RC+'''|| "--"'''+bc.GC+'''H'''+bc.RC+'''|| "--"'''+bc.GC+'''0'''+bc.RC+'''|| "--"'''+bc.GC+'''E'''+bc.RC+'''|| "--"'''+bc.GC+'''N'''+bc.RC+'''|| "--"'''+bc.GC+'''I'''+bc.RC+'''|| "--"'''+bc.GC+'''X'''+bc.RC+'''|| "--"'''+bc.GC+'''V'''+bc.RC+'''|| "--"'''+bc.GC+'''2'''+bc.RC+'''|
 `------'`------'`------'`------'`------'`------'`------'`------'`------'
''' + author + version + github

iBan = bc.BC + " [" + bc.GC + "?" + bc.BC + "]"
sBan = bc.BC + " [" + bc.GC + u'\u2713' + bc.BC + "]"
eBan = bc.BC + " [" + bc.RC + u'\u2717' + bc.BC + "]"

os.system('clear')
print(banner)

def ph0enix():
	try:
		username = str(input(bc.BC + " Username: " + bc.GC))
	except KeyboardInterrupt:
		os.system('clear')
		print(banner)
		print(bc.BC + ' Closing Ph0enix...')
		time.sleep(1)
		os.system('clear')
		print(banner)
		quit()
		
	os.system('clear')
	print(banner)

	try:
		urlFile=open("urls.txt", "r")
		lines = urlFile.readlines()
	except Exception:
		os.system('clear')
		print(banner)
		print(eBan + ' Failed to open URL file\n')
		time.sleep(1)
		ph0enix()

	print(iBan + ' Matches may not always be specific to the user you are looking for.')
	print(iBan + ' For example, someone else could have used the same username elsewhere.\n')

	print(bc.BC + ' Searching for username: ' + bc.GC + username)

	count = 0
	urls = []

	for line in lines:
		line = line.replace('\n', '')
		urls.append(line)
	
	found = []
	
	try:
		for u in urls:
			website = u.split(':', 1)[0]
			url = u.split(':', 1)[1].replace("[USER]", username)

			try:
				r = requests.get(url)
			except Exception:
				continue

			if r.status_code == 200:
				if username in r.text:
					print('\t' + sBan + bc.GC + ' ' + website.title().replace('_',' '))
					found.append(url)
					count += 1
					count2str = str(count)
				else:
					print('\t' + eBan + bc.RC + ' ' + website.title().replace('_',' '))
			else:
				print('\t' + eBan + bc.RC + ' ' + website.title().replace('_',' '))

	except KeyboardInterrupt:
		print('\n\n' + bc.BC + ' Scan Stopped!\n')
		time.sleep(1)
		ph0enix()

	total = str(len(urls))

	print('\n' + bc.BC + ' Websites Checked: ' + bc.GC + total)
	print(bc.BC + ' Matches Found: ' + bc.GC + count2str)
	
	for f in found:
		print('\t' + sBan + ' ' + bc.GC + f)

	print('\n' + bc.BC + ' Scan Finished...')

if __name__ == '__main__':
	ph0enix()
