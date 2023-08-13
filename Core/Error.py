from Core.Styling import *

from .Validity import Validation

class ErrorHandler:
    def __init__(self):
        self.Validator = Validation()

        self.DefinedErrors = [
            "empty_username_value",
            "username_length_too_short",
            "link_username_replacement_chunk_not_found",
            "none_200_response",
        ]

    def Throw(self, ErrorType: str = None, ErrorData: any = None):
        if(self.Validator.NotEmpty(ErrorType) and ErrorType.lower() in self.DefinedErrors):
            if(ErrorType == "empty_username_value"): return f"\n{sd.eBan} Username value cannot be empty\n"
            elif(ErrorType == "username_length_too_short"): return f"\n{sd.eBan} Invalid Username {bc.RC}{ErrorData}{bc.BC}, length must be 3 or more characters\n"
            elif(ErrorType == "link_username_replacement_chunk_not_found"): return f"\n{sd.eBan} Link {bc.RC}{ErrorData}{bc.BC} does not include {bc.RC}\"[USER]\"{bc.BC} to replace the username\n"
            elif(ErrorType == "none_200_response"): return f"\n{sd.eBan} Got no response from {bc.RC}{ErrorData}{bc.BC}\n"
        else:
            if(ErrorType == None): return f"\n{sd.eBan} Error Type cannot be None\n"    
            else: return f"\n{sd.eBan} Undefined Error Type {bc.RC}{ErrorType}{bc.BC}\n"
