nums = []
with open("randomnumbers.txt", "r") as file:
    for line in file:
        nums.append(int(line.strip()))
nums = sorted(nums)

for num in nums[-1:-4:-1]:
    print(num)