import os
import sys
import subprocess

try:
    subprocess.run("reboot", shell=True, text=True, check=True, stderr=subprocess.DEVNULL)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")