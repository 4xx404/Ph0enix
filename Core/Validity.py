from typing import List
from tld import get_tld

from Core.Config import CoreConfig
from Core.Error import ErrorHandler

class Validation:
    def __init__(self):
        self.Config = CoreConfig()
        self.Error = ErrorHandler()

    def GetWebsiteName(self, Link):
        self.Link = Link
        self.Site = get_tld(self.Link, as_object=True).domain.title()

        if(self.Site == "Steamcommunity"):
            self.Site = "Steam"
        else:
            self.Site = self.Site
        
        return self.Site

    def LinkFormatter(self, Username: str):
        self.Username: str = Username
        self.Links: list = self.Config.SitePack

        self.Response: list = []
        for self.Link in self.Links:
            if("[USER]" in self.Link):
                self.Response.append(self.Link.split(":", 1)[1].replace("[USER]", self.Username))
            else:
                print(self.Error.Throw("link_username_replacement_chunk_not_found", self.Username))

        return self.Response
