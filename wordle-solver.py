import sys

WORDLE_WORD_LENGTH = 5

status = {
    '0' : "wrong letter",
    '1' : "correct letter and position",
    '2' : "correct letter but wrong position",
}

class wordle_solver:

    attempts = {}

    def print_help(self):
        print("Usage:", sys.argv[0], "5-letter-word previous-word-result ...")
        print("\tTo represent results:")
        for i in status:
            print("\tType", i, "to represent", status[i])
        
    def start(self):
        for a in sys.argv:
            if a == sys.argv[0]:
                continue
            if len(a) != WORDLE_WORD_LENGTH:
                print("InputError:", a, "is not", WORDLE_WORD_LENGTH, "letters")
                print("Please check your inputs")
                return
        self.add_to_dict()
    
    
    def add_to_dict(self):
        i = 0
        num_of_pairs = (len(sys.argv) - 1) // 2
        while i < num_of_pairs:
            self.attempts[sys.argv[i*2 + 1]] = sys.argv[i*2 + 2]
            i  = i + 1
        print(self.attempts)
        
    def __init__(self):
        if (len(sys.argv) == 1):
            self.print_help()
        else:
            self.start()
        
if __name__ == "__main__":
    wordle_solver()