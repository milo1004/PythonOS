import sys
import time
import os
import random
import math
import decimal
from datetime import datetime
command = (0)
def start():
  os.system('cls')
  print("booting RAM...")
  time.sleep(3)
  print("booting CPU...")
  time.sleep(3)
  print("booting Hardisk...")
  time.sleep(2)
  print("booting PythonOS...")
  time.sleep(5)
  os.system("cls")
  print("Welcome to PythonOS 2")
  time.sleep(0.5)
  print(
      "You may begin entering the commands. Type 'help' for a list of commands. Or, you may type'apps' to show a list of apps.(Update Log added to PythonOS. Type 'update log' to check the things that are updated.)"
  )
  while True:
    command = input("C:\command> ")
    if command == "help":
      print("commands:")
      print("help - shows this list.")
      print("apps - shows a list of apps.")
      print("shutdown - shuts down the computer.")
      print("pyver - shows the current version of PythonOS.")
      print("date - shows the current date.")
      print("time - shows the current time.")
      print("restart - restarts the computer.")
      print("cls  /  clear - clear the terminal(you can still use the computer normally.)")
      print("update log - check the update log through this command.")
      print("sleep - put the computer to sleep, you can press Enter key to wake it up.")
      print("Note: If you want to open an app, type the app name, and add '.exe' behind.")
    elif command == "apps":
      print("apps:")
      print("random.exe - open random number picker")
      print("calc.exe - a simple calculator")
      print("that's all for now.")
    elif command == "shutdown":
      shutdown_yn = input("Are you sure you want to shutdown? y/n>")
      if shutdown_yn == "y":
        print("Shutting down...")
        time.sleep(2)
        print("Operating System Terminated")
        time.sleep(1)
        os.system("cls")
        sys.exit()
      elif shutdown_yn == "n":
        print("Shutdown cancelled.")
        time.sleep(1)
      else:
        print("Invalid input.")
        print("shutdown cancelled")
        time.sleep(1)
    elif command == "pyver":
      print("PythonOS 2")
      print("y_ver. 24")
      print("Copyright © 2024, python.org")
      print("All rights reserved.")
      print("This is a free operating system. It is not endorsed by python.org")
      print("you can download this software from https://github.com/milo1004/PythonOS.git")
      print("(end of properties)")
    elif command == "date":
      datenow = datetime.now()
      print("The date will be shown like this:YYYY/MM/DD")
      current_date = datenow.strftime("%Y/%m/%d")
      print(f"The Current date is : {current_date}")
    elif command == "time":
      timenow = datetime.now()
      print("The time will be shown like this:HH:MM")
      current_time = timenow.strftime("%H:%M")
      print(f"The Current time is : {current_time}")
    elif command == "random.exe":
      print("Welcome to Randomizer!")
      time.sleep(0.5)
      print("Warning: 1.DO NOT enter a non-number character")
      print("         2.when entering the greatest number, DO NOT enter a number which is smaller than the least number.")
      print("Doing these will result an error appears and you may need to restart the computer.")
      Lrandom = input("Enter the least number>")
      if Lrandom == "":
        print("Invalid input.")
        time.sleep(1)
      else:
        print("Invalid Input")
        time.sleep(1)
      Grandom = input("Enter the greatest number>")
      if Grandom == "":
        print("Invalid input.")
        time.sleep(1)
      else:
        print("Invalid Input")
        time.sleep(1)
      random_number = random.randint(int(Lrandom), int(Grandom))
      print(f"The randomized number is: {random_number}")
    elif command == "restart":
      restart = input("Are you sure you want to restart? y/n>")
      if restart == "y":
        print("Restarting...")
        time.sleep(1)
        os.system("cls")
        time.sleep(1)
        start()
      elif restart == "n":
        print("Restart cancelled")
        time.sleep(1)
      else:
        print("Invalid Input")
        print("Restart cancelled")
    elif command == "update log":
      print("Update Log:")
      print("shortened the startup time.")
      print("Added new application: Python Calculator, command: 'calc.exe'.")
      time.sleep(1)
    elif command == "sleep":
      sleep_confirm = input("You can wake the computer by pressing Enter.(press enter to continue.)")
      os.system("cls")
      sleep_response = input("")
      os.system("cls")
      print("Welcome back, user!")
    elif command == "calc.exe":
      print("Welcome to Python Calculator!")
      answer = ("null")
      time.sleep(0.5)
      print("Please input the formula down below.(Remember, always use these symbols: + - * /(plus, minus, time, divide))")
      fx = input("Formula:")
      answer = eval(fx)
      print(f"The Answer is: {answer}")
    elif command == "":
      print("Invalid input.")
    elif command == "cls":
      os.system('cls')
    elif command == "clear":
      os.system('cls')
    else:
      print("Illegal command. Type 'help' for a list of commands.")
start()
