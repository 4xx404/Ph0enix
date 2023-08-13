#!/usr/bin/python3
import sys, os, time
sys.dont_write_bytecode = True
from tld import get_tld

from Core.Styling import *

from .Validity import Validation

class Command:
    def __init__(self):
        self.Validator = Validation()

        self.Logo: str = sd.Logo

    def Clear(self, Message: str = None, ShouldQuit: bool = False):
        self.Message: str = Message
        self.ShouldQuit: bool = ShouldQuit

        if(self.Message != None and self.ShouldQuit == False):
            os.system("clear")
            print(self.Logo)
            print(self.Message)
        elif(self.Message == None and self.ShouldQuit == True):
            os.system("clear")
            print(self.Logo)
            quit()
        elif(self.Message != None and self.ShouldQuit == True):
            os.system("clear")
            print(self.Logo)
            print(self.Message)
            quit()
        else:
            # Message: None, ShouldQuit: False
            os.system("clear")
            print(self.Logo)

    def MoveFile(self, FileToMove: str, Destination: str, QuitOnInterrupt = True):
        self.FileToMove: str = FileToMove
        self.Destination: str = Destination

        print(f"{sd.iBan} Moving {bc.GC}{self.FileToMove}{bc.BC} to {bc.GC}{self.Destination}{bc.BC}")
        time.sleep(0.5)

        try:
            os.system(f"sudo mv {self.FileToMove} {self.Destination}")
        except Exception as e:
            self.Clear(f"Unable to move file from {bc.RC}{self.FileToMove}{bc.BC} to {bc.GC}{self.Destination}{bc.BC}\n {bc.RC}{e}\n\n Aborted...{bc.BC}", True)
        except KeyboardInterrupt:
            if(QuitOnInterrupt == True):
                self.Clear(" Quitting...", QuitOnInterrupt)
            else:
                self.Clear(None, QuitOnInterrupt)

        return True

    def MakeDirectory(self, DirectoryPath: str, ReturnBoolNotError: bool = True):
        self.DirectoryPath: str = DirectoryPath

        try:
            os.mkdir(self.DirectoryPath)
        except Exception:
            if(ReturnBoolNotError == True):
                return False
            else:
                self.Clear(f"Unable to make directory '{self.DirectoryPath}'", True)

        return True

    def ListDirectory(self, DirectoryToView: str):
        self.DirectoryToView: str = DirectoryToView

        try:
            os.listdir(self.DirectoryToView)
        except Exception:
            self.Clear(f"Could not get content of '{self.DirectoryToView}'", True)

        return True

    def ChangeDirectory(self, DirectoryToMoveTo: str):
        self.DirectoryToMoveTo: str = DirectoryToMoveTo

        try:
            os.chdir(self.DirectoryToMoveTo)
        except Exception:
            self.Clear(f"Unable to change directory to '{self.DirectoryToMoveTo}'", True)

        return False

    def RenameFileOrDirectory(self, FileOrDirectoryName: str, NewFileOrDirectoryName: str):
        self.FileOrDirectoryName: str = FileOrDirectoryName
        self.NewFileOrDirectoryName: str = NewFileOrDirectoryName

        try:
            os.rename(self.FileOrDirectoryName, self.NewFileOrDirectoryName)
        except Exception:
            self.Clear(f"Unable to rename file/directory from '{self.FileOrDirectoryName}' to '{self.NewFileOrDirectoryName}'", True)
        
        return True

    def RemoveDirectory(self, DirectoryToDelete: str):
        self.DirectoryToDelete: str = DirectoryToDelete

        try:
            os.rmdir(self.DirectoryToDelete)
        except Exception:
            self.Clear(f"Unable to remove directory '{self.DirectoryToDelete}'", True)

        return True
    
    def FileExists(self, FilePath = None):
        if(FilePath != None and os.path.isfile(FilePath)):
            return True
        else:
            return False
        
    def DirectoryExists(self, DirPath = None):
        if(DirPath != None and os.path.isdir(DirPath)):
            return True
        else:
            return False
    
    def GetFLD(self, Link: str = None):
        if(Link != None):
            Tld = get_tld(Link, as_object=True)

            if(Tld != None and Tld.fld != None):
                return Tld.fld

        return None