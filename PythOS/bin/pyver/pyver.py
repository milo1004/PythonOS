import sys
import time
import re
print("About PythOS")
with open("boot/PythOSLogo.txt","r") as readLogo:
    readLogo = readLogo.read()
    print(readLogo)
print(f"OS version: PythOS 6.2")
print(f"Codename: NewCore")
print(f"Python version: {sys.version}")