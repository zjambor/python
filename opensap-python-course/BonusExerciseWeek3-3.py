alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#abc = "abcdefghijklmnopqrstuvwxyz"

shift = ""
while (not shift.isdecimal()) or (int(shift) > 25 or int(shift) < 0):
    print("You need to enter a number between 0 and 25!")
    shift = input("Please enter the number of places to shift: ")

shift = int(shift)

Plaintext = input("Please enter a sentence: ").lower()  # python is fun!
Encrypted_text = ""

for letter in Plaintext:
    if letter in alphabet:
        position = (alphabet.index(letter) + shift) % len(alphabet)
        #position = (abc.find(letter) + shift) % (len(abc))
        Encrypted_text += alphabet[position]
    else:
        Encrypted_text += letter

print("The encrypted sentence is:", Encrypted_text)