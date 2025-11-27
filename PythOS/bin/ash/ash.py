import os
with open("bin/arguments.txt","r") as args:
    args = args.read()
with open("bin/arguments2.txt","r") as args2:
    args2 = args2.read()
if args == "231293hehe":
    if args2 == "":
        print("No command provided. Proper Format:\n    ash [developerpassword] [ashcommand]")
    else:
        os.system(args2)
else:
    print("Developer password needed, access denied.")