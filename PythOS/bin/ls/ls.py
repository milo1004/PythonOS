import os

with open("currentdir.txt", "r") as curdir_file:
    curdir = curdir_file.read()
with open("bin/arguments.txt", "r") as args_file:
    args = args_file.read()
if args == "":
    if curdir == "PythOS/":
        os.system("ls")
    elif curdir=="/":
        os.system("ls ../")
    else:
        if curdir[:7] == "PythOS/":
            os.system(f"ls {curdir[7:]}")
        elif curdir[1] == "/":
            os.system(f"ls ../{curdir}")