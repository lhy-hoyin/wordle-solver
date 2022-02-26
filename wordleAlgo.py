from scipy.stats import entropy
import collections
import operator

def getMaskForWord(guessedWord, index, n):
    mask = ""
    count = 0;
    for num in index:
        if num == n:
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
    notInAnswer = ""
    inAnswer = ""
    count = 0;
    for num in index:
        if num == '0':
            if count < len(guessedWord):
                if inAnswer.__contains__(guessedWord[count]) == False:
                    notInAnswer = notInAnswer + guessedWord[count]
        else:
            if count < len(guessedWord):
                inAnswer = inAnswer + guessedWord[count]
        count += 1
    
    for letter in notInAnswer:
        if inAnswer.__contains__(letter):
            notInAnswer = notInAnswer.replace(letter, "")

    print(notInAnswer)
    return notInAnswer

def containsLettersAndPosition(guessedWord, index, d):
    mask = getMaskForWord(guessedWord, index, '1')
    filteredList = {}

    for (key, values) in d.items():
       if all((c1 == "_") or (c1 == c2) for c1, c2 in zip(mask, key)):
            filteredList[key] = values
    return filteredList

def containsLetters(guessedWord, index, d):
    letters = getLetters(guessedWord, index)
    mask = getMaskForWord(guessedWord, index, '2')
    filteredDict = {}

    for (key, values) in d.items():
        if 0 not in [chars in key for chars in letters]:
            if not all((c1 == "_") or (c1 == c2) for c1, c2 in zip(mask, key)):
                filteredDict[key] = values

    return filteredDict

def containsNone(guessedWord, index, d):
    letters = getLettersNotInAnswer(guessedWord, index)
    filteredDict = {}
    for (key, values) in d.items():
        if 1 not in [chars in key for chars in letters]:
            filteredDict[key] = values 
    return filteredDict

def narrowWords(guessedWord, index, d):
    filteredList = d

    if (index.__contains__('0')):
        filteredList = containsNone(guessedWord, index, filteredList)
    if (index.__contains__('1')):
        filteredList = containsLettersAndPosition(guessedWord, index, filteredList)
    if (index.__contains__('2')):
        filteredList = containsLetters(guessedWord, index, filteredList)
    
    return filteredList

def getEntropy(word, mainList, listOfPermutes):
    arr = []
    for p in listOfPermutes:
        fList = narrowWords(word, p, mainList)
        arr.append(len(fList) / len(mainList))
    return entropy(arr, base=2)


if __name__ == "__main__":
    # All possible outcomes
    file = open('permutations.txt', "r")
    permute = file.readlines()
    file.close()
    
    # Get words in text file
    file = open('words.txt', "r")
    wordsRead = file.readlines()
    words = {}
    for word in wordsRead:
        words[word.strip()] = 0.00
    file.close()
    
    currentDict = words

    iterate = 0
    while (iterate <= 5): 
        word = input("please input a word: ").strip()
        num = input("please input the order, 0 for black, 1 for green, 2 for orange : ").strip()
        currentDict = narrowWords(word, num, currentDict)
        if iterate >= 1:
            for (key, value) in currentDict.items():
                currentDict[key] = getEntropy(key, currentDict, permute)
            currentDict = collections.OrderedDict(sorted(currentDict.items(), key=operator.itemgetter(1), reverse=True))

        print({k: currentDict[k] for k in list(currentDict)[:15]})
        iterate += 1
