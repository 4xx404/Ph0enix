from .Styling import *

from .Commands import Command
from .Error import ErrorHandler
from .Validity import Validation

class InputManager:
    def __init__(self):
        self.Cmd = Command()
        self.Error = ErrorHandler()
        self.Validator = Validation()

    def SetUsername(self):
        Username = str(input(f"{bc.BC} Username:{bc.GC} "))

        if(self.Validator.NotEmpty(Username)):
            if(len(Username) >= 3):
                return Username
            else:
                self.Cmd.Clear(self.Error.Throw("username_length_too_short", Username), False)
                self.SetUsername()
        else:
            self.Cmd.Clear(self.Error.Throw("empty_username_value", None), False)
            self.SetUsername()
