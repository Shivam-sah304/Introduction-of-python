#Write a Python program to create a dictionary with the names of 5 students as keys and their marks as values.
dict={'shivam':345,'rajan':456,'shishir':345,'samir':234,'karun':234}

name=input("Enter the name of students whose mark you want to access :")
print(dict[name])
""" Given a dictionary fruits = {"apple": 3, "banana": 5, "orange": 2},
write a program to add "mango": 4 to the dictionary and remove "banana"."""
fruits = {"apple": 3, "banana": 5, "orange": 2}
fruits['mango']=4
del(fruits['banana'])
print(fruits)