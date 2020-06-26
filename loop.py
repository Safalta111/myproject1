# print 10 natural no using while loop
print("First 10 natural no are as below:")
i = 0
while i <= 10:
    print(i)
    i += 1
# "pattern"
s = 6
for i in range(1, s):
    for j in range(1, i + 1):
        print(j, end=' ')
    print(" ")

# Sum of no
sum = 0
n = int(input("Enter the no"))
for i in range(n + 1):
    sum = sum + i
    # i+=1
print(sum)
# table
# x = 1
# n = int(input("Enter the no till u want to print the table"))
# for a in range(1, n + 1):
#     m = int(input("Enter the no which digit table you want to print"))
#     for a in range(1, n + 1):
#         x = a * m
#         print(x)
    # n=int(input("Enter which table you want to print:"))
    # for i in range(1, 11,1):
    #       x=i*n
    #       print(x)
    # lst=[12,15,32,42,55,75,122,132,150,180,200]
    # print(lst)
    # for i in lst:
    #  if(i>150):
    #   break
    #  if(i%5 == 0):
    #      print (i)
    # i=int(input("enter the digit which u want to count:"))
    # count=0
    # while i!=0:
    #    i//=10
    #    count+=1
    # print(count)
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print(" ")
# # lst=[10,20,30,40,50]
# # print("Given list:",lst)
# # lst.reverse()
# for i in lst:
#  print(i)

# for i in range(-10,0,1):
#     print(i)
