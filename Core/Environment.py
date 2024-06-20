import sys
from dotenv import dotenv_values

sys.dont_write_bytecode = True

from .Validity import Validation
from .Error import ErrorHandler

class Environment:
    def __init__(self) -> None:
        self.Validator = Validation()
        self.Error = ErrorHandler()

        self.Env = {}

        self.Load()

    def __FormatKey(self, Key: str = None) -> (str | None):
        if(self.Validator.NotEmpty(Key)):
            Key = Key.lower()

            if("_" in Key):
                KeyPieces = Key.split("_")

                Key = ""

                for KeyPiece in KeyPieces:
                    Key += KeyPiece.capitalize()
            else:
                Key = Key.capitalize()

            return Key

        return None

    def Load(self, EnvPath: str = ".env"):
        EnvironmentVariables = dotenv_values(EnvPath)

        if(len(EnvironmentVariables) > 0):
            for Key, Value in EnvironmentVariables.items():
                Key = self.__FormatKey(Key)

                if(self.Validator.NotEmpty(Key) and Key not in self.Env.keys()):
                    self.Env[Key] = Value

            if(not self.Validator.NotEmpty(self.Env)):
                self.Env = None
        else:
            self.Error.Throw("environment_load", "Could not load environment files")
            self.Error.AddToLog("error", "Could not load environment variables")

            quit()