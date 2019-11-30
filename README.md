# Ph30n1x

A search tool for finding usernames across a variety of sites.

# How it works?

The tool reads a file named urls.txt.

For every url inside the file, the tool will find for username matches.

# Usage

```
git clone https://github.com/Bl1xY/Ph30n1x.git
cd Ph30n1x
python ph30n1x.py <username> <textfile>
```

# Adding URL's

Open the urls.txt file and put the new URL with the next format:

```
site:url
```

Be sure to put "[USER]" inside the url to make the tool work properly.

# Example

```
python ph30n1x.py example456

+[+[+[ Ph03n1x v1.0 ]+]+]+
 __       ___   ___
[  ] [       ] [   ]      /|
[__] [__   __] [   ] ,__   |  \ /
[    [  ]    ] [   ] [  ]  |   :
[    [  ] ___] [___] [  ) _|_ / \
+[+[+[ Searching for username: example456 ]+]+]+
+[+[+[ Ph30n1x v1 is working... ]+]+]+

MATCH: example456 in ifttt:https://www.ifttt.com/p/example456
MATCH: example456 in instagram:https://www.instagram.com/example456
MATCH: example456 in twitter:https://www.twitter.com/example456
MATCH: example456 in tumblr:https://example456.tumblr.com
MATCH: example456 in scribd:https://www.scribd.com/example456
MATCH: example456 in spotify:https://open.spotify.com/user/example456
MATCH: example456 in pinterest:https://www.pinterest.com/example456
MATCH: example456 in wordpress:https://example456.wordpress.com
MATCH: example456 in slack:https://example456.slack.com
MATCH: example456 in gravatar:https://en.gravatar.com/example456
MATCH: example456 in deviantart:https://example456.deviantart.com
MATCH: example456 in reddit:https://www.reddit.com/user/example456
MATCH: example456 in flipboard:https://flipboard.com/@/example456
MATCH: example456 in facebook:https://www.twitter.com/example456
MATCH: example456 in canva:https://www.canva.com/example456
MATCH: example456 in bitbucket:https://bitbucket.org/example456
MATCH: example456 in github:https://github.com/example456
MATCH: example456 in google_plus:https://plus.google.com/s/example456/top
MATCH: example456 in ebay:https://www.ebay.com/usr/example456
MATCH: example456 in blogspot:https://example456.blogspot.com
MATCH: example456 in mixcloud:https://www.mixcloud.com/example456
MATCH: example456 in steam:https://steamcommunity.com/id/example456
FINISHED: A total of 22 MATCHES found out of 71 websites.
```
