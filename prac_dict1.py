#Create a dictionary called student with the following data:
# print te value of age 
# add one value and display the whole dictionary
my_dict={
    "name":"Rahul",
    "Age": 23,
    "course":"python"
}
#print the name
print(" The name of the student is "+my_dict["name"])
#print the age
print("The age of student is "+str(my_dict["Age"]))
#print the course
print("The course of the student is "+my_dict["course"])
#add another key
my_dict["class"]=12
print("The class of the student is "+str(my_dict["class"]))
#apply for loop to print the key and value of my_dict
for key,value in my_dict.items():
    print("The key is  " +key + " and the value is "+str( value))\
#print out the key of the my_dict
print(my_dict.keys())
#use type function
print(type(my_dict))