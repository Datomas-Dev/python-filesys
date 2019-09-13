"""
filesys.py
Date: 9/12/2019
Author: David T.

Provides a menu-driven too for navigating a file system and gathering information on files.
	
"""

import os, os.path

QUIT = '7'
COMMANDS = ('1','2','3','4','5','6','7')
MENU = """
	1 List the current directory
	2 Move up
	3 Move down
	4 Number of files in the directory
	5 Size of the directory in bytes
	6 Search for a filename
	7 Quit the program
	"""

def main():
	while True:
		print("\n"+os.getcwd())
		print(MENU)
		command = acceptCommand()
		runCommand(command)
		if command == QUIT:
			print("Exiting.")
			break

def acceptCommand():
	""" Inputs and returns a legitimate command value """
	command = input("Enter a number: ")
	if command in COMMANDS:
		return command
	else:
		print("Error: command not recognized.")
		return acceptCommand()

def runCommand(command):
	""" Selects and runs a command. """
	if command == '1':
		listCurrentDir(os.getcwd())
	elif command == '2':
		moveUp()
	elif command == '3':
		moveDown(os.getcwd())
	elif command == '4':
		print("The total number of files is ",countFiles(os.getcwd()))
	elif command == '5':
		print("The total number of bytes is ",countBytes(os.getcwd()))
	elif command == '6':
		target = input("Enter the search string: ")
		fileList = findFiles(target,os.getcwd())
		if not fileList:
			print("No files found")
		else:
			for f in fileList:
				print(f)

def listCurrentDir(dirName):
	""" Prints a list of the cwd's contents """
	lyst = os.listdir(dirName)
	for element in lyst:
		print(element)

def moveUp():
	""" Moves up to the parent directory """
	os.chdir("..")

def moveDown(currentDir):
	""" Moves down to the named subdirecory if it exists """
	newDir = input("Enter the directory name: ")
	if os.path.exists(currentDir+os.sep+newDir) and os.path.isdir(newDir):
		os.chdir(newDir)
	else:
		print("Error: no such directory")

def countFiles(path):
	""" Return the number of files in the cwd and all its subdirectories """
	count = 0
	lyst = os.listdir(path)
	for element in lyst:
		if os.path.isfile(element):
			count+=1
		else:
			os.chdir(element)
			count+=countFiles(os.getcwd())
			os.chdir("..")
	return count;

def countBytes(path):
	""" Return the number of files in the cwd and all its subdirectories """
	count = 0
	lyst = os.listdir(path)
	for element in lyst:
		if os.path.isfile(element):
			count+=os.path.getsize(element)
		else:
			os.chdir(element)
			count+=countBytes(os.getcwd())
			os.chdir("..")
	return count;

def findFiles(target,path):
	""" Returns a list of filenames that contain the target string in the cwd and all its subdirectories """
	files = []
	lyst = os.listdir(path)
	
	for element in lyst:
		if os.path.isfile(element):
			if target in element:
				files.append(path+os.sep+element)
		else:
			os.chdir(element)
			files.extend(findFiles(target,os.getcwd()))
			os.chdir("..")
	return files

main()