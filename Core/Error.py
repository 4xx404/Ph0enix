from Core.Styling.Banners import sd
eBan = sd.eBan
from Core.Styling.Colors import bc

class ErrorHandler:
    def __init__(self):
        self.DefinedErrors = [
            "empty_username_value",
            "build_links_failed",
            "link_username_replacement_chunk_not_found",
            "none_200_response",
        ]

    def Throw(self, ErrorType, ErrorData):
        self.ErrorType = ErrorType.lower()
        self.ErrorData = ErrorData

        if(self.ErrorType in self.DefinedErrors):
            if(self.ErrorType == "empty_username_value"):
                return f"\n{eBan} Username value cannot be empty\n"

            elif(self.ErrorType == "build_links_failed"):
                return f"\n{eBan} Failed to build link list\n"
            elif(self.ErrorType == "link_username_replacement_chunk_not_found"):
                return f"\n{eBan} Link {bc.RC}{self.ErrorData}{bc.BC} does not include {bc.RC}\"[USER]\"{bc.BC} to replace the username\n"

            elif(self.ErrorType == "none_200_response"):
                return f"\n{eBan} Got no response from {bc.RC}{self.ErrorData}{bc.BC}\n"       

        else:
            return f"\n{eBan} Undefined Error Type\n"
