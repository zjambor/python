def mysplit(strng : str):
    mypos = 0
    fnd = strng.find(' ')
    splitstring = []
    while fnd != -1:
        mystr = strng[mypos:fnd]
        if mystr != '':
            splitstring.append(mystr)
        mypos = fnd + 1
        fnd = strng.find(' ', mypos)
    mystr = strng[mypos:len(strng)]
    if mystr != '':
            splitstring.append(mystr)

    return splitstring


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

# Expected:
# ['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']
# ['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question']
# []
# ['abc']
# []

'''
def mysplit(strng):
    # return [] if string is empty or contains whitespaces only
    if strng == '' or strng.isspace():
        return [ ]
    # prepare a list to return
    lst = []
    # prepare a word to build subsequent words
    word = ''
    # check if we are currently inside a word (i.e., if the string starts with a word)
    inword = not strng[0].isspace()
    # iterate through all the characters in the string
    for x in strng:
        # if we are currently inside a string...
        if inword:
            # ... and the current character is not a space...
            if not x.isspace():
                # ... update the current word
                word = word + x
            else:
                # ... otherwise, we've reached the end of the word so we need to append it to the list...
                lst.append(word)
                # ... and signal the fact that we are outside the word now
                inword = False
        else:
            # if we are outside the word and we've reached a non-white character...
            if not x.isspace():
                # ... it means that a new word has begun so we need to remember it and...
                inword = True
                # ... store the first letter of the new word
                word = x
            else:
                pass
    # if we've left the string and there is a non-empty string in the word, we need to update the list
    if inword:
        lst.append(word)
    # return the list to the invoker
    return lst
'''
