def group_by_fun(data=[]):
    if not data:
        return {}
    gd = {}
    for i in data:
        if i in gd:
            gd[i] = gd[i] + 1
        else:
            gd[i] = 1
    return gd


# d = [None,1,2]
a = "safalta thakur hor r u ,plese safalta let me know how r u "
d = a.split(" ")

gd = group_by_fun(d)
print(gd)
