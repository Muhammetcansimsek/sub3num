from col import Colour as col
class Output:
    def __init__(self) -> None:
         pass
    def status(self, msg1, msg2):
        print(col.blue + "[*] " + msg1 + " : " + msg2 + col.end)

    def good(self, msg1, msg2):
        print(col.green + "[+] " + msg1 + " : " + msg2 + col.end)

    def verbose(self, msg1, msg2):
            print(col.brown + "[v] " + msg1 + " : " + msg2 + col.end)

    def warn(self, msg1, msg2):
        print(col.red + "[-] " + msg1 + " : " + msg2 + col.end)

    def fatal(self, msg1, msg2):
        print("\n" + col.red + "FATAL: " + msg1 + " : " + msg2 + col.end)
