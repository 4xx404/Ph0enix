# Ph0enix  
A search tool for finding usernames across a variety of sites.  
  
# How it works?  
The tool reads a file named urls.txt. For every url inside the file, the tool will find for username matches.  
  
# Usage  
  
```
git clone https://github.com/4xx404/Ph0enix.git
pip install requests
cd Ph0enix
python3 ph0enix.py
```
  
# Adding URL's  
Open the urls.txt file and put the new URL with the next format:  
  
```
site:url
```
  
Be sure to put "[USER]" inside the url(without quotes) to make the tool work properly.  
  
# Example  
  
```
 .------..------..------..------..------..------..------..------..------.
 |P.--. ||H.--. ||0.--. ||E.--. ||N.--. ||I.--. ||X.--. ||V.--. ||2.--. |
 | :/\: || :/\: || :/\: || (\/) || :(): || (\/) || :/\: || :(): || :/\: |
 | (__) || (__) || :\/: || :\/: || ()() || :\/: || (__) || ()() || (__) |
 | "--"P|| "--"H|| "--"0|| "--"E|| "--"N|| "--"I|| "--"X|| "--"V|| "--"2|
 `------'`------'`------'`------'`------'`------'`------'`------'`------'

 Author: 4xx404
 Version: 2.0
 Github: https://github.com/4xx404

 [?] Matches may not always be specific to the user you are looking for.
 [?] For example, someone else could have used the same username elsewhere.

 Searching for username: test143
	  [✗] About Me
	  [✗] Angel List
	  [✗] Badoo
	  [✗] Bandcamp
	  [✗] Basecamp Hq
	  [✗] Behance
	  [✗] Bitbucket
	  [✗] Blipfm
	  [✗] Buzzfeed
	  [✗] Canva
	  [✗] Cashme
	  [✗] Codeacademy
	  [✗] Contently
	  [✗] Creative Market
	  [✗] Dailymotion
	  [✗] Designspiration
	  [✗] Deviantart
	  [✗] Disqus
	  [✗] Dribbble
	  [✗] Ebay
	  [✗] Ello
	  [✗] Etsy
	  [✗] Facebook
	  [✗] Five Hundred Px
	  [✗] Flickr
	  [✗] Fotolog
	  [✗] Github
	  [✗] Goodreads
	  [✓] Google Plus
	  [✗] Gravatar
	  [✗] Gumroad
	  [✗] Houzz
	  [✗] Hubpages
	  [✗] Imgur
	  [✗] Instagram
	  [✗] Instructables
	  [✗] Keybase
	  [✗] Kongregate
	  [✗] Last Fm
	  [✗] Livejournal
	  [✗] Medium
	  [✗] Mixcloud
	  [✗] Okcupid
	  [✗] Pastebin
	  [✗] Patreon
	  [✗] Pinterest
	  [✗] Reddit
	  [✗] Reverbnation
	  [✗] Roblox
	  [✗] Scribd
	  [✗] Skyscanner
	  [✗] Slack
	  [✗] Slideshare
	  [✗] Soundcloud
	  [✗] Spotify
	  [✓] Steam
	  [✗] Trakt
	  [✗] Trip Advisor
	  [✗] Tumblr
	  [✓] Twitter
	  [✗] Vk
	  [✗] Wattpad
	  [✗] Wikipedia
	  [✗] Ycombinator
	  [✗] Youtube
 
 Websites Checked: 65
 Matches Found: 3
	  [✓] https://plus.google.com/s/test143/top
	  [✓] https://steamcommunity.com/id/test143
	  [✓] https://www.twitter.com/test143

 Scan Finished...
```
