"""
Your task for the final assignment is to implement a Wordle clone in Python. The basis for your version of Wordle is the file 5_letter_words.txt [1]. It contains more than 5.700 five letter words. In order to build your version of Wordle perform the following steps:

    Implement a function word_list() that reads the 5_letter_words.txt file and returns a list of the words in the file.
    Implement a function random_word() that takes a list of words as a parameter and returns a random word from this list.
    Implement a function is_real_word() that takes two parameters, a guess and a word list 
    and returns True if the word is in the word list and False otherwise.
    Implement a function check_guess() that takes two parameters. The first is the guessed word and the second is the word the user has to find. 

    If a letter is used twice in the guessed word and exists only once in the word to be found, then only one letter in the return string is marked. 
    In case one of the two letters is positioned correctly, then this letter is marked with an X in the return string. 
    For example, check_guess("carat", "train") should return _OO_O. Another example, check_guess("taunt", "train") should return XO_O_

    Implement a function next_guess() that takes a word list as a parameter. 
    The function asks the user for a guess, converts the guess to lower case and checks if the guess is in the word list. If this is the case, the guess is returned. 
    Otherwise, the function asks the user for another guess.

    Implement a function play() that:

    Uses the functions word_list and random_word to select a random 5 letter word.
    Asks the user for a guess using the next_guess function.
    Checks each guess using the check_guess function and shows the result to the user.
    Checks if the users guessed the right word with six guesses or less. If yes, the user wins and the function prints You won!. 
    Otherwise the user loses and the function prints You lost! as well as The word was: followed by word the user had to find.
The result of the function check_guess is not correct. The function should return '_O_XO' for a guess of 'cocoa' and the word 'taboo'.
"""

import random

def word_list():
    with open("5_letter_words.txt", "r") as ifile:
        wordlist = []
        for line in ifile:
            line = line.strip()
            wordlist.append(line)
    return wordlist

def random_word(wordlist):
    return random.choice(wordlist)

def is_real_word(word, wordlist):
    return word in wordlist

def check_guess(guess, finded_word):
    result = ""
    i = 0
    temp_finded_word = finded_word
    for letter in guess:
        if letter in temp_finded_word:
            if letter == finded_word[i]:
                result += "X"
            else:
                result += "O"
            temp_finded_word = temp_finded_word.replace(letter, "_", 1)
        else:
            result += "_"
        i += 1
    return result

def next_guess(wordlist):
    guess = input("Please enter a guess: ").lower()
    while not is_real_word(guess, wordlist):
        print("That's not a real word!")
        guess = input("Please enter a guess: ").lower()
    return guess

def play():
    list_of_words = word_list()
    finded_word = random_word(list_of_words)

    for _ in range(6):
        guess = next_guess(list_of_words)
        print(check_guess(guess, finded_word))
        if guess == finded_word:
            print(("You won!"))
            break

    if guess != finded_word:
        print(("You lost!"))
        print("The word was: ", finded_word)

play()
