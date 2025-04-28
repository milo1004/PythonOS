import os
with open("bin/arguments.txt", "r") as arg_file:
    args = arg_file.read()
if args == "":
    directory = os.getcwd()
else:
    directory = args
try:
    for item in os.listdir(directory):
        print(item)
except:
    print("Invalid directory.")