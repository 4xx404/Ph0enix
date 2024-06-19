#!/usr/bin/python3
import sys, platform, os
sys.dont_write_bytecode = True
from tld import get_tld

from Core.Styling import *

from .Validity import Validation

class Command:
    def __init__(self):
        self.Validator = Validation()

        self.Logo: str = sd.Logo

        self.CommandMatrix = {
            "windows": {
                "clear": "cls"
            },

            "linux": {
                "clear": "clear"
            },
            
            "darwin": {
                "clear": "clear"
            }
        }

    def GetOS(self) -> str:
        return platform.system().lower()

    def Clear(self, Message: str = None, ShouldQuit: bool = False) -> None:
        Platform = self.GetOS()

        os.system(self.CommandMatrix[Platform]["clear"])
    
        print(self.Logo)
    
        if(self.Validator.NotEmpty(Message)):
            print(Message)
    
        if(ShouldQuit):
            quit()
    
    def GetFLD(self, Link: str = None) -> (str | None):
        if(self.Validator.NotEmpty(Link)):
            Tld = get_tld(Link, as_object=True)

            if(self.Validator.NotEmpty(Tld) and self.Validator.NotEmpty(Tld.fld)):
                return str(Tld.fld)

        return None