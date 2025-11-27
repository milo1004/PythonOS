import os
with open("bin/command.txt","r") as cmd:
    command = cmd.read()
os.system(command)