import random

list = []
index = 0
def Numbersort(list):
    list.sort()
    return list

print("nevada3921")

while index < 1000:
    list.append(random.randint(1,1000))
    index += 1

list = Numbersort(list)

for item in list:
    print(item)
