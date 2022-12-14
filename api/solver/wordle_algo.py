import collections

from scipy.stats import entropy
import wordfreq

# Acknowledgements: 
#   - 3Blue1Brown
#       - Solving Wordle using information theory (https://www.youtube.com/watch?v=v68zYyaEmEA&t=720s)
#       - GitHub page: (https://github.com/3b1b/videos/tree/master/_2022/wordle)
#       - List of possible words (https://github.com/3b1b/videos/blob/master/_2022/wordle/data/allowed_words.txt)
#   - Website to find all possible combinations a word can be in Wordle
#       - https://www.dcode.fr/permutations-with-repetitions

def get_mask_for_word(guessed_word, index, n):
    mask = ""
    count = 0;
    for num in index:
        if num == n:
            mask = mask + guessed_word[count]
        else:
            mask = mask + "_"
        count += 1
    return mask

def get_letters(guessed_word, index):
    letters = ""
    count = 0;
    for num in index:
        if num == '2':
            letters = letters + guessed_word[count]
        count += 1
    return letters

def get_letters_not_in_answer(guessed_word, index):
    not_in_answer = ""
    in_answer = ""
    count = 0;
    for num in index:
        if num == '0':
            if count < len(guessed_word):
                if in_answer.__contains__(guessed_word[count]) == False:
                    not_in_answer = not_in_answer + guessed_word[count]
        else:
            if count < len(guessed_word):
                in_answer = in_answer + guessed_word[count]
        count += 1
    
    for letter in not_in_answer:
        if in_answer.__contains__(letter):
            not_in_answer = not_in_answer.replace(letter, "")

    return not_in_answer

def contains_letters_and_position(guessed_word, index, d):
    mask = get_mask_for_word(guessed_word, index, '1')
    filtered_list = {}

    for (key, values) in d.items():
       if all((c1 == "_") or (c1 == c2) for c1, c2 in zip(mask, key)):
            filtered_list[key] = values
    return filtered_list

def contains_letters(guessed_word, index, d):
    letters = get_letters(guessed_word, index)
    mask = get_mask_for_word(guessed_word, index, '2')
    filtered_dict = {}

    for (key, values) in d.items():
        if 0 not in [chars in key for chars in letters]:
            if not all((c1 == "_") or (c1 == c2) for c1, c2 in zip(mask, key)):
                filtered_dict[key] = values

    return filtered_dict

def containsNone(guessed_word, index, d):
    letters = get_letters_not_in_answer(guessed_word, index)
    filtered_dict = {}
    for (key, values) in d.items():
        if 1 not in [chars in key for chars in letters]:
            filtered_dict[key] = values 
    return filtered_dict

def narrow_words(guessed_word, index, d):
    filtered_list = d

    if (index.__contains__('0')):
        filtered_list = containsNone(guessed_word, index, filtered_list)
    if (index.__contains__('1')):
        filtered_list = contains_letters_and_position(guessed_word, index, filtered_list)
    if (index.__contains__('2')):
        filtered_list = contains_letters(guessed_word, index, filtered_list)
    
    return filtered_list

def getEntropy(word, main_list, list_of_permutes):
    arr = []
    for p in list_of_permutes:
        fList = narrow_words(word, p, main_list)
        arr.append(len(fList) / len(main_list))
    return entropy(arr, base=2)    
    
class wordle_algo:
    
    words = {}
    permute = None
    current_dict = None

    def __init__(self):
        # All possible outcomes
        with open('solver\permutations.txt', "r") as file:
            self.permute = file.readlines()
        
        # Get words in text file
        with open('solver\words.txt', "r") as file:
            wordsRead = file.readlines()
            for word in wordsRead:
                freq = wordfreq.zipf_frequency(word.strip(), 'en', 'large')
                self.words[word.strip()] = [0.00, freq, freq]
        
        # Sort the words by entropy + word frequency      
        self.words = collections.OrderedDict(
                sorted(self.words.items(), 
                key=lambda item: item[1][2],
                reverse=True))
        
        # Start first time
        self.restart()
    
    def get_possible_words(self, word_result):
        assert len(word_result) == 1
        for (word, result) in word_result.items():
            return narrow_words(word, result, self.current_dict)
        return self.current_dict
    
    def compute_entropy(self):
        # calculate entropy for each possible word
        for (key, value) in self.current_dict.items():
            en = getEntropy(key, self.current_dict, self.permute)
            self.current_dict[key] = [en, value[1], en + value[1]]
        
        #Sort the words by entropy + word frequency 
        self.current_dict = collections.OrderedDict(
                sorted(self.current_dict.items(), 
                key=lambda item: item[1][2],
                reverse=True))
    
    def restart(self):
        self.current_dict = self.words
        return self
        
    def test(self):
        iterate = 0
        while (iterate <= 5): 
            word = input("please input a word: ")
            num = input("please input the order, 0 for black, 1 for green, 2 for orange : ")
            self.current_dict = self.get_possible_words({word:num})
            # note: we only calc entropy after 1st iteration, 
            # cos it takes for the first one (too many words)
            if iterate >= 1:
                self.compute_entropy() # note: we only calc entropy after 1st iteration, cos it takes for the first one (too many words)
            iterate += 1
            print(self.current_dict)

if __name__ == "__main__":
    wordle_algo().test()
