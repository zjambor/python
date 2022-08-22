sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
words_lengths = [len(word) for word in words if word != "the"] 

print(words)
print(words_lengths)

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [n for n in numbers if n > 0]

print(newlist)
