def bot_respond(input_text):
    input_text = input_text.lower() # Change to lower characters
    input_text = input_text.strip() # remove leading/ending characters
    
    if ' ' in input_text:
        return "Sorry! You can only enter 1 word :("
    
    if len(input_text) != 5:
        return "You need to enter a 5-letter word"
    
    print("responding")
    return "hello"