import os
with open("bin/arguments.txt","r") as read_commands:
    args = read_commands.read()
with open("bin/arguments2.txt","r") as read_commands2:
    args2 = read_commands2.read()
if args2 == "":
    try:
        os.system(f"sudo apt install {args}")
    except:
        print("Error: Failed to install package")
elif args2 == "-r":
    try:
        os.system(f"sudo apt remove {args}")
    except:
        print("Error: Failed to remove package")
print(f"apt installing {args}")