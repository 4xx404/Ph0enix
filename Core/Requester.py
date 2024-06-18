import sys, requests, tld
sys.dont_write_bytecode = True

from .Config import CoreConfig
from .Commands import Command
from .Error import ErrorHandler
from .Validity import Validation

class RequestHandler:
    def __init__(self):
        self.Cmd = Command()
        self.Error = ErrorHandler()
        self.Config = CoreConfig()
        self.Validator = Validation()

    def LinkFormatter(self, Username: str):
        Response = []

        for Link in self.Config.SitePack:
            if("[USER]" in Link):
                Response.append(Link.split(":", 1)[1].replace("[USER]", Username))
            else:
                print(self.Error.Throw("link_username_replacement_chunk_not_found", Username))

        return Response

    def IsLive(self, Link: str):
        if(self.Validator.IsLinkFormat(Link)):
            try:
                Request = requests.get(Link, headers=self.Config.Headers, allow_redirects=True)

                if(Request.status_code == 200): return True
            except Exception:
                pass

        return False
    
    def GetWebsiteName(self, Link: str) -> (str | None):
        if(self.Validator.IsLinkFormat(Link)):
            Site = tld.get_tld(Link, as_object=True).domain.title()

            if(Site.lower() == "steamcommunity"):
                Site = "Steam"
            
            return Site

        return None

    def Search(self, Link: str):
        if(self.IsLive(Link)):
            for FailWord in self.Config.FailWords:
                Request = requests.get(url=Link, headers=self.Config.Headers, allow_redirects=True)
                
                if(FailWord in Request.text.lower() or Request.status_code == 404):
                    return False
            
            return True

        return False