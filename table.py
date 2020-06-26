# n = int(input("Enter the no till u want to print the table"))
# m = int(input("Enter the no which digit table you want to print"))
# # n = 20
# # m = 14
# for i in range(1, m + 1):
#     print(n * i)
#     print("  ")
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
'''
m = 6
for row in range(1,m):
    for col in range(1, row + 1):
        print(str(col) + " ", end='')
    print()
'''
6
6 5
6 5 4
6 5 4 3
6 5 4 3 2
6 5 4 3 2 1
'''
m = 5
for i in range(m + 1):
    for j in range(i + 1):
        print(m + 1 - j, end=' ')
    print()
