# -*- coding: utf-8 -*-

import os

from Core.Styling.Banners import sd
Banner, sBan, eBan, iBan = sd.logo, sd.sBan, sd.eBan, sd.iBan
from Core.Styling.Colors import bc

from Core.Config import CoreConfig
Config = CoreConfig()
from Core.Validity import Validation
Validator = Validation()
from Core.Requester import RequestHandler
Request = RequestHandler()
from Core.Error import ErrorHandler
Error = ErrorHandler()

def Clear():
	os.system("clear")
	print(Banner)

def Ph0enix(LinkList, Username):
	FoundCount = 0
	Matches = []

	try:
		print(f"{sBan} Searching: {bc.GC}{Username}{bc.BC}\n")
		for Link in LinkList:
			Website = Validator.GetWebsiteName(Link)
			IsInSite = Request.Search(Link, Username)

			if(IsInSite):
				FoundCount += 1
				Matches.append(Link)
				print(f" | Website: {bc.GC}{Website}{bc.BC}")
				print(f" | Status: {bc.GC}Match Found{bc.BC}")
				print(f" | Location: {bc.GC}{Link}{bc.BC}\n")
			else:
				print(f" | Website: {bc.RC}{Website}{bc.BC}")
				print(f" | Status: {bc.RC}Not Found{bc.BC}")
				print(f" | Location: {bc.RC}{Link}{bc.BC}\n")

		Clear()

		print(f"{sBan} Found {bc.GC}{str(FoundCount)}{bc.BC} matches out of {bc.GC}{str(len(LinkList))}{bc.BC} websites\n")
		for Match in Matches:
			print(f" | Website: {bc.GC}{Validator.GetWebsiteName(Match)}{bc.BC}")
			print(f" | Location: {bc.GC}{Match}{bc.BC}\n")

		Initiate()
	except KeyboardInterrupt:
		print(f"{bc.BC} | Scan stopped...\n")
		Initiate()

if __name__ == '__main__':
	Clear()
	print(f"{iBan} Matches may not always be specific to the user you are looking for")
	print(f"{iBan} For example, someone else could have used the same username elsewhere\n")

	def Initiate():
		try:
			Username = str(input(f"{bc.BC} Username: {bc.GC}"))

			LinkBuild = Validator.LinkFormatter(Username)
			if(LinkBuild["success"]):
				Clear()
				Ph0enix(LinkBuild["data"], Username.lower())
			else:
				Clear()
				print(LinkBuild["data"][0]) # Print Error
				Initiate()
		except KeyboardInterrupt:
			quit()

	Initiate()
