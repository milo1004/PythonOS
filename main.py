import sys
import time
import os
with open("data/timeused.txt", "r") as timeused:
  if timeused.read() == "0":
    print("We'll now install the latest modules.")
    time.sleep(2)
    os.system('sudo apt install python3-PyGithub')
    print("Done.")
    os.system("sudo apt install python3-pygame")
    os.system("clear")
    from pygame import mixer  #type: ignore
  elif timeused.read() == "":
    print("We'll now install the latest modules.")
    time.sleep(2)
    os.system('sudo apt install python3-PyGithub')
    print("Done.")
    os.system("sudo apt install python-pygame")
    os.system("clear")
    from pygame import mixer #type:ignore
  elif timeused.read() > 0:
    pass
import random
import getpass
import glob
from datetime import datetime
command = ""
version = "5.0"
username = ""
version_name = "PythonOS: QuantumLeap"


def logon():
  with open("data/user/account/password.txt", "r") as password_check:
    password = password_check.read()
    if password == "":
      pass
    else:
      password_correct = False
      while not password_correct:
        password_input = input("Please input your password>")
        if password_input == password:
          password_correct = True
          print("Loading...")
        else:
          print("Incorrect password, please try again.")
          time.sleep(1)


def setup():
  time.sleep(1)
  os.system("clear")
  with open("data/timeused.txt", "r") as setup:
    timeused = setup.read()
    if timeused == "0":
      timeused = (str(1))
      with open("data/timeused.txt", "w") as setup_2:
        setup_2.write("")
        setup_2.write(timeused)
        os.system("clear")
        print("It looks like that this is the first time you run PythonOS!")
        username_set = input(
            "Please input a username that you want us to call you>")
        if username_set == "":
          print(
              "If you input a blank username, PythonOS will call you 'user'.")
          username = "user"
          with open("data/username.txt", "w") as username_set:
            username_set.write("")
            username_set.write(username)
        else:
          username = username_set
          with open("data/username.txt", "w") as username_set:
            username_set.write("")
            username_set.write(username)
      with open("data/Terms & Services", "r") as terms:
        print("Please agree the following Terms of Agreements")
        print(terms.read())
        terms_agreement = input("Do you agree with this?(y/n)>")
        if terms_agreement == "y":
          print("Thank you for agreeing with the Terms of Agreements.")
        elif terms_agreement == "n":
          print("You must to agree with the Terms of Agreements in order to use PythOS.")
          time.sleep(1)
          change_mind = input("Would you like to change your mind?(y/n)>")
          if change_mind == "y":
            print("Thank you for agreeing with the Terms of Agreements.")
          else:
            print("We will now switch back to the Linux console. Change your mind anytime by rerunning the Operating System.")
            print("shuting down...")
            time.sleep(2)
            os.system("clear")
            sys.exit()
        else:
          print("We'll take that as a no.")
          time.sleep(1)
          print("We'll now reboot the OS if you want to change your mind")
          time.sleep(1)
          print("rebooting...")
          with open("data/timeused.txt", "w") as reset_setup:
            reset_setup.write("0")
          os.system("clear")
          os.system("python3 main.py")
    elif timeused > str(0):
      try:
        timeused = eval(f"{timeused} + 1")
        with open("data/timeused.txt", "w") as setup_3:
          setup_3.write("")
          setup_3.write(str(f"{timeused}"))
      except:
        print(
            "startup error, the computer will now run diagnosis, please wait.")
        time.sleep(3)
        with open("data/timeused.txt", "w") as diagnosis_data:
          os.system('clear')
          print("Diagnosis in progress...")
          time.sleep(2)
          diagnosis_data.write("")
          diagnosis_data.write("0")
          print("Diagnosis complete.")
          time.sleep(1)
          print("Rebooting...")
          time.sleep(2)
          os.system("clear")
          start()
    elif timeused == "":
      with open("data/timeused.txt", "w") as setup_2:
        setup_2.write("1")
        setup_2.write(timeused)
        timeused = (str(1))
        print("It looks like that this is the first time you run PythOS!")
        username_set = input(
            "Please input a username that you want us to call you>")
        if username_set == "":
          print(
              "If you input a blank username, PythonOS will call you 'user'.")
          username = "user"
          with open("data/username.txt", "w") as username_set:
            username_set.write("")
            username_set.write(username)
        else:
          username = username_set
          with open("data/username.txt", "w") as username_set:
            username_set.write("")
            username_set.write(username)
    elif timeused > str(0):
      timeused = eval(f"{timeused} + 1")
      with open("data/timeused.txt", "w") as setup_3:
        setup_3.write("")
        setup_3.write(timeused)
    else:
      print("startup error, the computer will now run diagnosis, please wait.")
      time.sleep(3)
      with open("data/timeused.txt", "w") as diagnosis_data:
        os.system('clear')
        print("Diagnosis in progress...")
        time.sleep(2)
        diagnosis_data.write("")
        diagnosis_data.write("0")
        print("Diagnosis complete.")
        time.sleep(1)
        print("Rebooting...")
        time.sleep(2)
        os.system("clear")
        start()


