# coding=UTF-8
""" Python task 1 by Lukas Tyla / llukas.tyla@gmail.com
	Apskaičiuoti nurodytoje direktorijoje esančių failų statistiką ir ją išvesti į failą.
	Statistika: pirmiausia išvesti bendrai visuose failuose kokie ir kiek kartų pasikartoja
	a) žodžiai b) simboliai. Antra, į tą patį failą išvesti tą pąčią statistiką apskaičiuotą
	kiekvienam failui atskirai.
"""
# Imports
import os, sys, string, re
from collections import Counter
# The main program logic. Asks for a path and calls the functions to handle man logic
def mainLogic():
	path = input("Specify the directory path(current directory is '.'): ")
	filesInDirectory = os.listdir(path)
	if filesInDirectory is not None:
		print "File(s) in the directory: "
		for fileName in filesInDirectory:
		    print fileName
		    if fileName[0] is not '.':
		    	parseFile(fileName, path)
	else:
		print "You listed a wrong directory path"
# Function to read file contents
def parseFile(fileName, path):
	try:
		if os.path.isfile(os.path.join(path, fileName)):
			fileObject = open(os.path.join(path, fileName), 'r')
			fileText = fileObject.read()
			# Find words
			words = re.findall(r"[\w]+", fileText)
			wordCollection = Counter(words);
			print "===========Word details of {} file===========".format(fileName)
			for word, repetitions in sorted(wordCollection.items(), key=lambda x:x[1]):
				print word, "mentioned:", repetitions
			# Filter all characters that are not printable.
			text = filter(lambda x: x in string.printable, fileText)
			characterCollection = Counter(text)
			print "===========Character details of {} file===========".format(fileName)
			for character, repetitions in sorted(characterCollection.items(), key=lambda x:x[1]):
				print character, 'mentioned:', repetitions
	except IOError as e:
		print "I/O error({0}): {1}".format(e.errno, e.strerror)
	except ValueError:
		print "Could not convert data to an integer."
	except:
		print "Unexpected error:", sys.exc_info()[0]
		raise

askForDirectory()
