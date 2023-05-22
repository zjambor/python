dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")

for key in dictionary.keys():
    print(key, "->", dictionary[key])

for english, french in dictionary.items():
    print(english, "->", french)

dictionary['swan'] = 'cygne'
print(dictionary)

dictionary.update({"duck": "canard"})
print(dictionary)

print(dictionary.popitem())

print(dictionary)

pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

copy_dictionary = pol_eng_dictionary.copy()

print(copy_dictionary)

copy_dictionary.clear()

print(copy_dictionary)

d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)

dictionary = {}
my_list = ['a', 'b', 'c', 'd']

for i in range(len(my_list) - 1):
    dictionary[my_list[i]] = (my_list[i], )

print(dictionary)

for i in sorted(dictionary.keys()):
    k = dictionary[i]
    print(k[0])

dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dictionary['one']
 
for k in range(len(dictionary)):
    v = dictionary[v]
 
print(v)