def start():
  os.system('clear')
  time.sleep(2.4)
  print("BIOS startup count = 2.4 secs")
  time.sleep(2)
  print("booting PythonOS...")
  setup()
  logon()
  time.sleep(1)
  os.system("clear")
  with open("data/username.txt", "r") as read_username:
    username = read_username.read()
  print(f"Welcome, {username}! You are running PythonOS {version}.")
  time.sleep(0.5)
  print(
      "You may begin entering the commands. Type 'help' for a list of commands. Or, you may type'apps' to show a list of apps."
  )
  while True:
    command = input(r"C:\PythOS> ")
    if command == "help":
      print("commands:")
      print("help - shows this list.")
      print("apps - shows a list of apps.")
      print("shutdown - shuts down the computer.")
      print("shutdown -sys - shuts down the OS switches back to the Linux Console")
      print("pyver - shows the current version of PythonOS.")
      print("date - shows the current date.")
      print("time - shows the current time.")
      print("restart  /  reboot - restarts the computer.")
      print("cls  /  clear - clear the terminal(you can still use the computer normally.)")
      print("update log  /  changelog - check the changelog through this command.")
      print("sleep - put the computer to sleep, you can press Enter key to wake it up.")
      print("kill - forces the computer to shutdown.(can only be used by developers)")
      print("username - shows your username.")
      print("username -c - change your username.")
      print("check updates - check for updates.")
      print("devtoggle - toggle developer mode.")
      print("wipe data - wipes all the data and settings")
      print("wipe data -s - wipes all the data and settings, and then shutdown.")
      print("devrefresh - refresh the code (can only be used by developers)")
      print("raspi-config - Opens Raspberrry Pi Config Menu. (Can only be used by Raspberry Pi OS users)")
    elif command == "applications":
      print("applications:")
      print("random.py - open random number picker")
      print("calc.py - a simple calculator")
      print("quick notes.py - open quick notes")
      print("text_viewer.py - open text viewer")
      print("MD Player.py - open Media Player")
    elif command == "shutdown":
        shutdown_yn = input("Are you sure you want to FULLY shutdown? (y/n)>")
        if shutdown_yn == "y":
          print("Shutting down...")
          time.sleep(2)
          os.system("clear")
          os.system("sudo shutdown now")
        elif shutdown_yn == "n":
          print("Shutdown cancelled.")
          time.sleep(1)
        else:
          print("Invalid input.")
          print("shutdown cancelled")
          time.sleep(1)
    elif command == "exit":
      exit_ask = input("You sure you want to exit back to Linux?y/n>")
      if exit_ask == "y":
        print("Exiting...")
        sys.exit()
      elif command == "n":
        print("Exit Cancelled") 
        time.sleep(1)
      else:
        print("Exit Cancelled.")
        time.sleep(1)
    elif command == "pyver":
      print(f"PythonOS {version}")
      print("codename: QuantumLeap")
      print("y_ver.24")
      print("Copyright © 2024, python.org")
      print("All rights reserved.")
      print("This is a free operating system. It is not endorsed by python.org")
      print("you can download this software from https://github.com/milo1004/PythonOS.git")
      print("A legal copy of PythOS.")
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
    elif command == "random.py":
      os.system("python3 data/user/applications/App.random.py")
    elif "reboot" in command:
      if "-full" in command:
        reboot = input("Are you sure you want to FULLY reboot? y/n>")
        if reboot == "y":
            time.sleep(1)
            os.system("clear")
            print("rebooting...")
            time.sleep(1)
            os.system("clear")
            os.system("sudo reboot now")
        elif reboot == "n":
          print("Reboot cancelled")
          time.sleep(1)
        else:
            print("Invalid Input")
            print("Reboot cancelled")
      elif "-sys" in command:
        reboot = input("Are you sure you want to reboot? y/n>")
        if reboot == "y":
            time.sleep(1)
            os.system("clear")
            print("rebooting...")
            time.sleep(1)
            os.system("clear")
            start()
        elif reboot == "n":
          print("Reboot cancelled")
          time.sleep(1)
        else:
            print("Invalid Input")
            print("Reboot cancelled")
    elif command == "changelog":
      print(f"PythonOS {version} changelog:")
      print("Fixed bugs.")
      print("Optimized perfomance.")
      print("Deleted ClockGE due to bugs.")
      print("Type 'change password' to add / change your password.")
      print(
          "You can download the latest version in https://github.com/milo1004/PythonOS/releases/"
      )
      time.sleep(1)
    elif command == "sleep":
      sleep_confirm = input(
          "You can wake the computer by pressing Enter.(press enter to continue.)"
      )
      os.system("clear")
      sleep_response = input("")
      os.system("clear")
      print(f"Welcome back, {username}!")
    
    elif command == "":
      print("Invalid input.")
    elif command == "clear":
      os.system('clear')
    elif command == "cls":
      os.system('clear')
    elif command == "kill":
      with open("data/developer mode.txt", 'r') as kill:
        kill_allow = kill.read()
      if kill_allow == "True":
        os.system('clear')
        sys.exit()
      elif kill_allow == "False":
        print("You can't use 'kill' because developer mode is not turned on.")
        print("To turn on developer mode, type 'developer mode'")
        time.sleep(1)
      else:
        with open("data/developer mode.txt", 'w') as diagnosis:
          diagnosis.write("False")
          print(
              "You can't use 'kill' because developer mode is not turned on.")
          print("To turn on developer mode, type 'developer mode'")
          time.sleep(1)
    elif command == "username":
      print(f"Your username is: {username}")
    elif command == "username -c":
      username_choice = input("Do you want to change your username? y/n>")
      if username_choice == "y":
        username_choice2 = input(
            "There are two options: 1. Enter a new username. 2. Set the username as the username you are currnetly using on Windows.> "
        )
        if username_choice2 == "1":
          new_username = input("Please input new username>")
          if new_username == "":
            print(
                "If you input a blank username, PythonOS will call you 'user'."
            )
            username = "user"
            with open("data/username.txt", "w") as username_set:
              username_set.write("")
              username_set.write(username)
            print(f"Your username is set to: {username}")
            time.sleep(1)
          else:
            username = new_username
            with open("data/username.txt", "w") as username_set:
              username_set.write("")
              username_set.write(username)
            print(f"Your username is set to: {username}")
            time.sleep(1)
            os.system("clear")
        elif username_choice2 == "2":
          username = getpass.getuser()
          with open("data/username.txt", "w") as username_set:
            username_set.write("")
            username_set.write(username)
            print(f"Your username is set to: {username}")
            time.sleep(1)
            os.system("clear")
        else:
          print("Invalid input.")
          print("Username will not be changed.")
          time.sleep(1)
          os.system("clear")
    elif command == "check updates":
      print("Checking for updates...")
      time.sleep(1)
      try:
        print(f"Current Version:{version_name}")
        g_token = Github("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") #type:ignore
        repo = g_token.get_repo("milo1004/PythonOS")
        lateset = repo.get_latest_release()
        release_name = lateset.title
        print(f"Latest Version: {release_name}")
        latest_num = "".join(filter(str.isdigit, release_name))
        cur_num = "".join(filter(str.isdigit, version_name))
        if latest_num > cur_num:
          print("There is an update available.")
          print(
              "Please download the latest version from: https://github.com/milo1004/PythonOS"
          )
        elif latest_num < cur_num:
          with open("data/developer mode.txt", "r") as developer_mode:
            developer = developer_mode.read()
            if developer == "True":
              print("There are no updates available.")
            else:
              activate_dev = input(
                  "Looks like that you are a developer, do you want to turn on devleloper mode? y/n>"
              )
              if activate_dev == "y":
                with open("data/developer mode.txt", "w") as developer_mode:
                  developer_mode.write("")
                  developer_mode.write("True")
                with open("data/username.txt", "w") as developer_mode:
                  developer_mode.write("")
                  developer_mode.write(f"{username} - Developer")
                print("You are now a developer.")
              elif activate_dev == "n":
                print("You will not be a developer.")
              else:
                print("Invalid input.")
        elif latest_num == cur_num:
          print("There is no update available.")
          time.sleep(1)
        else:
          print("Failed to check for updates.")
          print("You can restart PythonOS to solve problem.")
          time.sleep(1)
      except:
        print(f"Current version: {version_name}")
        print("Failed to check for updates.")
        print("Please contact the developer or check internet connection.")
        time.sleep(1)
        os.system("clear")
      time.sleep(1)
    elif command == "devtoggle":
      with open("data/developer mode.txt", "w") as dev_mode:
        dev_mode.write("")
        with open("data/developer mode.txt", "r") as dev_mode_read:
          dev_mode_read.read()
        if dev_mode_read == "True":
          dev_mode.write("False")
          print("Developer mode is now off.")
        elif dev_mode_read == "False":
          dev_mode.write("True")
          print("developer mode turned on.")
    elif command == "MD Player.py":
      MDP_status = True
      mixer.init()
      print("Welcome to MD Player!")
      time.sleep(1)
      print("this application allows you to play music.")
      time.sleep(1)
      print("Note:")
      print("1. Type /kill to exit application.")
      print("2. Type /list to show list of music.")
      print("3. Type /random to play random music.")
      print("4. Type /pause to pause the music.")
      print("5. Type /resume to resume the music.")
      print("6. Type /stop to stop the music.")
      print(
          "6. If you want to add more or delete music, please copy and paste the music file to 'data/user/Media Player/'."
      )
      print("Music List:")
      music_list = os.listdir("data/user/Media Player/")
      for music_files in music_list:
        print(music_files)
      while MDP_status == True:
        music_selection = input("Type the music name here>")
        if music_selection == "/kill":
          mixer.music.stop()
          print("application killed.")
          time.sleep(1)
          MDP_status = False
          os.system("clear")
        elif music_selection == "/list":
          print("Music List:")
          for music_files in music_list:
            print(music_files)
        elif music_selection == "/random":
          mixer.music.load(
              f"data/user/Media Player/{random.choice(music_list)}")
          print(f"Now playing: {random.choice(music_list)}")
          Music_playing = True
          mixer.music.play()
          time.sleep(1)
        elif music_selection == "/pause":
          if Music_playing == True:
            mixer.music.pause()
            print("Music paused.")
            Music_playing = False
            time.sleep(1)
          else:
            print("No music is playing.")
            time.sleep(1)
        elif music_selection == "/resume":
          if Music_playing == False:
            mixer.music.unpause()
            print("Music resumed.")
            Music_playing = True
            time.sleep(1)
          else:
            print("No music is playing.")
            time.sleep(1)
        elif music_selection == "/stop":
          if Music_playing == True:
            mixer.music.stop()
            print("Music stopped.")
            Music_playing = False
            time.sleep(1)
          else:
            print("No music is playing.")
            time.sleep(1)
        else:
          try:
            mixer.music.load(f"data/user/Media Player/{music_selection}")
            print(f"Now playing: {music_selection}")
            mixer.music.play()
            Music_playing = True
          except:
            print("Invalid music name. Type /list to show list of music.")
            time.sleep(1)
    elif command == "change password":
      with open("data/user/account/password.txt", "r") as check_password:
        password_check = check_password.read()
        if password_check == "":
          set_password = input("Please input desired password:")
          with open("data/user/account/password.txt", "w") as password_set:
            print("Setting password...")
            password_set.write("")
            password_set.write(set_password)
            print("Password set!")
        else:
          input_old_pw = input("Please input old password>")
          with open("data/user/account/password.txt", "r") as check:
            old_pw = check.read()
            old_pw_correct = False
          while not old_pw_correct:
            if input_old_pw == old_pw:
              time.sleep(1)
              print("Old password correct!")
              set_new_pw = input("Please input new password>")
              print("Setting password...")
              with open("data/user/account/password.txt", "w") as password_set:
                password_set.write("")
                password_set.write(set_new_pw)
                print("Password set!")
                old_pw_correct = True
            else:
              print("Incorrect password, please try again.")
    elif command == "wipe data":
      reset_confirm = input(
          "This is SERIOUS: \nAre you sure you want to wipe all data? (y/n)")
      if reset_confirm == "y":
        print("wiping data...")
        with open("data/user/account/password.txt", "w") as password_reset:
          password_reset.write("")
        with open("data/timeused.txt", "w") as timeused_reset:
          timeused_reset.write("0")
        with open("data/username.txt", "w") as username_reset:
          username_reset.write("user")
        file_list = glob.glob("data/user/quick notes")
        for file in file_list:
          if os.path.isfile(file):
            os.remove(file)
            with open("data/user/quick notes/data.txt",
                      "w") as create_timeused:
              create_timeused.write(str(0))
            with open("data/developer mode.txt", "w") as developer_mode:
              developer_mode.write("False")
        time.sleep(1)
        print("Data wiped.")
        time.sleep(1)
        print("We will now reboot the computer.")
        time.sleep(1)
        print("Rebooting...")
        os.system("clear")
        time.sleep(1)
        start()
    elif command == "wipe data -s":
      reset_confirm = input(
          "This is SERIOUS: \nAre you sure you want to wipe all data? (y/n)")
      if reset_confirm == "y":
        print("wiping data...")
        with open("data/user/account/password.txt", "w") as password_reset:
          password_reset.write("")
        with open("data/timeused.txt", "w") as timeused_reset:
          timeused_reset.write(str(0))
        with open("data/username.txt", "w") as username_reset:
          username_reset.write("user")
        file_list = glob.glob("data/user/quick notes")
        for file in file_list:
          if os.path.isfile(file):
            os.remove(file)
            with open("data/user/quick notes/data.txt",
                      "w") as create_timeused:
              create_timeused.write(str(0))
            with open("data/developer mode.txt", "w") as developer_mode:
              developer_mode.write("False")
        time.sleep(1)
        print("Data wiped.")
        time.sleep(1)
        print("We will now FULLY shutdown the computer.")
        time.sleep(1)
        os.system('clear')
        os.system("sudo shutdown now")
    elif command == "quick_internal_update":
      with open("data/developer mode.txt", "r") as developer_mode:
        developer_mode_check = developer_mode.read()
      if developer_mode_check == "True":
        os.system("clear")
        time.sleep(1)
        os.system("python3 main.py")
      else:
        print(
            "You don't have permission to use this command unless you're in developer mode."
        )
    elif command == "text_view.pe":
      print("Welcome to Text Veiwer!")
      print("This application helps you to view text from files.")
      print("The directory is now located in 'quick notes'.")
      print("Please input the name of the file you want to view.")
      file_name = input(">")
      try:
        with open(f"data/user/quick notes/{file_name}.txt", "r") as read_file:
          print(read_file.read())
      except:
        print("File not found.")
    elif "+" in command:
      try:
        answer = eval(command)
        print(answer)
      except:
        print("Illegal command. Type 'help' for a list of commands.")
    elif "-" in command:
      try:
        answer = eval(command)
        print(answer)
      except:
        print("Illegal command. Type 'help' for a list of commands.")
    elif "*" in command:
      try:
        answer = eval(command)
        print(answer)
      except:
        print("Illegal command. Type 'help' for a list of commands.")
    elif "/" in command:
      try:
        answer = eval(command)
        print(answer)
      except:
        print("Illegal command. Type 'help' for a list of commands.")
    elif command == "boot_config":
      print("This can only be ran on Raspberry Pi OS.")
      try:
        os.system("sudo raspi-config")
      except:
        print("Cannot run raspberry pi config menu. Please check whether you have Raspberry Pi OS installed")
    else:
      print("Illegal command. Type 'help' for a list of commands.")
start()
