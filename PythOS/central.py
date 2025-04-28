import os
import sys
import time
import subprocess

while True:
    with open("userdata/username.txt","r") as read_username:
        username = read_username.read()
    cmd = input(f"{username}@PythOS:~$ ")
    try:
        cmd_splitted = cmd.split()[0]
    except IndexError:
        cmd_splitted = cmd
    if cmd == "exit":
        print("See you next time! Exitting...")
        with open("bin/arguments.txt", "w") as arg_file:
            arg_file.write("")
        with open("bin/command.txt","w") as cmd_file:
            cmd_file.write("")
        sys.exit()
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
                
            result = subprocess.Popen(
                f"python3 bin/{cmd_splitted}/{cmd_splitted}.py", 
                shell=True, 
                text=True, 
                stderr=subprocess.PIPE,
                stdout=subprocess.PIPE
            )
            stdout, stderr = result.communicate()
            
            if stderr:
                print(f"Error: {stderr.strip()}")
            if stdout:
                print(stdout.strip())
                
        except Exception as e:
            print(f"Error: {str(e)}")