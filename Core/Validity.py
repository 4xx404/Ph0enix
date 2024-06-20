#!/usr/bin/python3
import sys, re
sys.dont_write_bytecode = True

class Validation:
    def __init__(self):
        self.EmailRegex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        self.PhoneNumberRegex = r"^\(*\+*[1-9]{0,3}\)*-*[1-9]{0,3}[-. /]*\(*[2-9]\d{2}\)*[-. /]*\d{3}[-. /]*\d{4} *e*x*t*\.* *\d{0,4}$"

        self.DomainExtensions: list = [".com", ".net", ".edu", ".org", ".gov", ".int", ".mil", ".aero", ".cat", ".asia", ".mobi", ".coop", ".travel", ".tel", ".jobs", ".pro", ".biz", ".info", ".store", ".me", ".co", ".online", ".xyz", ".site", ".club", ".shop", ".app", ".live", ".ac", ".ad", ".ae", ".af", ".ag", ".ai", ".al", ".am", ".an", ".ao", ".aq", ".ar", ".as", ".at", ".au", ".aw", ".ax", ".az", ".ba", ".bb", ".bd", ".be", ".bf", ".bg", ".bh", ".bi", ".bj", ".bl", ".bm", ".bn", ".bo", ".br", ".bq", ".bs", ".bt", ".bv", ".bw", ".by", ".bz", ".ca", ".cc", ".cd", ".cf", ".cg", ".ch", ".ci", ".ck", ".cl", ".cm", ".cn", ".co", ".cr", ".cs", ".cu", ".cv", ".cw", ".cx", ".cy", ".cz", ".dd", ".de", ".dj", ".dk", ".dm", ".do", ".dz", ".ec", ".ee", ".eg", ".eh", ".er", ".es", ".et", ".eu", ".fi", ".fj", ".fk", ".fm", ".fo", ".fr", ".ga", ".gb", ".gd", ".ge", ".gf", ".gg", ".gh", ".gi", ".gl", ".gm", ".gn", ".gp", ".gq", ".gr", ".gs", ".gt", ".gu", ".gw", ".gy", ".hk", ".hm", ".hn", ".hr", ".ht", ".hu", ".id", ".ie", ".il", ".im", ".in", ".io", ".iq", ".ir", ".is", ".it", ".je", ".jm", ".jo", ".jp", ".ke", ".kg", ".kh", ".ki", ".km", ".kn", ".kp", ".kr", ".kw", ".ky", ".kz", ".la", ".lb", ".lc", ".li", ".lk", ".lr", ".ls", ".lt", ".lu", ".lv", ".ly", ".ma", ".mc", ".me", ".mf", ".mg", ".mh", ".mk", ".ml", ".mm", ".mn", ".mo", ".mp", ".mq", ".mr", ".ms", ".mt", ".mu", ".mv", ".mw", ".mx", ".my", ".mz", ".na", ".nc", ".ne", ".nf", ".ng", ".ni", ".nl", ".no", ".np", ".nr", ".nu", ".nz", ".om", ".pa", ".pe", ".pf", ".pg", ".ph", ".pk", ".pm", ".pn", ".pr", ".ps", ".pt", ".pw", ".qa", ".re", ".ro", ".rs", ".ru", ".rw", ".sa", ".sb", ".sc", ".sd", ".se", ".sg", ".si", ".sj", ".sk", ".sl", ".sm", ".sn", ".so", ".sr", ".ss", ".st", ".su", ".sv", ".sx", ".sy", ".sz", ".tc", ".td", ".tf", ".tg", ".th", ".tj", ".tk", ".tl", ".tm", ".tn", ".to", ".tp", ".tr", ".tt", ".tv", ".tw", ".tz", ".ua", ".ug", ".uk", ".um", ".us", ".uy", ".uz", ".va", ".vc", ".ve", ".vg", ".vi", ".vn", ".vu", ".wf", ".ws", ".ye", ".yt", ".yu", ".za", ".zm", ".zr", ".zw"]

    def NotEmpty(self, Object: str or list or dict = None) -> bool: # type: ignore
        if(Object != None):
            if(type(Object) == str and Object.strip() != ""):
                return True
            elif(type(Object) == list and len(Object) > 0):
                return True
            elif(type(Object) == dict and len(Object.keys()) > 0):
                return True
            
        return False

    def HasProtocol(self, Link: str = None) -> bool:
        return (self.NotEmpty(Link) and Link.startswith(("http://", "https://")))

    def HasDomainExtension(self, Link: str = None) -> bool:
        if(self.NotEmpty(Link)):
            InLinkCount: int = 0

            for Extension in self.DomainExtensions:
                if(Extension in Link):
                    InLinkCount += 1
            
            if(InLinkCount > 0):
                return True
        
        return False
        
    def StartsOrEndsWith(self, TrailType: str = None, StringValue: str = None, CharacterToCheck: str = None) -> bool:
        if(self.NotEmpty(TrailType) and self.NotEmpty(StringValue) and self.NotEmpty(CharacterToCheck)):
            if(TrailType == "start" and StringValue.startswith(CharacterToCheck)):
                return True
            elif(TrailType == "end" and StringValue.endswith(CharacterToCheck)):
                return True
    
        return False

    def IsEmailFormat(self, Email: str = None) -> bool:
        if(self.NotEmpty(Email) and re.fullmatch(self.EmailRegex, Email)):
            return True

        return False

    def IsPhoneNumberFormat(self, PhoneNumber: str = None) -> bool:
        if(self.NotEmpty(PhoneNumber)):
            if(not PhoneNumber.startswith("+")):
                PhoneNumber = f"+{PhoneNumber}"

            if(re.fullmatch(self.PhoneNumberRegex, PhoneNumber)):
                return True

        return False

    def IsLinkFormat(self, Link: str = None, IncludeDomainExtensionCheck: bool = False) -> bool:
        if(self.NotEmpty(Link) and self.HasProtocol(Link)):
            if(IncludeDomainExtensionCheck == False or (IncludeDomainExtensionCheck == True and self.HasDomainExtension(Link))):
                return True

        return False
    
    def ID(self, IDValue: str = None) -> bool:
        return (self.NotEmpty(IDValue) and len(IDValue) == 32)