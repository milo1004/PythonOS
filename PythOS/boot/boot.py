import os
import sys

os.system("clear")

with open("timeusedtf.txt","r") as f:
    tf = f.read()
    
if tf == "False":
    os.system("python3 setup.py")
elif tf == "":
    os.system("python3 setup.py")
elif tf == "True":
    os.system("python3 logon.py")
elif tf == "Setup-In-Progress":
    os.system("python3 install.py")