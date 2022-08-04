# x = dict.get("key")
# add element ot dict with key: dict["key"] = value

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

# count items 1
res_dict = {}
for n in sample_list:
    res_dict[n] = sample_list.count(n)

print(res_dict)

# count items 2
countDict = {}
for item in sample_list:
    if item in countDict:
        countDict[item] += 1
    else:
        countDict[item] = 1
print(countDict)

# removing
rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
dictValues = sampleDict.values()
templist = []

for n in rollNumber:
    if n in dictValues:
        templist.append(n)

rollNumber = templist

print(rollNumber)

# other solution

rollNumber[:] = [item for item in rollNumber if item in sampleDict.values()]
print(rollNumber)
