# -*- coding: utf-8 -*-
import sys
sys.dont_write_bytecode = True

from Core.Styling import *

from Core.Config import CoreConfig
from Core.Commands import Command
from Core.Input import InputManager
from Core.Validity import Validation
from Core.Requester import RequestHandler
from Core.Error import ErrorHandler

class Ph0enix:
	def __init__(self):
		self.Config = CoreConfig()
		self.Cmd = Command()
		self.Validator = Validation()
		self.Request = RequestHandler()
		self.Error = ErrorHandler()

	def BuildLinks(self, Username: str = None) -> (list | None):
		BuiltLinks = self.Request.LinkFormatter(Username)
		
		if(len(BuiltLinks) > 0):
			return BuiltLinks

		self.Cmd.Clear(f"{sd.eBan} No data found", False)
		Initiate(True)

	def StartSearch(self, Username: str = None, FormattedLinks: list = []) -> list:
		self.Cmd.Clear(f"{sd.sBan}Searching for {bc.GC}{Username}{bc.BC}\n", False)

		Matches = []

		for Link in FormattedLinks:
			WebsiteName = self.Request.GetWebsiteName(Link)

			if(self.Validator.NotEmpty(WebsiteName)):
				IsInSite = self.Request.Search(Link)

				if(IsInSite):
					Matches.append(Link)

					StatusBanner = f"{bc.GC}Match Found{bc.BC}"
				else:
					StatusBanner = f"{bc.RC}Not Found{bc.BC}"
				
				print(f" | Website: {bc.GC}{WebsiteName}{bc.BC}\n | Status: {StatusBanner}\n | Location: {bc.GC}{Link}{bc.BC}\n")

		return Matches

	def PrintResults(self, SearchResults: list = [], TotalLinkCount: int = 0) -> None:
		FoundCount = 0

		if(self.Validator.NotEmpty(SearchResults)):
			FoundCount = len(SearchResults)

		self.Cmd.Clear(f"{sd.sBan}Found {bc.GC}{str(FoundCount)}{bc.BC} potential matches out of {bc.GC}{TotalLinkCount}{bc.BC} websites\n", False)

		for Match in SearchResults:
			print(f" | Website: {bc.GC}{self.Request.GetWebsiteName(Match)}{bc.BC} \n | Location: {bc.GC}{Match}{bc.BC}\n")

		Initiate(True)

if(__name__ == "__main__"):
	def Intro():
		print(f"{sd.iBan} Matches may not always be specific to the user you are looking for")
		print(f"{sd.iBan} For example, someone else could have used the same username elsewhere\n")

	def Initiate(SeenIntro: bool = False):
		try:
			Run = Ph0enix()

			if(not SeenIntro):
				Intro()

			Username = InputManager().SetUsername()

			WebsiteLinks = Run.BuildLinks(Username)
			SearchResults = Run.StartSearch(Username, WebsiteLinks)

			Run.PrintResults(SearchResults, len(WebsiteLinks))
		except KeyboardInterrupt:
			quit()

	Command().Clear()
	Initiate(False)
