import os
print("================================")
print(" FILE NOT FOUND ERROR LAB")
print("================================")
print("FileNotFoundError happens when:")
print("1. File does not exist")
print("2. Wrong file path")
print("3. Typo in filename")
print("================================")
print("CHECKING FILES:")
files = ["firewall.py","network_info.py","missing.py"]
for f in files:
    if os.path.exists(f):
        print(f, ": FOUND")
    else:
        print(f, ": NOT FOUND - FileNotFoundError!")
print("================================")
print("RULE: Always check file exists first!")
