sentence = input("What sentence should be output? ")
character = input("Which letter should be removed? ")
result = ""
for c in sentence:
    if c != character:
        result += c
    if len(result) > 20:
        break
print(result)