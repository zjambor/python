import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter: row.code for (index, row) in nato_alphabet_df.iterrows()}

print(nato_alphabet)

for (letter, code) in nato_alphabet.items():
    print(f"letter: {letter}, code: {code}")

# 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Please enter a word: ").upper()
code_words = [nato_alphabet[letter] for letter in word]

print(code_words)
