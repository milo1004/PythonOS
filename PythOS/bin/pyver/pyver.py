import sys
import time
import pyfiglet
import re
print("About PythOS")
ascii_version_title = pyfiglet.figlet_format("PythOS NewCore")
with open("boot/PythOSLogo.txt","r") as readLogo:
    readLogo = readLogo.read()
    print(readLogo)
print(ascii_version_title)
print(f"OS version: PythOS 6.0")
print(f"Codename: NewCore")
print(f"Python version: {sys.version}")
print(f"MIT License:")
with open("bin/pyver/MIT License.txt","r") as readLicense:
    readLicense = readLicense.read()
    print(readLicense)