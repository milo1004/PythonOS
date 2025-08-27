import os

with open("currentdir.txt", "r") as curdir_file:
    curdir = curdir_file.read()
with open("bin/arguments.txt", "r") as args_file:
    args = args_file.read()
if args == "":
    pass
elif args == "/":
    with open("currentdir.txt", "w") as curdir_file:
        curdir_file.write("/")
elif args == "~" or args == "~/":
    with open("currentdir.txt", "w") as curdir_file:
        curdir_file.write("PythOS/")
elif args == "..":
    if curdir == "PythOS/":
        with open("currentdir.txt", "w") as curdir_file:
            curdir_file.write("/")
    elif curdir == "/":
        with open("currentdir.txt", "w") as curdir_file:
            curdir_file.write("/")
    else:
        s = curdir.rstrip('/')
        idx = s.rfind('/')
        new = "/" if idx == -1 else s[:idx+1]
        with open("currentdir.txt", "w") as curdir_file:
            curdir_file.write(new)
elif args == ".":
    pass
elif args == "PythOS/" or args == "PythOS":
    if curdir == "/":
        with open("currentdir.txt", "w") as curdir_file:
            curdir_file.write("PythOS/")
    else:
        if os.path.exists("PythOS/"):
            with open("currentdir.txt", "w") as curdir_file:
                curdir_file.write(f"{curdir}PythOS/")
        else:
            print(f"{args}: No such file or directory")
else:
    if len(curdir) == 7 and curdir[:7] == "PythOS/":
        if os.path.exists(args):
            with open("currentdir.txt", "w") as curdir_file:
                curdir_file.write(f"PythOS/{args}")
        else:
            print(f"{args}: No such file or directory")
    elif curdir[0] == "/" and len(curdir) == 1:
        # build target without duplicating slashes, keep trailing '/'
        target = args if args.startswith("/") else f"/{args}"
        # remove duplicate leading slashes then ensure trailing slash
        target = "/" + target.lstrip("/") 
        if not target.endswith("/"):
            target = target + "/"
        # optional existence check (keep your existing check style)
        if os.path.exists(f"..{target}"):
            with open("currentdir.txt", "w") as curdir_file:
                curdir_file.write(target)
        else:
            print(f"{args}: No such file or directory")
    elif args.startswith("~/"):
        if os.path.exists(f"./{args}"):
            with open("currentdir.txt", "w") as curdir_file:
                curdir_file.write(f"PythOS/{args}")
        else:
            print(f"{args}: No such file or directory")
    elif args.startswith("/"):
        if os.path.exists(f"../{args}"):
            with open("currentdir.txt", "w") as curdir_file:
                curdir_file.write(args)
        else:
            print(f"{args}: No such file or directory")
    else:
        if os.path.exists(f"{curdir}/{args}"):
            with open("currentdir.txt", "w") as curdir_file:
                curdir_file.write(f"{curdir}/{args}")
        else:
            print(f"{args}: No such file or directory")