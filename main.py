# coding=UTF-8
""" Python task 1 by Lukas Tyla / llukas.tyla@gmail.com
    Apskaičiuoti nurodytoje direktorijoje esančių failų statistiką ir ją
    išvesti į failą. Statistika: pirmiausia išvesti bendrai visuose failuose
    kokie ir kiek kartų pasikartoja a) žodžiai b) simboliai. Antra, į tą patį
    failą išvesti tą pąčią statistiką apskaičiuotą kiekvienam failui atskirai.
"""
# Imports
import os
import sys
import string
import re
from collections import Counter
# Global variables
counter = 0
allWords = None
allCharacters = None


# The main program logic. Asks for path and calls parseFile function
def mainLogic():
    path = input("Specify the directory path (current directory is '.'): ")
    filesInDirectory = os.listdir(path)
    if filesInDirectory is not None:
        print "File(s) and folder(s) in the directory: "
        for fileName in filesInDirectory:
            # Prints all files and folders
            print fileName
            # If fileName does not point to a folder - parse file
            if fileName[0] is not '.':
                parseFile(fileName, path)
    else:
        print "You listed a wrong directory path"


# Read file contents and call outputResults function to output results
def parseFile(fileName, path):
    global allWords
    global allCharacters
    # If it is a file - read contents
    if os.path.isfile(os.path.join(path, fileName)):
        try:
            fileObject = open(os.path.join(path, fileName), 'r')
            fileText = fileObject.read()
            # Find words (at least two characters after one another)
            words = re.findall(r"[\w]{2,}", fileText)
            wordCollection = Counter(words)
            if allWords is not None:
                allWords.update(wordCollection)
            else:
                allWords = wordCollection
            outputContent = "===========Word details of {} file" \
                "===========\n".format(fileName)
            for word, repetitions in sorted(
                    wordCollection.items(),
                    key=lambda x: x[1]):
                outputContent += word + " mentioned: " + str(repetitions) + \
                    "\n"
            outputResults(outputContent)
            # Find printable characters
            text = filter(lambda x: x in string.printable, fileText)
            characterCollection = Counter(text)
            if allCharacters is not None:
                allCharacters.update(characterCollection)
            else:
                allCharacters = characterCollection
            outputContent = "===========Character details of {} file" \
                "===========\n".format(fileName)
            for character, repetitions in sorted(
                    characterCollection.items(),
                    key=lambda x: x[1]):
                outputContent += character + " mentioned: " + \
                    str(repetitions) + "\n"
            outputResults(outputContent)
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
        finally:
            fileObject.close()


# Output the provided contents into results file.
def outputResults(content):
    global counter
    # If it is the first run - overwrite file
    if counter == 0:
        openType = "w"
    else:
        openType = "a"
    try:
        outputFile = open("results.txt", openType)
        outputFile.write(content + "\n")
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise
    finally:
        outputFile.close()
        counter += 1


# Outputs the total results of words and characters into the results file
def outputTotalResults():
    global allWords
    global allCharacters
    try:
        outputFile = open("results.txt", "a")
        outputWordsContent = "\n==========TOTAL word details for all files" \
            "==========\n\n"
        for word, repetitions in sorted(allWords.items(), key=lambda x: x[1]):
            outputWordsContent += word + " mentioned: " + str(repetitions) + \
                "\n"
        outputFile.write(outputWordsContent + "\n")
        outputCharactersContent = "\n==========TOTAL character details for" \
            "all files==========\n\n"
        for character, repetitions in sorted(
                allCharacters.items(),
                key=lambda x: x[1]):
            outputCharactersContent += character + " mentioned: " + \
                str(repetitions) + "\n"
        outputFile.write(outputCharactersContent)
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise
    finally:
        outputFile.close()


# Main function - runs the program
def main():
    mainLogic()
    outputTotalResults()
    print "Output results were written into the results file."

if __name__ == "__main__":
    main()
