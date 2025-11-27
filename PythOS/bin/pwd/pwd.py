import os
import sys
with open("bin/arguments.txt","r") as args:
    args=args.read()
if args == "":
    with open("currentdir.txt","r") as read_file:
        currentdir = read_file.read()
    print(f"Current working directory: {currentdir}")
elif args == "231293hehe":
    print(os.system("pwd"))
    print(args)
sys.exit()