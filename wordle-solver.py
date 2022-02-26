import sys
import argparse

WORDLE_WORD_LENGTH = 5

status = {
    '0' : "wrong letter",
    '1' : "correct letter and position",
    '2' : "correct letter but wrong position",
}

def status_help_message():
    help_message = "Results of the word, using:"
    for i in status:
        help_message = help_message + "\n" + i + " to represent " + status[i]
    return help_message

class wordle_solver:

    attempts = {}

    def __init__(self):
        parser = argparse.ArgumentParser(
            formatter_class=argparse.RawTextHelpFormatter,
            epilog = "Positional arguments can be repeated (following the correct positions)")
        parser.add_argument("word",
            help = str(WORDLE_WORD_LENGTH) + "-letter word you tried")
        parser.add_argument("result",
            help = status_help_message())
            
        if (len(sys.argv) == 1):
            parser.print_help()
        else:
            self.start_auto()
    
    def start_auto(self):
        for arg in sys.argv:
            if arg is sys.argv[0]:
                continue
            if len(arg) != WORDLE_WORD_LENGTH:
                print("InputError:", arg, "is not", WORDLE_WORD_LENGTH, "letters")
                print("Please check your inputs")
                return
        self.auto_add_to_dict()
    
    def auto_add_to_dict(self):
        i = 0
        num_of_pairs = (len(sys.argv) - 1) // 2
        while i < num_of_pairs:
            key = sys.argv[i*2 + 1].lower()
            value = sys.argv[i*2 + 2]
            self.attempts[key] = value
            i  = i + 1
    
    # MUST ensure that key is all lower letters
    def add_to_dict(self, key_value):
        for k in key_value.keys():
            assert len(k) == WORDLE_WORD_LENGTH
            assert k == k.lower()
        for v in key_value.values():
            assert len(v) == WORDLE_WORD_LENGTH
        self.attempts.update(key_value)
    
    def get_attempts(self):
        return self.attempts
        
if __name__ == "__main__":
    solver = wordle_solver()
    print(solver.get_attempts())
