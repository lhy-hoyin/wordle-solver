def sample_responses(input_text):
    user_msg = str(input_text).lower()
    length = len(user_msg)

    if user_msg in ("hi", "hello", "hey"):
        return "Hello"

    if length != 5:
        return "Invalid Wordle try, please start over"

    if length == 5:
        wordle_x = user_msg
        return 'Entered word:', wordle_x


def wordlepositioncheck(input_text):
    wpos_v = int(input_text)
    return "Entered position:", wpos_v