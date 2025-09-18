employees_data = {
    "FullName": [
        "Rahul Kumar", "Ananya Sharma", "Vikash Reddy",
        "Pooja Mehra", "Arjun Nair", "Sneha Kapoor",
        "Manish Das", "Divya Singh", "Ravi Patel", "Kavya Iyer"
    ],
    "Department": [
        "HR", "Finance", "IT", "IT", "Marketing",
        "Finance", "HR", "IT", "Marketing", "Finance"
    ],
    "Email": [
        "rahul.kumar@company.com",
        "ananya.sharma@company.com",
        "vikash.reddy@company.com",
        "pooja.mehra@company.com",
        "arjun.nair@company.com",
        "sneha.kapoor@company.com",
        "manish.das@company.com",
        "divya.singh@company.com",
        "ravi.patel@company.com",
        "kavya.iyer@company.com"
    ],
    "City": [
        "Delhi", "Mumbai", "Bangalore", "Chennai", "Pune",
        "Kolkata", "Delhi", "Bangalore", "Pune", "Chennai"
    ]
}
import pandas as pd
data=pd.DataFrame(employees_data)
#On the “name” column:
#Convert to uppercase.
data["FullName"]=data["FullName"].str.upper()
print(data[["FullName","City"]])
#Check which names start with “A”.
starts_with_A=data["FullName"].str.startswith("A")
print(data[starts_with_A])
#Split full name into first and last names.
data[["FirstName","LastName"]]=data["FullName"].str.split(" ",expand=True)
print(data[["FirstName","LastName","City"]])