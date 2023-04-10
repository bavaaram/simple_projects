lis_t = [43, 6, 2, 72, 25, 23, 1, 4, 17, 15, 50, 13, 12, 20, 5]
print(lis_t)
roundd = 1
print("\n--------------------------------------------------------------\n")
for j in range(0, len(lis_t)):
    count = 1
    for i in range(len(lis_t) - 1, j, -1):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if lis_t[i] < lis_t[i - 1]:
            lis_t[i], lis_t[i - 1] = lis_t[i - 1], lis_t[i]
        print("Round %s" % str(roundd))
        print("Iteration #%s" % str(count))
        print(lis_t)
        print("+_+_+_+_+_")
        print("i is %s" % str(i))
        print("j js %s" % str(j))
        count += 1
        i -= 1
    print("\n*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*&*\n")
    roundd += 1
