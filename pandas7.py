#Group the data by “city”:
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
print(students_data1[["Name","City","Maths"]])
#Get average, max, and min marks of each subject per city.
students_data1_group=students_data1.groupby("City")[["Maths","Science","English"]].agg(["mean","max","min"])
print(students_data1_group)
#Count how many students are in each city.
print(students_data1.value_counts("City"))