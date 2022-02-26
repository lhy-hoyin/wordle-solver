import sys

WORDLE_WORD_LENGTH = 5

status = {
    '0' : "wrong letter",
    '1' : "correct letter and position",
    '2' : "correct letter but wrong position",
}

class wordle_solver:

    attempts = {}

    def __init__(self):
        if (len(sys.argv) == 1):
            self.print_help()
        else:
            self.start()
    
    def start(self):
        for arg in sys.argv:
            if arg == sys.argv[0]:
                continue
            if len(arg) != WORDLE_WORD_LENGTH:
                print("InputError:", arg, "is not", WORDLE_WORD_LENGTH, "letters")
                print("Please check your inputs")
                return
        self.add_to_dict()
        print(self.get_attempts())
    
    def add_to_dict(self):
        i = 0
        num_of_pairs = (len(sys.argv) - 1) // 2
        while i < num_of_pairs:
            key = sys.argv[i*2 + 1].upper()
            value = sys.argv[i*2 + 2]
            self.attempts[key] = value
            i  = i + 1
    
    def print_help(self):
        print("Usage:", sys.argv[0], "word result ...")
        print("Ensure that each word and results is", WORDLE_WORD_LENGTH, "letters")
        print("To represent results:")
        for i in status:
            print("Type", i, "to represent", status[i])
    
    def get_attempts(self):
        return self.attempts
        
if __name__ == "__main__":
    wordle_solver()