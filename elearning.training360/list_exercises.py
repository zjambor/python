lista = [-25, 12, -54, 8, 77, 98, -29, 35, 3, 71]

# Maximum value
maxelem = lista[0]
print("Maximum value:", maxelem)
for n in range(1, len(lista)):
    if lista[n] > maxelem:
        maxelem = lista[n]
    print("Maximum value:", maxelem)

print("Maximum value:", maxelem)

print(lista)

# index = 0
# print("A lista: ", end="")
# for n in lista:
#     print(f"[{index}]={n};", end=" ")
#     index += 1

for i, n in enumerate(lista):
    print(f"[{i}]={n};", end=' ')

print()

# Minimum value
minelem = lista[0]
minhely = 0

for n in range(1, len(lista)):
    if lista[n] < minelem:
        minelem = lista[n]
        minhely = n

print("Minimum value:", minelem)
print("Index of minimum value:", minhely)

# index = 0
# print("A lista:", end="")
# for n in lista:
#     print(f" {n}", end="")
#     if index == minhely:
#         print("[MIN]", end="")
#     index += 1

print("A lista:", end=" ")
for n in lista:
    print(f'{n}{ "[MIN]" if n == minelem else ""}', end=" ")

print()
# Reverse
reverse_list = []

for n in lista[::-1]:
    reverse_list.append(n)
print("Reversed list 1:", reverse_list)

new_lista = lista.copy()
reverse_list = []
for _ in range(len(new_lista)):
    reverse_list.append(new_lista.pop())

print("Reversed list 2:", reverse_list)
print("Original list:", lista)

reverse_list = lista.copy()

# solution 1
index = 0
lastindex = len(reverse_list) - 1
while index <= lastindex:
    n = reverse_list[index]
    reverse_list[index] = reverse_list[lastindex]
    reverse_list[lastindex] = n
    index += 1
    lastindex -= 1

print("Reversed list 3:", reverse_list)

# solution 2
reverse_list2 = lista.copy()
for i in range(len(reverse_list2) // 2 + 1):
    n = reverse_list2[i]
    reverse_list2[i] = reverse_list2[len(reverse_list2) - 1 - i]
    reverse_list2[len(reverse_list2) - 1 - i] = n

print("Reversed list 4:", reverse_list2)
