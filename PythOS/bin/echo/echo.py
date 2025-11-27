import os
import sys

with open("bin/arguments.txt","r") as args:
    args = args.read()
if args == "":
    pass
elif args[0] == "\"":
    if args[-1] == "\"":
        print(args[1:-1])
    else:
        print(args)
elif args[0] == "'":
    if args[-1] == "'":
        print(args[1:-1])
    else:
        print(args)
else:
    print(args)