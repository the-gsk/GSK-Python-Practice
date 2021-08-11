# Tuples in Python
#tuple is immutable (un changeble) data
a=() #empty tuple
print(a)
b=(1) #it's not a tuple 
print(b)
c=(45,) # tuple with one element need comma
print(c)
d=(2,5,6,8,1,3,4,9,5,4,6,7,3,1,2,3,6,9,7,4,1,) #tuple with more than one element
print(d)
print(d.count(4)) #count how many time have 4
print(d.index(9)) #return the index first occurance of 9 in d