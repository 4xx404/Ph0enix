# Ph0enix  
A search tool for finding usernames across a variety of sites.  
  
# How it works?  
The tool uses a config file which holds a list of urls. For every url inside the list, the tool will find the sites where the username matches.  

# Usage  
```
git clone https://github.com/4xx404/Ph0enix.git
cd Ph0enix
python3 -m pip install -r requirements.txt
python3 ph0enix.py
```
  
# Adding URL's  
Open **Config.py** which can be found in the **Core/** directory and add the new URL with the following format:  
```
site:url  
example:https://www.example.com/[USER]
example:https://[USER].example.com/
```
  
Be sure to put [USER] part inside the url to make the tool work properly.  

# Example  
```
 .------..------..------..------..------..------..------..------..------.
 |P.--. ||H.--. ||0.--. ||E.--. ||N.--. ||I.--. ||X.--. ||V.--. ||3.--. |
 | :/\: || :/\: || :/\: || (\/) || :(): || (\/) || :/\: || :(): || :/\: |
 | (__) || (__) || :\/: || :\/: || ()() || :\/: || (__) || ()() || (__) |
 | "--"P|| "--"H|| "--"0|| "--"E|| "--"N|| "--"I|| "--"X|| "--"V|| "--"2|
 `------'`------'`------'`------'`------'`------'`------'`------'`------'

 Author: 4xx404
 Version: 3.0
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
	  [✓] Github
	  [✗] Goodreads
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
	  [✓] Pinterest
	  [✓] Reddit
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
	  [✓] Youtube


|✓| Found 6 matches out of 63 websites

| Website: Github
| Location: https://github.com/test143

| Website: Pinterest
| Location: https://www.pinterest.com/test143

| Website: Reddit
| Location: https://www.reddit.com/user/test143

| Website: Steam
| Location: https://steamcommunity.com/id/test143

| Website: Twitter
| Location: https://www.twitter.com/test143

| Website: Youtube
| Location: https://www.youtube.com/c/test143
```
