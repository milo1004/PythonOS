import os
print("PythOS 6.2")
with open("PythOSLogo.txt","r") as read_logo:
    read_logo = read_logo.read()
    for line in read_logo:
        print(line, end="")
with open("insprompt.txt","r") as ip:
    ip=ip.read()
    
if ip == "True":
    print("Type \"setup-pythos\" to install PythOS, \"help\" to get help.")
else:
    print("Type \"help\" to get help.")
os.system("cd ../ && python3 central.py")
