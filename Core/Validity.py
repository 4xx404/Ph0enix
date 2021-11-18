from tld import get_tld

from Core.Config import CoreConfig
from Core.Error import ErrorHandler

class Validation:
    def __init__(self):
        self.Config = CoreConfig()
        self.Error = ErrorHandler()

    def NotEmpty(self, Object):
        self.Object = Object

        if(type(self.Object) == list):
            if(len(self.Object) > 0):
                return True
            else:
                return False
        elif(type(self.Object) == str):
            if(self.Object != "" or self.Object != " "):
                return True
            else:
                return False

    def GetWebsiteName(self, Link):
        self.Link = Link
        self.WebsiteName = get_tld(self.Link, as_object=True)

        self.Site = self.WebsiteName.domain.title()
        if(self.Site == "Steamcommunity"):
            self.Site = "Steam"
        else:
            self.Site = self.Site
        
        return self.Site

    def LinkFormatter(self, Username):
        self.ResponsePack = {
            "success": True,
            "data": []
        }

        if(self.NotEmpty(Username)):
            self.Username = Username
        else:
            self.ResponsePack["success"] = False
            self.ResponsePack["data"].append(self.Error.Throw("empty_username_value", None))

        self.Links = self.Config.LinkList
        for self.Link in self.Links:
            if("[USER]" in self.Link):
                self.ResponsePack["data"].append(self.Link.split(":", 1)[1].replace("[USER]", self.Username))
            else:
                self.ResponsePack["success"] = False
                self.ResponsePack["data"].append(self.Error.Throw("link_username_replacement_chunk_not_found", self.Username))
                return self.ResponsePack

        return self.ResponsePack
