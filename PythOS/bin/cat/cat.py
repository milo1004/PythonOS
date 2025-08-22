import os

with open("bin/arguments.txt","r") as read_file:
    file = read_file.read()

try:
    # Check if the file path is relative to PythOS 6.0R
    if not file.startswith("PythOS 6.0R"):
        file = os.path.join("PythOS 6.0R", file)
    
    with open(file, "r") as read_file:
        print(read_file.read())
except FileNotFoundError:
    # Try with absolute path
    try:
        current_dir = os.getcwd()
        with open(current_dir,"r") as read_file:
            current_dir = read_file.read()
        if "PythOS 6.0R" in current_dir:
            # Extract the path after PythOS 6.0R
            print(current_dir)
            base_path = current_dir.split("PythOS 6.0R")[0]
            full_path = os.path.join(base_path, file)
            with open(full_path, "r") as read_file:
                print(read_file.read())
        else:
            print(f"Error: File '{file}' not found")
    except Exception as e:
        print(f"Error: {str(e)}")
except Exception as e:
    print(f"Error: {str(e)}")
    
