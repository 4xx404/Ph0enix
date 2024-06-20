#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
sys.dont_write_bytecode = True

from Core.Styling import *

from Core.Environment import Environment
from Core.Database import Database
from Core.Config import CoreConfig
from Core.Commands import Command
from Core.Input import InputManager
from Core.Validity import Validation
from Core.Requester import RequestHandler
from Core.Error import ErrorHandler

ErrorHandler().CreateLogFile()

class Ph0enix:
	def __init__(self):
		self.Environment = Environment()
		self.Config = CoreConfig()
		self.Database = Database(self.Environment.Env, self.Config)
		self.Cmd = Command()
		self.Input = InputManager()
		self.Validator = Validation()
		self.Request = RequestHandler()
		self.Error = ErrorHandler()

	def BuildLinks(self, Username: str = None) -> (list | None):
		BuiltLinks = self.Request.LinkFormatter(Username)
		
		if(len(BuiltLinks) > 0):
			return BuiltLinks

		self.Cmd.Clear(f"{sd.eBan} No data found", False)

		self.Main()

	def LoadLinks(self, Username: str = None): # -> (dict | None)
		Links = self.Database.Select("website_urls", [["is_active", "=", 1]])

		Response = {}

		for LinkData in Links:
			LinkID = LinkData["id"] 
			Link = str(LinkData["url"])

			if("[USER]" in Link):
				Response[LinkID] = Link.replace("[USER]", Username)
			else:
				print(self.Error.Throw("link_username_replacement_chunk_not_found", Link))
		
		if(self.Validator.NotEmpty(Response)):
			return Response

		self.Cmd.Clear(f"{sd.eBan} No data found", False)

		self.Main()

	def StartSearch(self, Username: str = None, FormattedLinks: dict = {}) -> dict:
		self.Cmd.Clear(f"{sd.sBan}Searching for {bc.GC}{Username}{bc.BC}\n", False)

		Matches = {}

		for LinkID, Link in FormattedLinks.items():
			WebsiteName = self.Request.GetWebsiteName(Link)

			if(self.Validator.NotEmpty(WebsiteName)):
				IsInSite = self.Request.Search(Link)

				if(IsInSite):
					Matches[LinkID] = Link

					StatusBanner = f"{bc.GC}Match Found{bc.BC}"
					self.Error.AddToLog("info", f"Match found on '{WebsiteName}'")
				else:
					StatusBanner = f"{bc.RC}Not Found{bc.BC}"
					self.Error.AddToLog("info", f"No match found on '{WebsiteName}'")
				
				print(f"{bc.BC} | Website ID: {bc.GC}{LinkID}{bc.BC}")
				print(f" | Website: {bc.GC}{WebsiteName}{bc.BC}")
				print(f" | Status: {StatusBanner}")
				print(f" | Location: {bc.GC}{Link}{bc.BC}\n")

		return Matches

	def PrintResults(self, Username: str = None, SearchResults: dict = [], TotalLinkCount: int = 0) -> None:
		FoundCount = 0

		if(self.Validator.NotEmpty(SearchResults)):
			FoundCount = len(SearchResults.keys())

		self.Cmd.Clear()

		for MatchID, MatchLink in SearchResults.items():
			if(self.Environment.Env["StoreResults"] == "true"):
				self.Database.Insert(
					Table="found_profiles",
					Values=[self.Config.GenerateMD5(Username + self.Config.GenerateID()), MatchID, Username, MatchLink, self.Config.UnixTimestamp()]
				)

			print(f" | Website ID: {bc.GC}{MatchID}{bc.BC}")
			print(f" | Website: {bc.GC}{self.Request.GetWebsiteName(MatchLink)}{bc.BC}")
			print(f" | Location: {bc.GC}{MatchLink}{bc.BC}\n")

		print(f"{sd.sBan}Found {bc.GC}{str(FoundCount)}{bc.BC} potential matches on {bc.GC}{TotalLinkCount}{bc.BC} websites\n")

	def CommandStream(self, ShowHelp: bool = False, SeenIntro: bool = True) -> None:
		if(ShowHelp):
			print(f" Use {bc.GC}help{bc.BC} to see all commands\n")
		
		InputValue = str(input(f"{bc.BC} Command ?>{bc.GC} ")).strip()
		
		if(self.Validator.NotEmpty(InputValue)):
			if(InputValue == "help"):
				self.Cmd.Clear()

				self.Input.Help()
			elif(InputValue.startswith("database")):
				self.Cmd.Clear()

				self.Database.Interface.Stream(None, True)
			else:
				if(not SeenIntro):
					print(f"{sd.iBan} Matches may not always be specific to the user you are looking for")
					print(f"{sd.iBan} For example, someone else could have used the same username elsewhere\n")
				
				Username = InputValue
				
				if(self.Validator.NotEmpty(Username)):
					WebsiteLinks = self.LoadLinks(Username)
					SearchResults = self.StartSearch(Username, WebsiteLinks)

					self.PrintResults(Username, SearchResults, len(WebsiteLinks))
		else:
			self.Cmd.Clear(self.Error.Throw("empty_command_stream_value"), False)
		
		self.CommandStream()

if(__name__ == "__main__"):
	def Initiate():
		try:
			Run = Ph0enix()
			Run.CommandStream(True, False)
		except KeyboardInterrupt:
			ErrorHandler().AddToLog("info", "User interrupted the program")
			quit()

	Command().Clear()
	Initiate()
