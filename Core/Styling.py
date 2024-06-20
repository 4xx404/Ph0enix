#!/usr/bin/python3
import sys, emojis
sys.dont_write_bytecode = True

class bc:
	GC = '\033[1;39m'
	BC = '\033[1;34m'
	RC = '\033[1;31m'

class sd:
	iBan: str = emojis.encode(f" :information_source:{bc.BC} ")
	sBan: str = emojis.encode(f" :white_check_mark:{bc.BC} ")
	eBan: str = emojis.encode(f" :x:{bc.RC} ERROR:{bc.BC}")

	def Colorify(String: str = None, Color: str = None) -> str:
		if(Color == None):
			[LastCharColor, NewString] = ["red", ""]

			if(String != None and  String.strip() != ""):
				for Character in String:
					if(Character == " "):
						NewString += Character
					else:
						if(LastCharColor == "blue"):
							NewString += f"{bc.GC}{Character}"
							LastCharColor = "green"
						elif(LastCharColor == "green"):
							NewString += f"{bc.RC}{Character}"
							LastCharColor = "red"
						elif(LastCharColor == "red"):
							NewString += f"{bc.BC}{Character}"
							LastCharColor = "blue"
		else:
			if(Color.lower() == "red"):
				NewString = f"{bc.RC}{String}{bc.BC}"
			elif(Color.lower() == "green"):
				NewString = f"{bc.GC}{String}{bc.BC}"
			elif(Color.lower() == "blue"):
				NewString = f"{bc.BC}{String}{bc.BC}"

		return NewString

	Author_4xx404 = Colorify("4xx404", "green") + f"\t\t\t " + Colorify("https://github.com/4xx404", "green") + f"{bc.BC}\n\n"
	Contributor_JCalabres = Colorify("jcalabres", "green") + f"\t\t " + Colorify("https://github.com/jcalabres", "green") + f"{bc.BC}"
	Contributor_Kf637 = Colorify("Kf637", "green") + f"\t\t\t " + Colorify("https://github.com/Kf637", "green") + f"{bc.BC}\n\n"

	Authors = f"{bc.BC}\n Authors: \n\t{Author_4xx404}"
	Contributors = f"{bc.BC} Contributors: \n\t{Contributor_JCalabres}\n\t{Contributor_Kf637}"

	Version = f"{bc.BC} Version: {bc.GC}2.0{bc.BC}\n"

	Logo = f"""{bc.BC}
 .------..------..------..------..------..------..------..------..------.
 |{bc.GC}P{bc.BC}.--. ||{bc.GC}H{bc.BC}.--. ||{bc.GC}0{bc.BC}.--. ||{bc.GC}E{bc.BC}.--. ||{bc.GC}N{bc.BC}.--. ||{bc.GC}I{bc.BC}.--. ||{bc.GC}X{bc.BC}.--. ||{bc.GC}V{bc.BC}.--. ||{bc.GC}3{bc.BC}.--. |
 | :/\: || :/\: || :/\: || (\/) || :(): || (\/) || :/\: || :(): || :/\: |
 | (__) || (__) || :\/: || :\/: || ()() || :\/: || (__) || ()() || (__) |
 | "--"{bc.GC}P{bc.BC}|| "--"{bc.GC}H{bc.BC}|| "--"{bc.GC}0{bc.BC}|| "--"{bc.GC}E{bc.BC}|| "--"{bc.GC}N{bc.BC}|| "--"{bc.GC}I{bc.BC}|| "--"{bc.GC}X{bc.BC}|| "--"{bc.GC}V{bc.BC}|| "--"{bc.GC}3{bc.BC}|
 `------'`------'`------'`------'`------'`------'`------'`------'`------'
{Authors}{Contributors}{Version}"""