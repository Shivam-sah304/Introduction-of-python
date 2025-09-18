#From the above DataFrame:(pandas4)
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
import pandas as pd
students_data1=pd.DataFrame(students_data)
#Select only the “marks” columns.
print(students_data1[["Maths","Science","English"]])
#Retrieve rows where marks in Maths > 80.
print(students_data1[students_data1["Maths"]>80])
#Use .iloc to get the 2nd row and 3rd column.
print(students_data1.iloc[1,2])
#Set “name” as the index and reset it.
students_data1_ind=students_data1.set_index("Name")
print(students_data1_ind)
#reseet
print(students_data1_ind.reset_index())