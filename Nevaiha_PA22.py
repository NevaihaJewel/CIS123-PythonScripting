import random

list = []

for i in range(100):
    list.append(random.randint(1,1000))

print(list)

list.sort()
print(list)
