#You start with this data:



students = {
    "S101": {
        "name": "Anita",
        "age": 20,
        "subjects": {"Math": [88, 92], "Science": [85, 90]}
    },
    "S102": {
        "name": "Ravi",
        "age": 21,
        "subjects": {"Math": [75, 80], "Science": [78, 82]}
    }
}
#Check if "S103" exists.
data={"name":"shishir","age":20,"subjects":{"Math":[56,78],"Science":[98.76]}}
if "S103" in students:
    print("The student s103 is exit")
else:
    print("Student s103 is not exit")
    students["S103"]=data

#Add 95 in Math for student S101.
#Add 88 in Science for S103.
students["S101"]["subjects"]["Math"].append(95)
students["S103"]["subjects"]["Science"].append(88)
#Update the age of S102 to 22.
students["S102"]["age"]=22
#Remove the age field from S101.
del(students["S101"]["age"])
#print every students name
for student_id in students:
    print(students[student_id]["name"])
#for each student 
#For each subject, calculate and print the average marks.
