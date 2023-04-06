import random
import math

print("Hi, This is a program that make Random integers and sort them via Insertion sorting method :)")
n = 20
a = list()
print(type(a))
counter = 0
for y in range(n):
    a.append(random.randint(-100, 100))
print("Now the list of integers is ready, Here wo gooooo :0")
print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
print(a)
print("There is a star row, but i changed it for practical porpuses :)")
for j in range(1, len(a)):
    item = a[j]
    while (j > 0) and (a[j-1] > item):
        a[j] = a[j - 1]
        j -= 1
        counter += 1
    a[j] = item

    print(a)
print("This section is added for learning vim, be funny :)")
print("The required operation count is %s" % counter)

