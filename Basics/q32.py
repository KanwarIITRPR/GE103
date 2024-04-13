import random
l = []

r = random.randint(1, 1001)
for i in range(r):
    l.append(random.randint(1, 1000))

print(f"The list is {l}.\nThe number of elements in the list are {r}.")