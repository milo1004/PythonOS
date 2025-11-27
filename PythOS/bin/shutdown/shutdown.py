import os
import time

i = input("Are you sure you want to shutdown?(yn)")
if i.lower() == "y":
	print("See you next time!")
	time.sleep(1)
	os.system("shutdown now")
else:
	print("Shutdown aborted.")
