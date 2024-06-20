#!/usr/bin/python3
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

    def LinkFormatter(self, Username: str = None) -> list:
        Response = []

        if(self.Validator.NotEmpty(Username)):
            for Link in self.Config.SitePack:
                if("[USER]" in Link):
                    Response.append(Link.split(":", 1)[1].replace("[USER]", Username))
                else:
                    print(self.Error.Throw("link_username_replacement_chunk_not_found", Username))

        return Response

    def IsLive(self, Link: str) -> bool:
        if(self.Validator.IsLinkFormat(Link)):
            self.Error.AddToLog("info", f"Requesting '{Link}'")

            try:
                Request = requests.get(Link, headers=self.Config.Headers, allow_redirects=True, timeout=5)

                if(Request.status_code == 200):
                    return True
            except requests.exceptions.Timeout:
                self.Error.AddToLog("error", f"Timeout occurred while live checking '{Link}'")
            except Exception:
                self.Error.AddToLog("error", f"Failed to live check '{Link}'")

        return False
    
    def GetWebsiteName(self, Link: str) -> (str | None):
        if(self.Validator.IsLinkFormat(Link)):
            Site = tld.get_tld(Link, as_object=True).domain.title()

            if(Site.lower() == "steamcommunity"):
                Site = "Steam"
            
            return Site

        return None

    def Search(self, Link: str) -> bool:
        if(self.IsLive(Link)):
            try:
                Request = requests.get(url=Link, headers=self.Config.Headers, allow_redirects=True, timeout=5)

                if(Request.status_code == 404):
                    return False
                
                for FailWord in self.Config.FailWords:    
                    if(FailWord in Request.text.lower()):
                        self.Error.AddToLog("info", f"FailWord '{FailWord}' found in '{Link}' response text")

                        return False
                
                return True
            except requests.exceptions.Timeout:
                self.Error.AddToLog("error", f"Timeout occurred while requesting '{Link}'")
            except Exception:
                self.Error.AddToLog("error", f"Failed to request '{Link}'")

        return False