# a=input("Enter Your Name: ")
# print("Good Morning, \n"+ a)
letter= '''Dear <|NAME|>,
You are verry lucky today
you are Selected win price program
Have a great day ahead!
Thanks and Regards,
GSK
Date- <|DATE|>'''
name= input("Enter Your Name: ")
date= input("Enter Date: ")
letter= letter.replace("<|NAME|>", name)
letter= letter.replace("<|DATE|>", date)
print(letter)