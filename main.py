# coding=UTF-8
""" Python task 1 by Lukas Tyla / llukas.tyla@gmail.com
	Apskaičiuoti nurodytoje direktorijoje esančių failų statistiką ir ją išvesti į failą.
	Statistika: pirmiausia išvesti bendrai visuose failuose kokie ir kiek kartų pasikartoja
	a) žodžiai b) simboliai. Antra, į tą patį failą išvesti tą pąčią statistiką apskaičiuotą
	kiekvienam failui atskirai.
"""
#import os library to be able to list the files within a directory
import os
def askForDirectory():
	directory = input("Specify the directory path(current directory is '.'): ")
	filesInDirectory = os.listdir(directory)
	if filesInDirectory is not None:
		print "File(s) in the directory: "
		for fileName in filesInDirectory:
		    print fileName
	else:
		print "You listed a wrong directory path"
	

askForDirectory()