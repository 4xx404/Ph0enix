# Ph0enix  
A search tool for finding usernames across a variety of sites.  
  
# How it works?  
The tool uses a sqlite database file which holds a list of urls. For every url inside the database, the tool will find the sites where the username matches.  

# Usage  
```
git clone https://github.com/4xx404/Ph0enix.git
cd Ph0enix
pip3 install -r requirements.txt
python3 ph0enix.py
```
  
# Database Interface  
**Enter database interface**  
From the Ph0enix terminal, run ```database```  
  
**Activate website record**  
From the database interface, run ```activate website_id``` (website_id is an MD5 hash).  
  
**Deactivate website record**  
From the database interface, run ```deactivate website_id``` (website_id is an MD5 hash).  
  
**List all website records**  
From the database interface, run ```list```  
  
**Add new website record**  
From the database interface, run ```add website_name url``` (Be sure to put the [USER] part inside the url to make the tool work properly).  
  
**Update website record**  
From the database interface, run ```update website_id type value``` (website_id is an MD5 hash and type can be **name** or **url**).  
  
**Delete website record**  
From the database interface, run ```delete website_id``` (website_id is an MD5 hash).  
  
# Username Search  
From the Ph0enix terminal, enter the username you want to search for and hit enter.  
  
**Store Results**  
By default, matches found in the search will be stored in the database file in the **found_profiles** table. If you want to turn it off, edit **.env** setting **STORE_RESULTS=false**.  
  
# Example  
```
 .------..------..------..------..------..------..------..------..------.
 |P.--. ||H.--. ||0.--. ||E.--. ||N.--. ||I.--. ||X.--. ||V.--. ||3.--. |
 | :/\: || :/\: || :/\: || (\/) || :(): || (\/) || :/\: || :(): || :/\: |
 | (__) || (__) || :\/: || :\/: || ()() || :\/: || (__) || ()() || (__) |
 | "--"P|| "--"H|| "--"0|| "--"E|| "--"N|| "--"I|| "--"X|| "--"V|| "--"3|
 `------'`------'`------'`------'`------'`------'`------'`------'`------'

 Authors: 
	4xx404			 https://github.com/4xx404

 Contributors: 
	jcalabres		 https://github.com/jcalabres
	Kf637			 https://github.com/Kf637

 Version: 2.0

 ✅ Searching for test143

 | Website ID: fd7e471d9e5696ea083f10720f169311
 | Website: About
 | Status: Not Found
 | Location: https://about.me/test143

 | Website ID: d0b51e9846050f97b0902d6f4865fe52
 | Website: Angel
 | Status: Not Found
 | Location: https://www.angel.co/test143

 | Website ID: dae50a9a8aebec46afe1a0966d0813f5
 | Website: Badoo
 | Status: Not Found
 | Location: https://www.badoo.com/en/test143

 | Website ID: c8a97defb11394de186baef0f875eb91
 | Website: Bandcamp
 | Status: Not Found
 | Location: https://www.bandcamp.com/test143

 | Website ID: cae73846b22537e6c40c0d4c8b5fe5e3
 | Website: Basecamphq
 | Status: Not Found
 | Location: https://test143.basecamphq.com/Login

 | Website ID: a99d1d69583c41c94a3582969decc21f
 | Website: Behance
 | Status: Match Found
 | Location: https://www.behance.net/test143

 | Website ID: 3b06adaccec858239426bbced386dfef
 | Website: Bitbucket
 | Status: Match Found
 | Location: https://bitbucket.org/test143

 | Website ID: 8df8939b53642963029ea621c1db84de
 | Website: Blip
 | Status: Not Found
 | Location: https://blip.fm/test143

 | Website ID: db896369ba07e55c5ee571c67b76c422
 | Website: Buzzfeed
 | Status: Not Found
 | Location: https://buzzfeed.com/test143

 | Website ID: 776828efa2737f017d05c533df1f8041
 | Website: Canva
 | Status: Not Found
 | Location: https://www.canva.com/test143

 | Website ID: f7041171cbc2b92e585f4b6e3c11e776
 | Website: Cash
 | Status: Not Found
 | Location: https://cash.me/test143

 | Website ID: b97a5a2add70a4d6b24de035452ebe84
 | Website: Codeacademy
 | Status: Not Found
 | Location: https://www.codeacademy.com/test143

 | Website ID: b625d79d1f51ba22509033eb2f2c7844
 | Website: Creativemarket
 | Status: Not Found
 | Location: https://creativemarket.com/test143

 ...
```
