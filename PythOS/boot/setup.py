import time
import sys
import os
import subprocess
import getpass
def clear():
    os.system("clear")
clear()
print("Hi! And thank you for choosing PythOS 6.1! It is a brand new redesigned and clean Operating System made fully by Python.")
time.sleep(2)
print("Before we begin, there's a very important thing: Terms and Agreements!")
with open("Terms and Services.txt", "r") as TaS:
    print(TaS.read())
    agreeyn = input("Do you agree with the Terms & Services?(yn) >")
    if agreeyn.lower() == "" or agreeyn.lower() == "y":
        print("Great! Now, let's get started!")
        os.system("clear")
        login_ask = input("Now, let's setup something about your account. What username would you like to create? (We take \"user\" as default.) >")
        if login_ask == "":
            print("Since you've decided to make your username as \"blank\", we'll make it \"user\" for you.")
            print("Change your mind anytime by typing \"username -c\"")
            with open("../userdata/username.txt", "w") as usrnamewrite:
                usrnamewrite.write("user")
        else:
            print("Good choice!")
            with open("../userdata/username.txt", "w") as usrnamewrite:
                usrnamewrite.write(login_ask)
        passwd_set = getpass.getpass("Let's setup your password.(Note: a blank password will be considered as no password.) >")
        if passwd_set == "":
            clear()
            print("Okay, password is set to none.(Change anytime by typing \"passwd -c\")")
            with open("../userdata/passwd.txt", "w") as passwdwrite:
                passwdwrite.write("")
                sys.exit()
        else:
            clear()
            print("Done!")
            with open("../userdata/passwd.txt", "w") as passwdwrite:
                command = "echo -n " + passwd_set + " | od -An -t x1 | tr -d ' \n'"
                password = subprocess.check_output(command, text=True, shell=True)
                passwdwrite.write(password)
        print("Installing packages...")
        os.system("xbps-install -u xbps")
        os.system("xbps-install python3")
        os.system("xbps-install -upipx")
        Enter=input("Press Enter to reboot...")
        with open("timeusedtf.txt","w") as write_boot:
            write_boot.write("Setup-In-Progress")
        os.system("pwd")
        time.sleep(3)
        clear()
        os.system("python3 boot.py")
    elif agreeyn.lower() == "n":
        print("Sorry, but you can't use PythOS 6.1 without agreeing")
        time.sleep(0.5)
        print("But no worries, you can change your mind anytime. Just reboot the computer.")
        time.sleep(1)
        print("We will now shutdown the computer.")
        time.sleep(1)
        print("Cancelling...")
        with open("timeusedtf.txt","w") as retry_setup:
            retry_setup.write("False")
        os.system("shutdown now")
        sys.exit()
    else:
        print("Sorry, but you can't use PythOS 6.1 without agreeing")
        time.sleep(0.5)
        print("But no worries, you can change your mind anytime. Just reboot the computer.")
        time.sleep(1)
        print("Cancelling...")
        with open("timeusedtf.txt","w") as retry_setup:
            retry_setup.write("False")
        print("We will now shutdown the computer.")
        time.sleep(1)
        os.system("shutdown now")
        sys.exit()
