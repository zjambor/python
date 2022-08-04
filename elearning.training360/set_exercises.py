# set functions: add(element), remove(element), add more elements: update([element list])

# s.issubset(t) - test whether s is subset of t
# s.issuperset(t) - test whether s is superset of t
# s.union(t) - new set with union of s and t
# s.intersection(t) - new set with intersection of s and t

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

union_list = []
# for i in range(len(first_list)):
#     union_list.append((first_list[i], second_list[i]))

for i, n in enumerate(first_list):
    union_list.append((n, second_list[i]))
print(union_list)

union_set = set(union_list)
print(union_set)

# using zip function
result_set = set(zip(first_list, second_list))
print(result_set)
