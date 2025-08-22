import os
import time
import sys
print("Checking package list...")
with open("../packages.txt","r") as read_packages:
    packages = read_packages.readlines()
    for line in packages:
        os.system(f"pip install {line}")
os.system("clear")
time.sleep(1)
with open("timeusedtf.txt","w") as writeTrue:
    writeTrue.write("True")
print("Now, you're device is ready to rock!")
reboot_enter = input("Press enter to reboot...")
os.system("../shs/boot3.sh")
sys.exit()