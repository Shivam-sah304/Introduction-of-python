
students_missing = {
    "Name": [
        "Aarav Mehta", "Priya Sharma", "Rohan Gupta",
        "Isha Verma", "Aditya Singh", "Neha Kapoor",
        "Kabir Das", "Simran Kaur", "Vikram Joshi", "Ananya Rai"
    ],
    "Age": [18, 19, 21, 20, 22, 18, 23, 19, 20, 21],
    "Maths": [88, None, 76, 85, 95, None, 80, 90, None, 85],
    "Science": [91, 85, None, 80, 97, 60, None, 88, 74, None],
    "English": [84, 90, 65, None, 88, 72, 79, None, 69, 87],
    "City": [
        "Delhi", "Mumbai", "Delhi", "Bangalore", "Delhi",
        "Chennai", "Mumbai", "Delhi", "Chennai", "Bangalore"
    ]
}
import pandas as pd
student_data=pd.DataFrame(students_missing)
#check any missing values exit 
print(student_data.isna().any())
#Fill missing marks with the column mean.
data_filled=student_data.fillna(student_data.mean(numeric_only=True))
print(data_filled[["Name","Maths","Science","English"]])
#Drop rows where all subject marks are NaN
print(student_data.dropna(subset=["Maths","Science","English"],how="all"))
#print sum of all nan
print(student_data.isna().sum())


