# remove last element
my_tuple = (-25, 12, -54, 8, 77, 98, -29, 35, 3, 71)

my_tuple = my_tuple[:-1]

print(my_tuple)

# remove third element
my_tuple = my_tuple[:2] + my_tuple[3:]
print(my_tuple)

# remove duplication
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

result_list = []
temp_list = [result_list.append(x) for x in sample_list if x not in result_list]

new_tuple = tuple(result_list)
print(new_tuple)

# solution with set
print("Original list:", sample_list)
sample_list = list(set(sample_list))
print("Unique list:", sample_list)

# minelem, maxelem
print(min(new_tuple))
print(max(new_tuple))
