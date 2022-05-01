emojis = {
"happy": "😃",
"heart": "😍",
"rotfl": "🤣",
"smile": "😊",
"crying": "😭",
"kiss": "😘",
"clap": "👏",
"grin": "😁",
"fire": "🔥",
"broken": "💔",
"think": "🤔",
"excited": "🤩",
"boring": "🙄",
"winking": "😉",
"ok": "👌",
"hug": "🤗",
"cool": "😎",
"angry": "😠",
"python": "🐍"
}  

"""
Use this dictionary to build a program that:
    Reads a sentence from the user.
    Replaces all the words in the sentence with the corresponding Emoji.
Please enter a sentence: I'm so excited to learn python
"""

sentence = input("Please enter a sentence: ")
words = sentence.split()
#print(words)
new_words = []
keys_ = list(emojis.keys())

for k in words:
    if k in keys_:
        new_words.append(emojis[k])
    else:
        new_words.append(k)

new_sentence = ' '.join(new_words)

print(new_sentence)