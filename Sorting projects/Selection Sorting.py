a = [10, 5, 3, 24, 2, 23, 17, 12, 1, 5, 9]
n = len(a)
for i in range(n):
    selection = i
    flag = False
    for j in range(i + 1, n):
        if a[j] == a[i]:
            continue
        if a[j] < a[selection]:
            flag = True     #if a smaller element than our i element through the i + 1 to end of list, flag is assigned to True and assignment between elements is needed.
            selection = j
    a[i], a[selection] = a[selection], a[i]
    if not flag:        #if no element exists smaller than our element thet i counter is currently its index, no assignment needed and continue through the first loop.
        continue
print(a)
