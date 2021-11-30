class CoreConfig:
    def __init__(self):
        self.AppName = "Ph0enix"
        self.Version = "V3"
        self.SitePack = [
            "about_me:https://about.me/[USER]",
            "angel_list:https://www.angel.co/[USER]",
            "badoo:https://www.badoo.com/en/[USER]",
            "bandcamp:https://www.bandcamp.com/[USER]",
            "basecamp_HQ:https://[USER].basecamphq.com/Login",
            "behance:https://www.behance.net/[USER]",
            "bitbucket:https://bitbucket.org/[USER]",
            "blipfm:https://blip.fm/[USER]",
            "buzzfeed:https://buzzfeed.com/[USER]",
            "canva:https://www.canva.com/[USER]",
            "cashme:https://cash.me/[USER]",
            "codeacademy:https://www.codeacademy.com/[USER]",
            "contently:https://[USER].contently.com/",
            "creative_market:https://creativemarket.com/[USER]",
            "designspiration:https://www.designspiration.net/[USER]",
            "deviantart:https://[USER].deviantart.com/",
            "disqus:https://disqus.com/by/[USER]",
            "dribbble:https://www.dribbble.com/[USER]",
            "ebay:https://www.ebay.com/usr/[USER]",
            "ello:https://ello.co/[USER]",
            "etsy:https://www.etsy.com/shop/[USER]",
            "facebook:https://www.facebook.com/[USER]",
            "five_hundred_px:https://500px.com/[USER]",
            "flickr:https://www.flickr.com/people/[USER]",
            "fotolog:https://fotolog.com/[USER]",
            "github:https://github.com/[USER]",
            "goodreads:https://www.goodreads.com/[USER]",
            "gravatar:https://en.gravatar.com/[USER]",
            "gumroad:https://www.gumroad.com/[USER]",
            "houzz:https://houzz.com/user/[USER]",
            "hubpages:https://[USER].hubpages.com/",
            "imgur:https://imgur.com/user/[USER]",
            "instagram:https://www.instagram.com/[USER]",
            "instructables:https://www.instructables.com/member/[USER]",
            "keybase:https://www.keybase.io/[USER]",
            "kongregate:https://kongregate.com/accounts/[USER]",
            "last_fm:https://www.last.fm/user/[USER]",
            "livejournal:https://[USER].livejournal.com/",
            "medium:https://medium.com/@/[USER]",
            "mixcloud:https://www.mixcloud.com/[USER]",
            "okcupid:https://www.okcupid.com/profile/[USER]",
            "pastebin:https://pastebin.com/u/[USER]",
            "patreon:https://www.patreon.com/[USER]",
            "pinterest:https://www.pinterest.com/[USER]",
            "reddit:https://www.reddit.com/user/[USER]",
            "reverbnation:https://www.reverbnation.com/[USER]",
            "roblox:https://www.roblox.com/users/[USER]/profile/",
            "scribd:https://www.scribd.com/[USER]",
            "skyscanner:https://www.trip.skyscanner.com/user/[USER]",
            "slack:https://[USER].slack.com/",
            "slideshare:https://slideshare.net/[USER]",
            "soundcloud:https://soundcloud.com/[USER]",
            "spotify:https://open.spotify.com/user/[USER]",
            "steam:https://steamcommunity.com/id/[USER]",
            "trakt:https://www.trakt.tv/users/[USER]",
            "trip_advisor:https://tripadvisor.com/members/[USER]",
            "tumblr:https://[USER].tumblr.com/",
            "twitter:https://www.twitter.com/[USER]",
            "vk:https://vk.com/[USER]",
            "wattpad:https://www.wattpad.com/user/[USER]",
            "wikipedia:https://www.wikipedia.org/wiki/User:[USER]",
            "ycombinator:https://news.ycombinator.com/user?id=[USER]",
            "youtube:https://www.youtube.com/c/[USER]"
        ]

        # Domain Extensions List (Used in Validation)
        self.DomainExtensions = [".com", ".net", ".edu", ".org", ".gov", ".int", ".mil", ".aero", ".cat", ".asia", ".mobi", ".coop", ".travel", ".tel", ".jobs", ".pro", ".biz", ".info", ".store", ".me", ".co", ".online", ".xyz", ".site", ".club", ".shop", ".app", ".live", ".ac", ".ad", ".ae", ".af", ".ag", ".ai", ".al", ".am", ".an", ".ao", ".aq", ".ar", ".as", ".at", ".au", ".aw", ".ax", ".az", ".ba", ".bb", ".bd", ".be", ".bf", ".bg", ".bh", ".bi", ".bj", ".bl", ".bm", ".bn", ".bo", ".br", ".bq", ".bs", ".bt", ".bv", ".bw", ".by", ".bz", ".ca", ".cc", ".cd", ".cf", ".cg", ".ch", ".ci", ".ck", ".cl", ".cm", ".cn", ".co", ".cr", ".cs", ".cu", ".cv", ".cw", ".cx", ".cy", ".cz", ".dd", ".de", ".dj", ".dk", ".dm", ".do", ".dz", ".ec", ".ee", ".eg", ".eh", ".er", ".es", ".et", ".eu", ".fi", ".fj", ".fk", ".fm", ".fo", ".fr", ".ga", ".gb", ".gd", ".ge", ".gf", ".gg", ".gh", ".gi", ".gl", ".gm", ".gn", ".gp", ".gq", ".gr", ".gs", ".gt", ".gu", ".gw", ".gy", ".hk", ".hm", ".hn", ".hr", ".ht", ".hu", ".id", ".ie", ".il", ".im", ".in", ".io", ".iq", ".ir", ".is", ".it", ".je", ".jm", ".jo", ".jp", ".ke", ".kg", ".kh", ".ki", ".km", ".kn", ".kp", ".kr", ".kw", ".ky", ".kz", ".la", ".lb", ".lc", ".li", ".lk", ".lr", ".ls", ".lt", ".lu", ".lv", ".ly", ".ma", ".mc", ".me", ".mf", ".mg", ".mh", ".mk", ".ml", ".mm", ".mn", ".mo", ".mp", ".mq", ".mr", ".ms", ".mt", ".mu", ".mv", ".mw", ".mx", ".my", ".mz", ".na", ".nc", ".ne", ".nf", ".ng", ".ni", ".nl", ".no", ".np", ".nr", ".nu", ".nz", ".om", ".pa", ".pe", ".pf", ".pg", ".ph", ".pk", ".pm", ".pn", ".pr", ".ps", ".pt", ".pw", ".qa", ".re", ".ro", ".rs", ".ru", ".rw", ".sa", ".sb", ".sc", ".sd", ".se", ".sg", ".si", ".sj", ".sk", ".sl", ".sm", ".sn", ".so", ".sr", ".ss", ".st", ".su", ".sv", ".sx", ".sy", ".sz", ".tc", ".td", ".tf", ".tg", ".th", ".tj", ".tk", ".tl", ".tm", ".tn", ".to", ".tp", ".tr", ".tt", ".tv", ".tw", ".tz", ".ua", ".ug", ".uk", ".um", ".us", ".uy", ".uz", ".va", ".vc", ".ve", ".vg", ".vi", ".vn", ".vu", ".wf", ".ws", ".ye", ".yt", ".yu", ".za", ".zm", ".zr", ".zw"]

        # Fail Words (Indicators an account doesn"t exist)
        self.FailWords = [
            "oops",
            "sorry",
            "does not exist",
            "doesnt exist",
            "doesn't exist",
            "no user",
            "no profile",
            "page not found"
        ]

        # Request Headers (sent with every request)
        self.Headers = {
            "Accept-Language": "en-US,en;q=0.5",
            "Cache-Control": "no-cache",
            "User-Agent": f"{self.AppName}.{self.Version}"
        }
