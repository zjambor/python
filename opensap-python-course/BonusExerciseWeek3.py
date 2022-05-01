"""
Your task for the bonus exercise is the implementation of a Caesar cipher with a variable shift. The program should ask the user for a number of characters for the shift first. 
Next the program should ask the user for a plain text sentence and print the encrypted text. Here is an example execution of the program:

Please enter the number of places to shift: 5
Please enter a sentence: python is fun!
The encrypted sentence is: udymts nx kzs!

The simple solution using a dictionary will not work for this exercise. Instead you need to build the substitution dynamically. 
This can be done using the find method and some calculations: abc = “abcdefghijklmnopqrstuvw” char_index = abc.find(“f”) encrypted_char = abc[char_index + 5]

Note that in the example above there will be an error if char_index +5 is larger then 25. You need to use the modulo (%) operator to take care of this situation.

In order to check if the user entered a number, the method isdecimal() can be used.

To avoid handling upper and lower case letters it is best to first convert the user input to lower case. 
After that you only need to take into account lower case letters. A string can be converted into lower case using the .lower() method.
"""

#alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
abc = "abcdefghijklmnopqrstuvwxyz"

shift = ""
while not shift.isdecimal():
    shift = input("Please enter the number of places to shift: ")

shift = int(shift)

if shift > 25 or shift < 0:
    print("You need to enter a number between 0 and 25!")
else:

    Plaintext = input("Please enter a sentence: ").lower()
    Encrypted_text = ""

    for letter in Plaintext:
        if letter in abc:
            #position = (alphabet.index(letter) + shift) % 25    #len(alphabet)
            position = (abc.find(letter) + shift) % (len(abc))
            Encrypted_text += abc[position]
        else:
            Encrypted_text += letter

    print("The encrypted sentence is:", Encrypted_text)
