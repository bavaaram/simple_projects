from random import randint
n = input("How many numbers in list? ")
lis_t = list()
for k in range(int(n)):
    lis_t.append(randint(-100, 100))
print("The Generated list is: %s" % str(lis_t))
roundd = 1
print("\n--------------------------------------------------------------\n")
for j in range(0, len(lis_t)):
    bubble_found = False
    count = 1
    for i in range(len(lis_t) - 1, j, -1):
        if lis_t[i] < lis_t[i - 1]:
            lis_t[i], lis_t[i - 1] = lis_t[i - 1], lis_t[i]
            bubble_found = True
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Round %s" % str(roundd))
            print("Iteration #%s" % str(count))
            print(lis_t)
            print("+_+_+_+_+_")
            print("i is %s" % str(i))
            print("j js %s" % str(j))
            count += 1
    if not bubble_found:
        break
        i -= 1
    roundd += 1
    if j > i:
        break
    print("\n*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*\n")
print("The final sorted list is %s" % str(lis_t))
