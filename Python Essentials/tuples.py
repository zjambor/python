var = 123
 
t1 = (1, )
t2 = (2, )
t3 = (3, var)
 
t1, t2, t3 = t2, t3, t1
 
print(t1, t2, t3)

my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)

my_list = [2, 4, 6]
print(my_list) # outputs: [2, 4, 6]
print(type(my_list)) # outputs: <class 'list'>
tup = tuple(my_list)
print(tup) # outputs: (2, 4, 6)
print(type(tup)) # outputs: <class 'tuple'>

tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)

print(duplicates)    # outputs: 4
