from wordle_solver import WORDLE_WORD_LENGTH, status_help_message, wordle_solver

class bot_logic:

    DEFAULT_SUGGEST_N_WORDS = 10

    flag_enter_word = True
    flag_enter_result = False
    entered_word, entered_result = "", ""
    possible_words = {}
    
    def __init__(self):
        self.solver = wordle_solver()
    
    def respond(self, input_text):
        if input_text.lower() in ("hi", "hey", "yoyoyo"):
            return "Hello"
        
        input_text = input_text.lower() # Change to lower characters
        input_text = input_text.strip() # remove leading/ending characters
        
        if ' ' in input_text:
            return "Oops! Looks like you entered more than 1 word"
        
        if len(input_text) != WORDLE_WORD_LENGTH:
            return "Oh no! You need to enter a " + str(WORDLE_WORD_LENGTH) + "-letter word"
        
        if self.flag_enter_word:
            if not input_text.isalpha():
                return "This doesn't look like a word :("
                
            self.entered_word = input_text
            self.toggle_status()
            return "What did Wordle say about the word?\nEnter in this format:\n• 0: Wrong letter choice\n• 1: Correct letter position\n• 2: Wrong letter position\nExample: 10200"
        
        elif self.flag_enter_result:
            if not input_text.isdecimal():
                return "Hmm...I don't quite understand this format :(\nType /format for more info" 
                # maybe use inline kb here(??)
            #fixme: code supposed to check that no other digits are input
            # except for 0, 1, 2
            '''
            if not any((d in set("012")) for d in input_text):
                return "wrong digit(s)"
            '''
            if input_text == "11111":
                return "Yay!!! You got the correct answer already!\n(Hint: type /start to try the next one)"
            
            self.entered_result = input_text
            return self.run_solver()
        
        return "default-response"
       
    def run_solver(self):
        assert len(self.entered_word) != 0
        assert len(self.entered_result) != 0
        self.possible_words = self.solver.try_word({ self.entered_word : self.entered_result })
        self.toggle_status()
        return self.suggest_words()
    
    def suggest_words(self, num = DEFAULT_SUGGEST_N_WORDS):
        length = len(self.possible_words.items())
        limit = (num if num < length else length)
        
        if length <= 0:
            return "Sorry, I can't think of anything :'("
        
        # Retrieve suggestions from dict
        suggestions = list(self.possible_words.items())[:limit]
        
        reply = "I suggest trying " + suggestions[0][0] + "\n"
        reply += "You can also try:"
        
        for word_pair in suggestions:
            if word_pair != suggestions[0]:
                reply += "\n" + word_pair[0]
        
        #TODO: can also display numbers to users (to make a better choice)
        return reply
    
    def result_format_message_str(self):
        return status_help_message()
    
    def toggle_status(self):
        self.flag_enter_word = not self.flag_enter_word
        self.flag_enter_result = not self.flag_enter_result

if __name__ == "__main__":
    bot = bot_logic()
    while(True):
        print(bot.respond(input("> ")))