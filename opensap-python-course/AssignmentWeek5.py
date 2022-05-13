"""
Vignère Cipher

Implement a program, that gets a text as input and in addition a keyword, which is the number of shifts.

    Implement a function encrypt_letter(), that gets a character and the key as input. The return value will be the encrypted character.
    Implement a function calculate_shifts(), that gets a letter as input parameter and returns the position of this letter in the alphabet (starting with a at position 0):
    Implement a function encrypt_text(), that gets a text and a keyword as input and returns the encrypted text. This function calls both calculate_shifts()and encrypt_letter()

Which text should be encrypted: Python is Really Beautiful
Which keyword should be used? Random
gygkcz if fqrlyb nvahwwrll
"""

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def encrypt_letter(character, shifts):
    if not character.isalpha():
        return character

    char_index = ALPHABET.find(character)
    result = (char_index + shifts) % len(ALPHABET)
    return ALPHABET[result]

def calculate_shifts(character):
    return ALPHABET.find(character)

def encrypt_text(text, key_word):
    text = text.lower()
    key_word = key_word.lower()

    encrypted_text = ""
    char_index = 0
    for letter in text:
        key_index = char_index % len(key_word)
        shifts = calculate_shifts(key_word[key_index])
        encrypted_text += encrypt_letter(letter, shifts)
        char_index += 1
    return encrypted_text

clear_text = input("Which text should be encrypted: ")
keyword = input("Which keyword should be used? ")
print(encrypt_text(clear_text, keyword))
