import os

def clear():
    os.system("clear")
clear()

with open("PythOS/boot/live.txt","r") as live:
    live=live.read()
if live == "True":
    with open("PythOS/userdata/username.txt","w") as usr:
        usr.write("live-session")
    with open("PythOS/userdata/passwd.txt","w") as pw:
        pw.write("")
    with open("PythOS/boot/insprompt.txt","w") as ip:
        ip.write("True")
    os.system("cd PythOS/boot && python3 logon.py") 
elif live == "False":
    with open("PythOS/userdata/username.txt","w") as usr:
        usr.write("user")
    with open("PythOS/userdata/passwd.txt","w") as pw:
        pw.write("")
    with open("PythOS/boot/insprompt.txt","w") as ip:
        ip.write("False")
    os.system("cd PythOS/boot && python3 bmenu.py")