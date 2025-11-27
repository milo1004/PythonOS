import os
import sys
import time
import subprocess
import signal
with open("currentdir.txt","w") as initw:
    initw.write("~")
while True:
    with open("userdata/username.txt","r") as read_username:
        username = read_username.read()
    with open("currentdir.txt","r") as read_currentdir:
        currentdir = read_currentdir.read().strip()
    if currentdir == "~/" or currentdir == "~":
        currentdir = "~"
    elif currentdir == "/":
        currentdir = "/"
    elif currentdir.startswith("~/"):
        # show as ~/<rest>, e.g. PythOS/boot/ -> ~/boot/
        currentdir = f"~/{currentdir[2:]}"
    cmd = input(f"{username}@PythOS:{currentdir}$ ")
    try:
        cmd_splitted = cmd.split()[0]
    except IndexError:
        cmd_splitted = cmd
    if cmd == "":
        pass
    elif cmd_splitted == "echo":
        args = cmd[5:]
        with open("bin/arguments.txt", "w") as arg_file:
            arg_file.write(args)
        os.system("python3 bin/echo/echo.py")
        continue
    elif cmd_splitted == "exit":
        while True:
            confirm = input("Are you sure you want to shutdown? (y/n): ").lower()
            if confirm == "y":
                print("Powering off...")
                time.sleep(1)
                os.system("clear")
                os.system("shutdown")
                break
            elif confirm == "n":
                print("Shutdown aborted.")
                break
            elif confirm == "":
                print("Powering off...")
                time.sleep(1)
                os.system("clear")
                os.system("shutdown")
                break
            else:
                print("Shutdown aborted.")
                break
    else:
        try:
            try:
                args = cmd.split()[1]
                with open("bin/arguments.txt", "w") as arg_file:
                    arg_file.write(args)
            except:
                with open("bin/arguments.txt", "w") as arg_file:
                    arg_file.write("")
            try: 
                args2 = cmd.split()[2]
                with open("bin/arguments2.txt", "w") as arg2_file:
                    arg2_file.write(args2)
            except:
                pass
            # Check if the command directory exists
            if not os.path.exists(f"bin/{cmd_splitted}"):
                print(f"{cmd_splitted}: Command not found.")
                continue
                
            # Check if the command file exists
            if not os.path.exists(f"bin/{cmd_splitted}/{cmd_splitted}.py"):
                print(f"{cmd_splitted}: Command not found.")
                continue
            os.system(f"python3 bin/{cmd_splitted}/{cmd_splitted}.py")
                
        except KeyboardInterrupt:
            print("test")
            os.killpg(os.getpgid(result.pid), signal.SIGINT)
            result.wait()
