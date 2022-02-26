from scipy.stats import entropy
import collections
import operator

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

def containsLettersAndPosition(guessedWord, index, d):
    mask = getMaskForWord(guessedWord, index)
    filteredList = {}

    for (key, values) in d.items():
       if all((c1 == "_") or (c1 == c2) for c1, c2 in zip(mask, key)):
            filteredList[key] = values
    return filteredList

def containsLetters(guessedWord, index, d):
    letters = getLetters(guessedWord, index)
    filteredDict = {}
    for (key, values) in d.items():
        if 0 not in [chars in key for chars in letters]:
            filteredDict[key] = values
    return filteredDict

def containsNone(guessedWord, index, d):
    letters = getLettersNotInAnswer(guessedWord, index)
    filteredDict = {}
    for (key, values) in d.items():
        if 1 not in [chars in key for chars in letters]:
            filteredDict[key] = values
    return filteredDict

def narrowWords(guessedWord, index, dict):
    filteredList = containsLettersAndPosition(guessedWord, index, containsLetters(guessedWord, index, containsNone(guessedWord, index, dict)))
    return filteredList

def getEntropy(word, mainList, listOfPermutes):
    arr = []
    for p in listOfPermutes:
        fList = narrowWords(word, p, mainList)
        arr.append(len(fList) / len(mainList))
    return entropy(arr, base=2)


class wordle_algo:

    words = {}
    permute = None

    def __init__(self):
        # All possible outcomes
        with open('permutations.txt', "r") as file:
            self.permute = file.readlines()
        
        # Get words in text file
        with open('words.txt', "r") as file:
            wordsRead = file.readlines()
            for word in wordsRead:
                self.words[word.strip()] = 0.00
    
    def start(self):
        currentDict = self.words
        iterate = 0
        while (iterate <= 4): 
            word = input("please input a word: ")
            num = input("please input the order, 0 for black, 1 for green, 2 for orange : ")
            currentDict = narrowWords(word, num, currentDict)
            if iterate >= 1:
                for (key, value) in currentDict.items():
                    currentDict[key] = getEntropy(key, currentDict, self.permute)
                currentDict = collections.OrderedDict(sorted(currentDict.items(), key=operator.itemgetter(1), reverse=True))
            print(currentDict)
            iterate += 1


if __name__ == "__main__":
    wordle_algo().start()