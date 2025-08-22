import subprocess
import os
import time

with open("bin/arguments.txt", "r") as arg_file:
    args = arg_file.read()
if args == "":
    print("No arguments provided.")
    print("Arguments available:")
    with open("bin/reboot/argumentsexplained.txt","r") as arg_explained:
        print(arg_explained.read())
elif args == "-now":
    print("The computer is going to reboot NOW!")
    subprocess.run("python3 bin/reboot/reboot_now.py", shell=True, text=True, check=True, stderr=subprocess.DEVNULL)
elif args == "-refresh":
    print("The computer is going to refresh NOW!")
    subprocess.run("python3 bin/reboot/reboot_refresh.py", shell=True, text=True, check=True, stderr=subprocess.DEVNULL)
else:
    print("Invalid arguments provided.")
    with open("bin/reboot/argumentsexplained.txt","r") as arg_explained:
        print(arg_explained.read())