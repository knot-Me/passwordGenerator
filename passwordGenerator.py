#!/bin/python3
import random
import os
import sys
import time
lowerLetterList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
upperLetterList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numberList = ["1","2","3","4","5","6","7","8","9","0"]
specialCharList = ["*", "+", "°", "_", "-" , ",", ":", ".", "?", "^", "~", "#", "!", "£", "$", "%", "€", "@"] 
try:
	print("\n\nMade by: ")
	print("\033[1;32;40m  |                   |     \  |       \n  |  /  __ \    _ \   __|  |\/ |   _ \ \n    <   |   |  (   |  |    |   |   __/ \n _|\_\ _|  _| \___/  \__| _|  _| \___|") 
 
	mainmenu = input("Press enter to continue...")
	if(mainmenu != None):
		clear = "clear"
		os.system(clear)

	passwdLength = int(input("\033[1;31;40mInsert the password length: (Range 8-80) \033[0;37;40m"))
	while(passwdLength in range(8, 80)):

		add = lowerLetterList + upperLetterList + numberList + specialCharList

		generator = random.sample(add,passwdLength)

		password= "".join(generator)
		print("\033[0;37;40mGenerating the password ...")
		time.sleep(1.2)
		print("\033[0;32;40m")
		print(password)
		file=int(input("\n\033[1;31;40mDo you want to create a file that stores the account:\n\033[1;31;40m1)\033[0;37;40mCreate file\n\033[1;31;40m2)\033[0;37;40mDo you already have it?\n\033[1;31;40m3)\033[0;37;40mExit\n\n"))
		while(file in range(1,3)):
			if(file == 1):
				email=str(input("\033[1;31;40mInsert the email where you used the password:\n\033[0;37;40m"))
				site=str(input("\033[1;31;40mInsert the site where you used the credentials:\n\033[0;37;40m"))
				fileEXT = str(input("\033[1;31;40mInsert the name, or the PATH, where to save the file (example.txt):\n\033[0;37;40m"))
			
				cmd="echo Sito: " +site+ "\rEmail: " +email+ "\rPassword: " +password+  " > " +fileEXT
				cmdLine="echo \r--------------------------------------------------------------------- >> " +fileEXT
				os.system(cmd)
				os.system(cmdLine)
				print("File created and saved successfully, name file: "+fileEXT)
				time.sleep(1.1)
				sys.exit(0)
			
			elif(file == 2):
				email=str(input("\033[1;31;40mInsert the email where you used the password:\n\033[0;37;40m"))
				site=str(input("\033[1;31;40mInsert the site where you used the credentials:\n\033[0;37;40m"))
				fileEXT = str(input("\033[1;31;40mInsert the name, or the PATH, where to save the file (example.txt):\n\033[0;37;40m"))
		
				cmd="echo Sito: " +site+ "\rEmail: " +email+ "\rPassword: " +password+  " >> " +fileEXT
				cmdLine="echo \r--------------------------------------------------------------------- >> " +fileEXT
				os.system(cmd)
				os.system(cmdLine)
				print("File saved successfully, name file: "+fileEXT)
				time.sleep(1.1)
				sys.exit(0)

#Else if(file)
			elif(file == 3):
				print("\033[1;33;40mExiting...")
				time.sleep(1.1)
				sys.exit(0)

#Second while's break (file)
			break


#First while's break (passwdLength)	
		break		
		
except KeyboardInterrupt:
	print("\n\033[1;33;40mExiting...\nCTRL+C")
	time.sleep(1.1)
	sys.exit(0)
			
			
			
			
			
			