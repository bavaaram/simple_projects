a = [10, 5, 3, 24, 2, 23, 17, 12, 1, 5, 9]

for i in range(0, len(a)):
    A = a[i]
    B = a[i]
    flag = False
    for j in range(i + 1, len(a)):
        if a[j] == A:
            continue
        if a[j] < B:
            flag = True     #if a smaller element than our i element through the i + 1 to end of list, flag is assigned to True and assignment between elements is needed.
            B = a[j]
            index = j
    if not flag:        #if no element exists smaller than our element thet i counter is currently its index, no assignment needed and continue through the first loop.
        continue
    a[i] = B
    a[index] = A

print(a)
