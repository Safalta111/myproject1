#Tuple(same as list except it is immutable(read only version of list)represents by paranthesis ())

#accessing elements in tuple
a =(10, 20, 30, 40, "safalta","book")
print(type(a))
print("value of Tuple:",a)
print("value of given index:", a[0])
print("value of given index:", a[-1])
print("value between given position:", a[2:6])#slicing

print("no of value:", a.count(40))#value appear no of times

#add anything in typle (need to convert into list first then append)
b=("a", "b", "d")
x = list(b)
x.append("c")
x[3]="m"
print (x)
b = tuple(x)
print("type check:", type(b))

# del tuple
print(b)
del b
print("print", b)# raise error
'''
a[0] =4  #bcz tuple is immutable
print(a)#'tuple' object does not support item assignment
'''
# types of tuple
s = ()
print(type(s)) #<class 'tuple'> empty tuple
s = (1)
print(type(s))#<class 'int'> only this type os problem occure in tuple
s = (1,)
print(type(s))