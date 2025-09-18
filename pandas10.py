employees_dates = {
    "EmployeeID": ["E101", "E102", "E103", "E104", "E105", "E106"],
    "Name": ["Rahul", "Priya", "Vikash", "Pooja", "Arjun", "Sneha"],
    "Department": ["HR", "Finance", "IT", "IT", "Marketing", "Finance"],
    "JoinDate": [
        "2022-03-15",
        "2023-01-10",
        "2021-07-25",
        "2023-06-01",
        "2022-11-30",
        "2023-02-20"
    ],
    "DOB": [
        "1995-05-12",
        "1998-08-24",
        "1994-12-05",
        "1996-03-18",
        "1993-09-10",
        "1997-11-22"
    ]
}
import pandas as pd
data=pd.DataFrame(employees_dates)
#Extract year, month, and weekday.
data["JoinDate"]=pd.to_datetime(data["JoinDate"])
data["Join_Year"]=data["JoinDate"].dt.year
print(data.head())
#Filter students who joined after 2023-01-01.
print(data[data["JoinDate"]>"2023-01-01"])