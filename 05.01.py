a= {
    "key" : "value",
    "gaurav": "kumar",
    "shaurabh": "kumar",
    "list": [2,5,10,12],
    "b": {"son": "ravi"}
}
print(a["list"])
print(a["b"]["son"])
print(a["b"])
a["list"]=[45,10]
print(a["list"])
print(list(a.keys()))
print(list(a.values()))
print(list(a.items()))
a.update({"swami":"kailash"})
print(list(a.items()))
print(a["swami"])
print(a.get("key"))
print(a.get("name"))
print(type(a))