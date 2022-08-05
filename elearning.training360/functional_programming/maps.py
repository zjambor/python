from functools import reduce
from closure import pow_of_2

li = [1,3,5,2,5,7,8]
li2 = list(map(pow_of_2, li))
print(li2)

# higher order func

li3 = list(
        map(pow_of_2, 
            filter(lambda x: x % 2 == 0, li)))
print(li3)

sum2 = reduce(lambda x,y: x+y,
            map(pow_of_2, 
                filter(lambda x: x % 2 == 0, li)))
print(sum2)
