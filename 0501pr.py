myDict={
    'pankha': 'fan',
    'vastu': 'iteam',
    'ghanti': 'bell',
    'kutta':'dog',
    'billi':'cat',
    'ghora':'horse',
    'kursi':'chair',
}
print("Option are avialable" , myDict.keys() )
a=input("enter your hindi word \n")
print("the meaning of your word is: ",myDict.get(a))