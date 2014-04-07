# coding=UTF-8
""" Python task 1 by Lukas Tyla / llukas.tyla@gmail.com
	Apskaičiuoti nurodytoje direktorijoje esančių failų statistiką ir ją išvesti į failą.
	Statistika: pirmiausia išvesti bendrai visuose failuose kokie ir kiek kartų pasikartoja
	a) žodžiai b) simboliai. Antra, į tą patį failą išvesti tą pąčią statistiką apskaičiuotą
	kiekvienam failui atskirai.
"""
#import os library to be able to list the files within a directory
import os
import sys
from collections import Counter
def askForDirectory():
	directory = input("Specify the directory path(current directory is '.'): ")
	filesInDirectory = os.listdir(directory)
	if filesInDirectory is not None:
		print "File(s) in the directory: "
		for fileName in filesInDirectory:
		    print fileName
		    if fileName[0] is not '.':
		    	openFile(fileName)
	else:
		print "You listed a wrong directory path"
	
def openFile(fileName):
	try:
		fileObject = open(fileName, 'r')
		lines = fileObject.readlines()
		for line in lines:
			# Filter all characters that are not letters.
			textContent = filter(lambda x: x in string.letters, text.lower())
			c = Counter(textContent)
			for letter, repetitions in c.iteritems():
				print letter, repetitions
	except IOError as e:
		print "I/O error({0}): {1}".format(e.errno, e.strerror)
	except ValueError:
		print "Could not convert data to an integer."
	except:
		print "Unexpected error:", sys.exc_info()[0]
		raise
	finally:
		fileObject.close()
askForDirectory()
