import requests

from Core.Config import CoreConfig
from Core.Error import ErrorHandler

class RequestHandler:
    def __init__(self):
        self.Error = ErrorHandler()
        self.Config = CoreConfig()

    def IsLive(self, Link):
        self.Link = Link
        self.Request = requests.get(self.Link, headers=self.Config.Headers)

        if(self.Request.status_code == 200):
            return True
        else:
            return False

    def Search(self, Link, Username):
        self.Link = Link
        self.Username = Username

        if(self.IsLive(self.Link)):
            for FailWord in self.Config.FailWords:
                if(self.Username in self.Request.text.lower() and not FailWord in self.Request.text.lower()):
                    return True
                else:
                    continue

            return False

        else:
            return False
