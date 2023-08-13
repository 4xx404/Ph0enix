# Ph0enix  
A search tool for finding usernames across a variety of sites.  
  
# How it works?  
The tool uses a config file which holds a list of urls. For every url inside the list, the tool will find the sites where the username matches.  

# Usage  
```
git clone https://github.com/4xx404/Ph0enix.git
cd Ph0enix
pip3 install -r requirements.txt
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
 | "--"P|| "--"H|| "--"0|| "--"E|| "--"N|| "--"I|| "--"X|| "--"V|| "--"3|
 `------'`------'`------'`------'`------'`------'`------'`------'`------'

 Authors: 4xx404			     https://github.com/4xx404
 Contributors: jcalabres		 https://github.com/jcalabres
 Version: 1.0

 [?] Matches may not always be specific to the user you are looking for.
 [?] For example, someone else could have used the same username elsewhere.

 Searching for username: test143

 ✅ Found 23 potential matches out of 61 websites

 | Website: Bitbucket 
 | Location: https://bitbucket.org/test143

 | Website: Deviantart 
 | Location: https://test143.deviantart.com/

 | Website: Disqus 
 | Location: https://disqus.com/by/test143

 | Website: Ebay 
 | Location: https://www.ebay.com/usr/test143

 | Website: Facebook 
 | Location: https://www.facebook.com/test143

 | Website: Github 
 | Location: https://github.com/test143

 | Website: Gravatar 
 | Location: https://en.gravatar.com/test143

 | Website: Instagram 
 | Location: https://www.instagram.com/test143

 | Website: Medium 
 | Location: https://medium.com/@/test143

 | Website: Pastebin 
 | Location: https://pastebin.com/u/test143

 | Website: Pinterest 
 | Location: https://www.pinterest.com/test143

 | Website: Reddit 
 | Location: https://www.reddit.com/user/test143

 | Website: Reverbnation 
 | Location: https://www.reverbnation.com/test143

 | Website: Scribd 
 | Location: https://www.scribd.com/test143

 | Website: Slideshare 
 | Location: https://slideshare.net/test143

 | Website: Soundcloud 
 | Location: https://soundcloud.com/test143

 | Website: Spotify 
 | Location: https://open.spotify.com/user/test143

 | Website: Steam 
 | Location: https://steamcommunity.com/id/test143

 | Website: Tumblr 
 | Location: https://test143.tumblr.com/

 | Website: Vk 
 | Location: https://vk.com/test143

 | Website: Wattpad 
 | Location: https://www.wattpad.com/user/test143

 | Website: Ycombinator 
 | Location: https://news.ycombinator.com/user?id=test143

 | Website: Youtube 
 | Location: https://www.youtube.com/c/test143
```
