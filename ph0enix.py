# -*- coding: utf-8 -*-
import sys
sys.dont_write_bytecode = True

from Core.Styling.Banners import sd
from Core.Styling.Colors import bc

from Core.Config import CoreConfig
from Core.Commands import Command
from Core.Input import InputManager
from Core.Validity import Validation
from Core.Requester import RequestHandler
from Core.Error import ErrorHandler

class Ph0enix:
	def __init__(self) -> None:
		self.Config = CoreConfig()
		self.Cmd = Command()
		self.Validator = Validation()
		self.Request = RequestHandler()
		self.Error = ErrorHandler()

	def BuildLinks(self, Username: str):
		self.Username:str = Username

		self.BuiltLinks = self.Validator.LinkFormatter(self.Username)
		if(len(self.BuiltLinks) > 0):
			return self.BuiltLinks
		else:
			self.Cmd.Clear()
			print(f"{sd.eBan} No data found")
			Initiate()

	def StartSearch(self, Username, FormattedLinks: list):
		self.Username = Username
		self.Links: list = FormattedLinks

		self.FoundCount = 0
		self.Matches = []

		print(f"{sd.sBan} Searching for {bc.GC}{Username}{bc.BC}\n")
		for self.Link in self.Links:
			self.Website = self.Validator.GetWebsiteName(self.Link)
			self.IsInSite = self.Request.Search(self.Link, self.Username)

			if(self.IsInSite):
				self.FoundCount += 1
				self.Matches.append(self.Link)
				print(f" | Website: {bc.GC}{self.Website}{bc.BC}\n | Status: {bc.GC}Match Found{bc.BC}\n | Location: {bc.GC}{self.Link}{bc.BC}\n")
			else:
				print(f" | Website: {bc.RC}{self.Website}{bc.BC}\n | Status: {bc.RC}Not Found{bc.BC}\n | Location: {bc.RC}{self.Link}{bc.BC}\n")

		return self.Matches, self.FoundCount

	def PrintResults(self, Results: list, FoundNum: int, TotalLinkCount: int):
		self.Cmd.Clear()
		self.Results: list = Results
		self.FoundCount = FoundNum
		self.TotalLinkCount = TotalLinkCount

		print(f"{sd.sBan} Found {bc.GC}{str(self.FoundCount)}{bc.BC} matches out of {bc.GC}{self.TotalLinkCount}{bc.BC} websites\n")
		for self.Match in self.Results:
			print(f" | Website: {bc.GC}{self.Validator.GetWebsiteName(self.Match)}{bc.BC}")
			print(f" | Location: {bc.GC}{self.Match}{bc.BC}\n")

		Initiate(True)

if __name__ == '__main__':
	def Initiate(SeenIntro = False):
		try:
			Run = Ph0enix()

			if(not SeenIntro):
				print(f"{sd.iBan} Matches may not always be specific to the user you are looking for")
				print(f"{sd.iBan} For example, someone else could have used the same username elsewhere\n")

			Username = InputManager().SetUsername()
			WebsiteLinks = Run.BuildLinks(Username)
			SearchResults, FoundCount = Run.StartSearch(Username, WebsiteLinks)
			Run.PrintResults(SearchResults, FoundCount, len(WebsiteLinks))
		except KeyboardInterrupt:
			quit()

	Command().Clear()
	Initiate()
