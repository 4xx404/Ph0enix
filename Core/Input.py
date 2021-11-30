from .Styling.Colors import bc

from .Commands import Command
from .Error import ErrorHandler

class InputManager:
    def __init__(self):
        self.Cmd = Command()
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

    def SetUsername(self):
        self.Username: str = str(input(f"{bc.BC} Username:{bc.GC} "))

        if(self.NotEmpty(self.Username)):
            if(len(self.Username) > 1):
                return self.Username
            else:
                self.Cmd.Clear()
                print(self.Error.Throw("username_length_too_short", self.Username))
                self.SetUsername()
        else:
            self.Cmd.Clear()
            print(self.Error.Throw("empty_username_value", None))
            self.SetUsername()
