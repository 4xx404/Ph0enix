# -*- coding: utf-8 -*-

import requests
import time

class bcolors:
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'


uname = str(raw_input('Enter username: '))

instagram = 'https://www.instagram.com/'+uname
facebook = 'https://www.twitter.com/'+uname
twitter = 'https://www.twitter.com/'+uname
youtube = 'https://www.youtube.com/'+uname
tumblr = 'https://'+uname+'.tumblr.com'
blogspot = 'https://'+uname+'.blogspot.com'
google_plus = 'https://plus.google.com/s/'+uname+'/top'
reddit = 'https://www.reddit.com/user/'+uname
wordpress = 'https://'+uname+'.wordpress.com'
pinterest = 'https://www.pinterest.com/'+uname
github = 'https://github.com/'+uname
flickr = 'https://www.flickr.com/people/'+uname
steam = 'https://steamcommunity.com/id/'+uname
vimeo = 'https://vimeo.com/'+uname
soundcloud = 'https://soundcloud.com/'+uname
disqus = 'https://disqus.com/by/'+uname
medium = 'https://medium.com/@/'+uname
deviantart = 'https://'+uname+'.deviantart.com'
vk = 'https://vk.com/'+uname
aboutme = 'https://about.me/'+uname
imgur = 'https://imgur.com/user/'+uname
flipboard = 'https://flipboard.com/@/'+uname
slideshare = 'https://slideshare.net/'+uname
fotolog = 'https://fotolog.com/'+uname
spotify = 'https://open.spotify.com/user/'+uname
mixcloud = 'https://www.mixcloud.com/'+uname
scribd = 'https://www.scribd.com/'+uname
badoo = 'https://www.badoo.com/en/'+uname
patreon = 'https://www.patreon.com/'+uname
bitbucket = 'https://bitbucket.org/'+uname
dailymotion = 'https://www.dailymotion.com/'+uname
etsy = 'https://www.etsy.com/shop/'+uname
cashme = 'https://cash.me/'+uname
behance = 'https://www.behance.net/'+uname
goodreads = 'https://www.goodreads.com/'+uname
instructables = 'https://www.instructables.com/member/'+uname
keybase = 'https://www.keybase.io/'+uname
kongregate = 'https://kongregate.com/accounts/'+uname
livejournal = 'https://'+uname+'.livejournal.com'
angellist = 'https://www.angel.co/'+uname
last_fm = 'https://www.last.fm/user/'+uname
dribbble = 'https://www.dribbble.com/'+uname
codeacademy = 'https://www.codeacademy.com/'+uname
gravatar = 'https://en.gravatar.com/'+uname
pastebin = 'https://pastebin.com/u/'+uname
roblox = 'https://www.roblox.com/users/'+uname+'/profile/'
gumroad = 'https://www.gumroad.com/'+uname
wattpad = 'https://www.wattpad.com/user/'+uname
canva = 'https://www.canva.com/'+uname
creative_market = 'https://creativemarket.com/'+uname
trakt = 'https://www.trakt.tv/users/'+uname
five_hundred_px = 'https://500px.com/'+uname
buzzfeed = 'https://buzzfeed.com/'+uname
tripadvisor = 'https://tripadvisor.com/members/'+uname
hubpages = 'https://'+uname+'.hubpages.com'
contently = 'https://'+uname+'.contently.com'
houzz = 'https://houzz.com/user/'+uname
blipfm = 'https://blip.fm/'+uname
wikipedia = 'https://www.wikipedia.org/wiki/User:'+uname
ycombinator = 'https://news.ycombinator.com/user?id='+uname
reverbnation = 'https://www.reverbnation.com/'+uname
designspiration = 'https://www.designspiration.net/'+uname
bandcamp = 'https://www.bandcamp.com/'+uname
ifttt = 'https://www.ifttt.com/p/'+uname
ebay = 'https://www.ebay.com/usr/'+uname
slack = 'https://'+uname+'.slack.com'
okcupid = 'https://www.okcupid.com/profile/'+uname
skyscanner = 'https://www.trip.skyscanner.com/user/'+uname
ello = 'https://ello.co/'+uname
tracky = 'https://tracky.com/user/~'+uname
basecamp = 'https://'+uname+'.basecamphq.com/Login'

sites = [instagram, facebook, twitter, youtube, tumblr, blogspot, google_plus, reddit, wordpress, pinterest, github, flickr, steam, vimeo, soundcloud, disqus, medium, deviantart, vk, aboutme, imgur, flipboard, slideshare, fotolog, spotify, mixcloud, scribd, badoo, patreon, bitbucket, dailymotion, etsy, cashme, behance, goodreads, instructables, keybase, kongregate, livejournal, angellist, last_fm, dribbble, codeacademy, gravatar, pastebin, roblox, gumroad, wattpad, canva, creative_market, trakt, five_hundred_px, buzzfeed, tripadvisor, hubpages, contently, houzz, blipfm, wikipedia, ycombinator, reverbnation, designspiration, bandcamp, ifttt, ebay, slack, okcupid, skyscanner, ello, tracky, basecamp]



def banner():
	print(bcolors.RED + "+[+[+[ Ph03n1x v1.0 ]+]+]+")
	print(bcolors.GREEN + '''
 __       ___   ___
[  ] [       ] [   ]      /|
[__] [__   __] [   ] ,__   |  \ /
[    [  ]    ] [   ] [  ]  |   :
[    [  ] ___] [___] [  ) _|_ / \	''')


def search():
	print '+[+[+[ Searching for username: '+uname+' ]+]+]+'
	time.sleep(0.5)
	print '........'
	time.sleep(0.5)
	print '........\n'
	time.sleep(0.5)

	print '+[+[+[ Ph30n1x v1 is working... ]+]+]+\n'
	time.sleep(0.5)
	print'........'
	time.sleep(0.5)
	print'........\n'
	time.sleep(0.5)

	time.sleep(1)

	count = 0
	match = True
	for url in sites:
		r = requests.get(url)

		if r.status_code == 200:
			r.status_code = str('200')
			if match == True:
				print'[+] FOUND Matches'
				match = False

			print '\n'+url+' - '+r.status_code+' - OK'
			if uname in r.text:
				print 'POSITIVE Match: Username:'+uname+' - text has been detected in url.'
			else:
				print 'NEGATIVE Match: Username:'+uname+' - text has NOT been detected in url. Could be a FALSE POSITIVE.'
		count += 1
		count2str = str(count)
	total = str(len(sites))
	print 'FINISHED: A total of '+count2str+' MATCHES found out of '+total+' websites.'

if __name__=='__main__':
	banner()
	search()
