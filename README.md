# Wordle Solver
This is our project for [iNTUition v8.0](https://intuition-v8.devpost.com/) (2022)
<details>
  <summary><strong>More project releated info</strong></summary>
  
  Group Name: `def foo(c, l)`\
  Find out more at our Devpost [post](https://devpost.com/software/wordle-solver-telegram-bot).
</details>

### What is it?
It's a [telegram bot](https://t.me/WdSolver_bot) that can help you solve Wordle, by suggesting words to try. Just provide the bot with the words you tried, and the result of the words you tried which Wordle says.\
(Disclaimer: Sorry if our bot isn't running 24/7)\
**The API Key has been omitted, please use your own bot API key to run the code.

### Dependencies
|Library|Installation|
|---|---|
| [SciPy](https://pypi.org/project/scipy/) | `pip install scipy` |
| [wordfreq](https://pypi.org/project/wordfreq/) | `pip install wordfreq` |
| [python-telegram-bot](https://pypi.org/project/python-telegram-bot/) | `pip install python-telegram-bot` |


### References
#### For the wordle-solver algorithm
  - 3Blue1Brown
    - [Solving Wordle using information theory](https://www.youtube.com/watch?v=v68zYyaEmEA&t=720s)
    - [GitHub page](https://github.com/3b1b/videos/tree/master/_2022/wordle)
    - [List of possible words](https://github.com/3b1b/videos/blob/master/_2022/wordle/data/allowed_words.txt)
  - Website to find all possible combinations a word can be in Wordle
    - https://www.dcode.fr/permutations-with-repetitions

