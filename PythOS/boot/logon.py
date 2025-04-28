import os
import time
import sys
import getpass
time.sleep(1)
def clear():
    os.system("clear")
with open("../userdata/username.txt","r") as readusr:
    username = readusr.read()
clear()
print("Logon")
print(f"Hey, welcome back to PythOS, {username}!")
with open("../userdata/passwd.txt","r") as readpasswd:
    passwd = readpasswd.read()
    passwd_converted = bytes.fromhex(passwd).decode("utf-8")
if passwd_converted == "":
    os.system("python3 show_info.py")
else:
    while True:
        logon = input("Please input your password >")
        if logon == passwd_converted:
            print(f"Welcome back, {username}!")
            os.system("python3 show_info.py")
            sys.exit()
        else:
            print("Incorrect password. Please try again.")
sys.exit()
