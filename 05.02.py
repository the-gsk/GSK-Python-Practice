a={}
print(type(a))

#creatin a empty set
b=set()
print(type(b))
b.add(4)
b.add(8)
b.add(7)
b.add(6)
b.add(4)
b.add(5)
# b.add("gaurav")
# b.add("gaurav")

# b.add({45:50}) cannot add list or distionary
# b.add([4,5,8]) can't add list

b.add((4,2,6,4))

print(b)
print(len(b))

b.remove(4)
# b.remove(9)  '''if data not available retun error'''
print(b.pop()) #remove any things from set

print(b)

print(b.clear())
print(b)
b.union()
print(b)