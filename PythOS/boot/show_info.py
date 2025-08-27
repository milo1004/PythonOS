import os
print("PythOS 6.0R")
with open("PythOSLogo.txt","r") as read_logo:
    read_logo = read_logo.read()
    for line in read_logo:
        print(line, end="")
print("Type \"help\" if you need help.")        
os.system("cd ../ && python3 central.py")
