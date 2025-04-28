import subprocess
import sys

try:
    with open("bin/arguments.txt", "r") as file:
        arguments = file.read().strip()
    
    # Split arguments into a list for safer execution
    cmd = ["cat"] + arguments.split()
    
    # Run the command and capture output
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        check=True  # This will raise CalledProcessError if command fails
    )
    
    # Print the output
    print(result.stdout)
    
except subprocess.CalledProcessError as e:
    print(f"Error: Command failed with exit code {e.returncode}")
    if e.stderr:
        print(f"Error message: {e.stderr}")
except FileNotFoundError:
    print("Error: The 'cat' command was not found")
except Exception as e:
    print(f"Error: {str(e)}")

sys.exit()