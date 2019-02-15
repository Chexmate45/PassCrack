import os
import sys

if len(sys.argv) != 2:
        sys.exit("Argument usage: python main.py (txt directory) (password to c$

passList = open("list.txt", "r")
for line in passList:
        if (line.strip() == str(sys.argv[2])):
                print("Password found: " + line)
                break
        print(line)
