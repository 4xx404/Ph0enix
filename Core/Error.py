from Core.Styling.Banners import sd
from Core.Styling.Colors import bc

class ErrorHandler:
    def __init__(self):
        self.DefinedErrors = [
            "empty_username_value",
            "username_length_too_short",
            "link_username_replacement_chunk_not_found",
            "none_200_response",
        ]

    def Throw(self, ErrorType, ErrorData):
        self.ErrorType = ErrorType.lower()
        self.ErrorData = ErrorData

        if(self.ErrorType in self.DefinedErrors):
            if(self.ErrorType == "empty_username_value"):
                return f"\n{sd.eBan} Username value cannot be empty\n"
            elif(self.ErrorType == "username_length_too_short"):
                return f"\n{sd.eBan} Invalid Username {bc.RC}{self.ErrorData}{bc.BC}, length must be more than 1\n"

            elif(self.ErrorType == "link_username_replacement_chunk_not_found"):
                return f"\n{sd.eBan} Link {bc.RC}{self.ErrorData}{bc.BC} does not include {bc.RC}\"[USER]\"{bc.BC} to replace the username\n"

            elif(self.ErrorType == "none_200_response"):
                return f"\n{sd.eBan} Got no response from {bc.RC}{self.ErrorData}{bc.BC}\n"       

        else:
            return f"\n{sd.eBan} Undefined Error Type {bc.RC}{self.ErrorType}{bc.BC}\n"
