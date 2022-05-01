alphabet = {' ': ' ', '!': '!', 'a': 'f', 'b': 'g', 'c': 'h', 'd': 'i', 'e': 'j', 'f': 'k', 'g': 'l', 'h': 'm', 
            'i': 'n', 'j': 'o', 'k': 'p', 'l': 'q', 'm': 'r', 'n': 's', 'o': 't', 'p': 'u', 'q': 'v', 
            'r': 'w', 's': 'x', 't': 'y', 'u': 'z', 'v': 'a', 'w': 'b', 'x': 'c', 'y': 'd', 'z': 'e', 
            '.': '.', ',': ',', '-': '-', ';': ';'}

"""Using this substitutions, a plain text can be encrypted:

    Plaintext: programming python is fun!
    Encrypted text: uwtlwfrrnsl udymts nx kzs!"""

Plaintext = input("Please enter a sentence: ").lower()
Encrypted_text = ""

for letter in Plaintext:
    Encrypted_text += alphabet[letter]

print("The encrypted sentence is:", Encrypted_text)
