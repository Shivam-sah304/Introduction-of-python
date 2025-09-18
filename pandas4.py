#Create a pandas DataFrame from a Python dictionary containing student names, age, marks in 3 subjects, and city.
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
#Print first 3 rows, last 2 rows, shape, columns, dtypes, and info.
print(students_data1.head())
#printing shape of the dataframe
#shape()=gives the number of rows vs column
print(students_data1.shape)
#printing the column of the dataframe
#column=it gives name of all the columns
print(students_data1.columns)
#print dtypes of dataframe
print(type(students_data1))
#print the info of data frame
print(students_data1.info())

