import os

print("PythOS NewCore")
print("Available commands:")
for cmds in os.listdir("bin"):
    if cmds.endswith(".py"):
        pass
    elif cmds.endswith(".txt"):
        pass
    else:
        print(f"  {cmds}")