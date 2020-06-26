n = 6
for j in range(1, n):
    for i in range(1, j + 1):
        print(str(i) + " ", end='')
        k = i
        for m in range(k,-1):
            print(str(k))
    print()



