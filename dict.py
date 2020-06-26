d = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(d["model"])
# print(d["pkt"])
d["model"] = 6
print(d["model"])
# del d["model"]
print(d["model"])

for k in d:
    print(k, d[k])


