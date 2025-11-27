import os

with open("currentdir.txt","r") as orgdir:
    orgdir = orgdir.read()
with open("bin/arguments.txt","r") as args:
    args = args.read()

if args == "":
    if orgdir[:1] == "~":
        if orgdir == "~":
            os.system("ls ./")
        else:
            os.system(f"ls ./{orgdir[2:]}")
    elif orgdir[0] == "/":
        if orgdir == "/":
            os.system("ls ../")
        else:
            os.system(f"ls ..{orgdir}")
elif args[:2] == "..":
    if args == ".." or args == "../":
        if orgdir == "~":
            os.system(f"ls ../")
        elif orgdir == "/":
            os.system("ls ../")
        else:
            if orgdir[0] == "/":
                if os.path.exists(os.path.dirname(f"../{orgdir[1:]}")):
                    os.system(f"ls ..{os.path.dirname(orgdir)}")
                else:
                    print(f"ls: {os.path.dirname(orgdir)}: No such file or directory.")
            elif orgdir[0] == "~":
                if os.path.exists(os.path.dirname(orgdir[1:])):
                    os.system(f"ls .{os.path.dirname(orgdir[1:])}")
                else:
                    print(f"ls: {os.path.dirname(orgdir)}: No such file or directory.")
    else:
        if orgdir[0] == "~":
            if orgdir == "~":
                if os.path.exists(f"../{args[3:]}"):
                    os.system(f"ls ../{args[3:]}")
                else:
                    print(f"ls: {args}: No such file or directory.")
            else:
                if os.path.exists(args):
                    os.system(f"ls {args}")
                else:
                    print(f"ls: {args}: No such file or directory.")
        elif orgdir == "/":
            if orgdir == "/":
                print(f"Displaying files inside: /{args[3:]}/")
                if os.path.exists(f"../{args[3:]}"):
                    os.system(f"ls ../{args[3:]}")
                else:
                    print(f"ls: {args}: No such file or directory.")
            else:
                if os.path.exists(args):
                    os.system(f"ls {args}")
                else:
                    print(f"ls: {args}: No such file or directory.")
elif args[0] == "~":
    if args == "~":
        os.system("ls ./")
    else:
        if os.path.exists(f"./{args[2:]}"):
            os.system(f"ls ./{args[2:]}")
        else:
            print(f"ls: {args}: No such file or directory.")
elif args[0] == "/":
    if args == "/":
        os.system("ls ../")
    else:
        if os.path.exists(f"../{args[1:]}"):
            os.system(f"ls ../{args[1:]}")
        else:
            print(f"ls: {args}: No such file or directory.")
else:
    if orgdir[0] == "~":
        if os.path.exists(f"./{args}"):
            os.system(f"ls ./{args}")
        else:
            print(f"ls: {args}: No such file or directory.")
    elif orgdir[0] == "/":
        if os.path.exists(f"../{args}"):
            os.system(f"ls ../{args}")
        else:
            print(f"ls: {args}: No such file or directory.")