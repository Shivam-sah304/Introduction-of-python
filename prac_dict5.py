#You have this nested dictionary:
students = {
    "S1": {"name": "Anita", "age": 19},
    "S2": {"name": "Vikram", "age": 21}
}
#Print the name of student S2.
print(students["S2"]["name"])
#Add a new student S3 with your own data.
data={"name":"samir","age":20}
students["S3"]=data
print(students)