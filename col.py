import sys
import platform

class Colour:
    def __init__(self) -> None:
        pass
    
    if sys.stdout.isatty() and platform.system() == "Windows":
        green = '\033[32m'
        blue = '\033[94m'
        red = '\033[31m'
        brown = '\033[33m'
        end = '\033[0m'
    else:   # Colours mess up redirected output, disable them
        green = ""
        blue = ""
        red = ""
        brown = ""
        end = ""