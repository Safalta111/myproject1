'''def calculate(a, b):
    print("sum of a+b", a + b)
    print("difference of a-b", a - b)
    print("multiply of  of a*b", a * b)
    print("Divison of a%b", a % b)
    print("Divison of a/b", a / b)


x , y = int(input("enter the value of a:")),int(input("enter the value of b:"))
#y = int(input("enter the value of b:"))
calculate(x,y)

a=10
def f():
    a=20
    print(a)
def f1():
 print(a)

f()
f1()
def f3():
    print("hi")
f3()



# def details(s):
#     print ("safalta details",s)
#
# details("email")
# details("name")
# details("password")
# max of three no
def max(a, b, c, ):
    if a > b and a > c:
        print("largest of a:", a)
    elif c > a and c > b:
        print("largest ofc:", c)
    else:
        print(c)

#
# max(23, 34, 56)


# Sum of all no into list

def sum(lst):
    sum_value = 0
    for i in lst:
        sum_value = sum_value + int(i)
    return sum_value


#lst = [3, 4, 5, 6]
lst= input("enter the list ")
lt = lst.split()
print(sum(lt))

#function to multiply all the numbers in a list
def mul_list(lst):
    mul = 1
    for i in lst:
        mul = mul * int(i)
    return mul

x = input("enter the value of list which you need to multiply:")
lt = x.split()
print(mul_list(lt))
'''


# factorial of a no
def factorial(a):
    num = 1
    for i in range(2, a + 1):
        num = num * i
    return num


factorial(5)
print("factorial", factorial(5))
