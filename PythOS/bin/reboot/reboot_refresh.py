import subprocess
import sys

try:
    subprocess.run("clear", shell=True, text=True, check=True, stderr=subprocess.DEVNULL)
    subprocess.run("python3 central.py", shell=True, text=True, check=True, stderr=subprocess.DEVNULL)
    sys.exit()
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")