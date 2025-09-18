#Filter all students who:
students_data = {
    "Name": [
        "Aarav Mehta", "Priya Sharma", "Rohan Gupta",
        "Isha Verma", "Aditya Singh", "Neha Kapoor",
        "Kabir Das", "Simran Kaur", "Vikram Joshi", "Ananya Rai"
    ],
    "Age": [18, 19, 21, 20, 22, 18, 23, 19, 20, 21],
    "Maths": [88, 92, 76, 85, 95, 67, 80, 90, 72, 85],
    "Science": [91, 85, 70, 80, 97, 60, 78, 88, 74, 90],
    "English": [84, 90, 65, 82, 88, 72, 79, 85, 69, 87],
    "City": [
        "Delhi", "Mumbai", "Delhi", "Bangalore", "Delhi",
        "Chennai", "Mumbai", "Delhi", "Chennai", "Bangalore"
    ]
}
#belong to “Delhi” OR math scored > 90 in any subject.
import pandas as pd
import numpy as np
student_data1=pd.DataFrame(students_data)
print(student_data1[np.logical_or(student_data1["City"]=="Delhi",student_data1["Maths"]>90)])
#are from “Mumbai” AND have age between 18 and 22.
age=[19,20,21]
print(student_data1[np.logical_and(student_data1["City"]=="Mumbai",student_data1["Age"].isin(age))])
# add a column called total_marks
student_data1["total_marks"]=student_data1["Maths"]+student_data1["Science"]+student_data1["English"]
print(student_data1)
#Sort the DataFrame by:
#Total marks (descending).
students_data_sort=student_data1.sort_values("total_marks",ascending=False)
print(students_data_sort[["Name","total_marks","City"]])
#City (ascending) and Age (descending).
students_data_sort_city=student_data1.sort_values(["City","Age"],ascending=[True,False])
print(students_data_sort_city[["Name","City","Age"]])
#Also find the rank of students based on their total marks.
students_data_sort["Rank"]=students_data_sort["total_marks"].rank(method="dense",ascending=False)
print(students_data_sort[["Name","total_marks","Rank"]].sort_values("Rank"))