import re

text = 'Kiss Pista szerencseszáma 122'
pattern = r'\d\d\d'

regex = re.compile(pattern)
number = regex.findall(text)        # .match(), .search(), .findall(), .finditer()
# replace: result = regex.sub(replaceText, text)
# split: result = regex.split(text)

print(number)
