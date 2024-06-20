#!/usr/bin/python3
import sys
sys.dont_write_bytecode = True

from .Styling import *

from .Commands import Command
from .Error import ErrorHandler
from .Validity import Validation

class InputManager:
    def __init__(self):
        self.Cmd = Command()
        self.Error = ErrorHandler()
        self.Validator = Validation()

        self.Commands = {
            "database_manager": f"Use {bc.GC}database{bc.BC} to enter the database interface",
        }

    def Help(self) -> None:
        HelpCounter = 0

        for Category, Description in self.Commands.items():
            if("_" in Category):
                CategoryPieces = Category.split("_")

                Category, CategoryCounter = "", 0

                for CategoryPiece in CategoryPieces:
                    Category += CategoryPiece.capitalize()

                    if(CategoryCounter < len(CategoryPieces) - 1):
                        Category += " "
                    
                    CategoryCounter += 1
                
            else:
                Category = Category.capitalize()
                        
            print(f" {bc.BC}{Category}\t{Description}")

            if(HelpCounter == len(self.Commands.keys()) - 1):
                print()

            HelpCounter += 1