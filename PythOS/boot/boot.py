import os
import time
import sys
import signal
print("Booting PythOS...")

with open("timeusedtf.txt","r") as read_boot:
        boot_tf = read_boot.read()
        if boot_tf == "" or boot_tf == "False":
            with open("loggedon.txt","w") as loggedon:
                loggedon.write("Setup")
            os.system("python3 setup.py")
        elif boot_tf == "Setup-In-Progress":
            with open("loggedon.txt","w") as loggedon:
                loggedon.write("Setup")
            os.system("python3 install.py")
            sys.exit()
        elif boot_tf == "True":
            with open("loggedon.txt","w") as loggedon:
                loggedon.write("False")
            os.system("python3 logon.py")
            sys.exit()
        else:
            with open("timeusedtf.txt","w") as write_boot:
                write_boot.write("True")
                os.system("cd PythOS/boot/ && python3 boot.py")
            sys.exit()