import os
import time
import sys
print("Installing pip packages. This might take a few minutes.")
os.system("pip install -r requirements.txt")
print("You're device is ready!")
reboot_enter = input("Press enter to reboot...")
with open("timeusedtf.txt","w") as writeTrue:
    writeTrue.write("True")
os.system("cd ../../ && python3 main.py")
sys.exit()
