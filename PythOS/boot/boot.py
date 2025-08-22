import os
import time
import sys
print("Booting PythOS...")
    
with open("timeusedtf.txt","r") as read_boot:
        boot_tf = read_boot.read()
        if boot_tf == "" or boot_tf == "False":
            with open("timeusedtf.txt","w") as write_boot:
                write_boot.write("Setup-In-Progress")
            os.system("python3 setup.py")
        elif boot_tf == "Setup-In-Progress":
            with open("timeusedtf.txt","w") as complete_boot:
                complete_boot.write("True")
            os.system("python3 install.py")
            sys.exit()
        elif boot_tf == "True":
            os.system("../shs/logon.sh")
            sys.exit()
        else:
            with open("timeusedtf.txt","w") as write_boot:
                write_boot.write("True")
                os.system("../boot.sh")
            sys.exit()
