from random import seed, randint

seed()          # a seed() inicializálja a random number generatort
data = [randint(-10,10) for x in range(5)]          # random egészeket generál -10 és +10 között
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)
