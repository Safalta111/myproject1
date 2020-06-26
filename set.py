#set(unordered,duplicate elements are not allowed,rep by{})

# create set
s={10,20,30,50}
print(s)
#print(s[1])#TypeError: 'set' object is not subscriptable (means unorder)
s.add(70) #append is used in list &add is used in set
print(s)

#types of set
d={}
a = set()
print(type(a))
print(type(s))
print(type(d))

