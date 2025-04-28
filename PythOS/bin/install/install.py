import os
with open("bin/arguments.txt","r") as read_commands:
    args = read_commands.read()
print(f"installing {args}")
os.system(f"pip install {args}")