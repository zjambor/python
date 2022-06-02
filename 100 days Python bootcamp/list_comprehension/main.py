with open("file1.txt", "r") as file1:
    list1 = file1.readlines()

with open("file2.txt", "r") as file2:
    list2 = file2.readlines()

result = [int(x) for x in list1 if x in list2]

sum_of_elements = [int(list1[i]) + int(list2[i]) for i in range(len(list1))]

print(result)
print(sum_of_elements)
