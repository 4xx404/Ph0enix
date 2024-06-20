#!/usr/bin/python3
import sys, random, string, hashlib, datetime
sys.dont_write_bytecode = True

from .Styling import *

class CoreConfig:
    def __init__(self):
        self.AppName = "Ph0enix"

        # Domain Extensions List (Used in Validation)
        self.DomainExtensions = [".com", ".net", ".edu", ".org", ".gov", ".int", ".mil", ".aero", ".cat", ".asia", ".mobi", ".coop", ".travel", ".tel", ".jobs", ".pro", ".biz", ".info", ".store", ".me", ".co", ".online", ".xyz", ".site", ".club", ".shop", ".app", ".live", ".ac", ".ad", ".ae", ".af", ".ag", ".ai", ".al", ".am", ".an", ".ao", ".aq", ".ar", ".as", ".at", ".au", ".aw", ".ax", ".az", ".ba", ".bb", ".bd", ".be", ".bf", ".bg", ".bh", ".bi", ".bj", ".bl", ".bm", ".bn", ".bo", ".br", ".bq", ".bs", ".bt", ".bv", ".bw", ".by", ".bz", ".ca", ".cc", ".cd", ".cf", ".cg", ".ch", ".ci", ".ck", ".cl", ".cm", ".cn", ".co", ".cr", ".cs", ".cu", ".cv", ".cw", ".cx", ".cy", ".cz", ".dd", ".de", ".dj", ".dk", ".dm", ".do", ".dz", ".ec", ".ee", ".eg", ".eh", ".er", ".es", ".et", ".eu", ".fi", ".fj", ".fk", ".fm", ".fo", ".fr", ".ga", ".gb", ".gd", ".ge", ".gf", ".gg", ".gh", ".gi", ".gl", ".gm", ".gn", ".gp", ".gq", ".gr", ".gs", ".gt", ".gu", ".gw", ".gy", ".hk", ".hm", ".hn", ".hr", ".ht", ".hu", ".id", ".ie", ".il", ".im", ".in", ".io", ".iq", ".ir", ".is", ".it", ".je", ".jm", ".jo", ".jp", ".ke", ".kg", ".kh", ".ki", ".km", ".kn", ".kp", ".kr", ".kw", ".ky", ".kz", ".la", ".lb", ".lc", ".li", ".lk", ".lr", ".ls", ".lt", ".lu", ".lv", ".ly", ".ma", ".mc", ".me", ".mf", ".mg", ".mh", ".mk", ".ml", ".mm", ".mn", ".mo", ".mp", ".mq", ".mr", ".ms", ".mt", ".mu", ".mv", ".mw", ".mx", ".my", ".mz", ".na", ".nc", ".ne", ".nf", ".ng", ".ni", ".nl", ".no", ".np", ".nr", ".nu", ".nz", ".om", ".pa", ".pe", ".pf", ".pg", ".ph", ".pk", ".pm", ".pn", ".pr", ".ps", ".pt", ".pw", ".qa", ".re", ".ro", ".rs", ".ru", ".rw", ".sa", ".sb", ".sc", ".sd", ".se", ".sg", ".si", ".sj", ".sk", ".sl", ".sm", ".sn", ".so", ".sr", ".ss", ".st", ".su", ".sv", ".sx", ".sy", ".sz", ".tc", ".td", ".tf", ".tg", ".th", ".tj", ".tk", ".tl", ".tm", ".tn", ".to", ".tp", ".tr", ".tt", ".tv", ".tw", ".tz", ".ua", ".ug", ".uk", ".um", ".us", ".uy", ".uz", ".va", ".vc", ".ve", ".vg", ".vi", ".vn", ".vu", ".wf", ".ws", ".ye", ".yt", ".yu", ".za", ".zm", ".zr", ".zw"]

        # Fail Words (Indicators an account doesn"t exist)
        self.FailWords = ["oops", "sorry", "does not exist", "doesnt exist", "doesn't exist", "no user", "no profile", "page not found", "page cannot be found", "this page is no longer available", "no such user"]

        # Request Headers (Macintosh; Intel Mac OS X 10_15_7)
        self.Headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br"
        }
    
    def GetAppName(self, IncludePlaceholder: bool = False) -> str:
        if(IncludePlaceholder == True):
            return f"{bc.BC} App Name: {bc.GC}{self.AppName}{bc.BC}"
        
        return f"{bc.GC}{self.AppName}{bc.BC}"
    
    def GenerateID(self, Length: int = 0) -> str:
        if(Length <= 0):
            Length = 32

        return "".join(random.choices(string.ascii_lowercase, k=Length))

    def GenerateMD5(self, StringValue: str = None) -> str:
        if(StringValue == None):
            StringValue = self.GenerateID()

        return hashlib.md5(StringValue.encode("utf-8")).hexdigest()

    def UnixTimestamp(self):
        return int(round(datetime.datetime.timestamp(datetime.datetime.now()), 0))