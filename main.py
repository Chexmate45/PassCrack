import os
import sys

if len(sys.argv) != 4:
	sys.exit("Argument usage: python main.py (txt directory) (password to crack) (name of the word list file not including .txt")

for root,dir, files in os.walk(sys.argv[1]):
	for file in files:
		if (file.endswith('.txt') and file.startswith(sys.argv[3])):
			file = os.path.join(root, file)


passList = open(file, "r")
for line in passList:
	if (line.strip() == str(sys.argv[2])):
		print("Password found: " + line)
		break
	print(line)

