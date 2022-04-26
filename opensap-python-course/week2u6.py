list_l = [1, 2, 3, 4, 5, 6]
string_s = "This is a string, right?"
range_100 = range(0, 100, 2)

print("Number 4 in list?", 4 in list_l)
print("Number 10 in list?", 10 in list_l)

print("String contains s!", "s" in string_s)
print("The range contains the number 27:", 27 in range_100)

print("Those str" + "ings were concatenated")

#print(5 * range_100)

print(min(list_l))
stringlist = ["b", "ab","bab","abab"]
print(sorted(stringlist))
print(min(stringlist))
print(min("abab"))

print("List of squares:", [x ** 2 for x in list(range(1,21))])

list1 = [0]
print(3 * list1)
print(type( list1[-0]))
print(list(range(10,1)))