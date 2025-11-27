import os

with open("bin/arguments.txt","r") as args:
    args = args.read()
with open("currentdir.txt","r") as orgdir:
    orgdir = orgdir.read()
if orgdir == "":
    with open("currentdir.txt","w") as orgdirw:
        orgdirw.write("/")
        
if args == "":
    curdir = "~"
elif args[0] == "~":
    if args == "~" or args == "~/":
        curdir = "~"
    else:
        if os.path.exists(f"./{args[2:]}"):
            curdir = f"~/{args[2:]}"
        else:
            print(f"cd: {args}: No such file or directory")
elif args[0] == "/":
    if args == "/" or args == "//":
        curdir = "/"
    elif args[1:] == "PythOS/" or args[1:] == "PythOS":
        curdir = "~"
    else:
        if os.path.exists(f"..{args}"):
            curdir = f"/{args[1:]}"
        else:
            print(f"cd: {args}: No such file or directory")
elif args == "./" or args == ".":
    curdir = orgdir

elif args[:2] == "..":
    count = False
    count = args.count("..")
    if count == 1:
        counttf = True
    elif count > 1:
        if orgdir == "~/" or orgdir == "~":
            curdir = "~"
        elif orgdir == "/":
            curdir = "/"
        else:
            curdir = os.path.dirname(orgdir)
        for _ in range(count - 1):
            if curdir == "~/" or curdir == "~":
                curdir = "~"
                break
            elif curdir == "/":
                curdir = "/"
                break
            else:
                curdir = os.path.dirname(curdir)
    if args == "../" or args == "..":
        if count > 1:
            pass
        else:
            if orgdir == "/":
                curdir = "/"
            elif orgdir == "~":
                curdir = "/"
            else:
                if orgdir[0] == "/":
                    if os.path.dirname(orgdir) == "/":
                        curdir = "/"
                    else:
                        curdir = os.path.dirname(orgdir)
                elif orgdir[0] == "~":
                    if os.path.dirname(orgdir) == "~":
                        curdir = "~"
                    else:
                        curdir = os.path.dirname(orgdir)
    else:
        if count > 1:
            pass
        else:
            if orgdir[0] == "~":
                dir = f"{os.path.dirname(orgdir)}{args[2:]}"
                if os.path.exists(f"./{dir[2:]}"):
                    curdir = dir
                else:
                    print(f"cd: {args}: No such file or directory.")
            elif orgdir[0] == "/":
                dir = f"{os.path.dirname(orgdir)}{args[2:]}"
                if os.path.exists(f"../{dir[2:]}"):
                    curdir = dir[1:]
                else:
                    print(f"cd: {args}: No such file or directory.")
else:
    if orgdir[0] == "~":
        if os.path.exists(f"./{orgdir[2:]}/{args}"):
            curdir = f"{orgdir}/{args}"
        else:
            print(f"cd: {args}: No such file or directory.")
    elif orgdir[0] == "/":
        if os.path.exists(f"../{orgdir}/{args}"):
            if orgdir == "/":
                curdir = f"/{args}"
        else:
            print(f"cd: {args}: No such file or directory.")
    
with open("currentdir.txt","w") as curdirw:
    
    try:
        if curdir == "/PythOS/" or curdir == "/PythOS":
            curdir = "~"
        elif curdir[:8] == "/PythOS/":
            curdir = f"~/{args[8:]}"
        else:
            pass
        curdirw.write(curdir)
    except Exception as e:
        curdirw.write(orgdir)