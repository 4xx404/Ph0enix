import os

from .Styling.Banners import sd

class Command:
    def __init__(self):
        pass

    def Clear(self):
        os.system("clear")
        print(sd.Logo)
