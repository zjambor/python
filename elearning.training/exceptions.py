rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
dictValues = sampleDict.values()

try:
    for i in range(len(rollNumber)):
        if rollNumber[i] in dictValues:
            rollNumber.remove(rollNumber[i])
except(Exception) as e:
    print("Error message:", e)

print(rollNumber)