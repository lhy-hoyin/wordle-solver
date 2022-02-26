from asyncio import FastChildWatcher
import PyDictionary as pypi
import numpy as np

#get words in text file
file = open('words.txt', "r")
wordsRead = file.readlines()
words = {}
for word in wordsRead:
    words[word.strip()] = 0.00

def getMaskForWord(guessedWord, index):
    mask = ""
    count = 0;
    for num in index:
        if num == '1':
            mask = mask + guessedWord[count]
        else:
            mask = mask + "_"
        count += 1
    return mask

def getLetters(guessedWord, index):
    letters = ""
    count = 0;
    for num in index:
        if num == '2':
            letters = letters + guessedWord[count]
        count += 1
    return letters

def getLettersNotInAnswer(guessedWord, index):
    letters = ""
    count = 0;
    for num in index:
        if num == '0':
            letters = letters + guessedWord[count]
        count += 1
    return letters

def containsLettersAndPosition(guessedWord, index, dict):
    mask = getMaskForWord(guessedWord, index)
    print(mask)
    filteredList = {}

    for (key, values) in dict.items():
       if all((c1 == "_") or (c1 == c2) for c1, c2 in zip(mask, key)):
            filteredList[key] = values
    return filteredList

def containsLetters(guessedWord, index, dict):
    letters = getLetters(guessedWord, index)
    filteredList = {}
    for (key, values) in dict.items():
        if 0 not in [chars in key for chars in letters]:
            filteredList[key] = values
    return filteredList

def containsNone(guessedWord, index, dict):
    letters = getLettersNotInAnswer(guessedWord, index)
    filteredList = {}
    for (key, values) in dict.items():
        if 1 not in [chars in key for chars in letters]:
            filteredList[key] = values
    return filteredList

def narrowWords(guessedWord, index, dict):
    filteredList = containsNone(guessedWord, index, containsLetters(guessedWord, index, containsLettersAndPosition(guessedWord, index, dict)))
    return filteredList

first = narrowWords("tared", "00000", words)
second = narrowWords("yogic", "00020", first)
third = narrowWords("fusil", "00221", second)
fourth = narrowWords("shill", "20222", third)
print(fourth)
