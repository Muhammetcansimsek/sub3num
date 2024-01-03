from col import Colour as col
class Output:
    def __init__(self) -> None:
         pass
    def status(self, msg1, msg2):
        print(col.blue + "[*] " + col.end + msg1 + " : " + msg2)

    def good(self, msg1, msg2):
        print(col.green + "[+] " + col.end + msg1 + " : " + msg2)

    def verbose(self, msg1, msg2):
            print(col.brown + "[v] " + col.end + msg1 + " : " + msg2)

    def warn(self, msg1, msg2):
        print(col.red + "[-] " + col.end + msg1 + " : " + msg2)

    def fatal(self, msg1, msg2):
        print("\n" + col.red + "FATAL: " + msg1 + " : " + msg2 + col.end)
