data = {
    "Name": ["Aarav", "Priya", "Kiran", "Rohan", "Sneha", "Maya"],
    "Department": ["HR", "IT", "IT", "Finance", "Finance", "HR"],
    "Joining_Year": [2020, 2019, 2021, 2018, 2022, 2020],
    "Salary": [55000, 72000, 65000, 80000, 62000, 60000],
    "Experience": [3, 5, 2, 6, 1, 3]
}
import pandas as pd
import numpy as np
data1=pd.DataFrame(data)
data1.index=["AR","PR","KR","RO","SN","MA"]
#Filter employees who joined after 2019 AND have a salary greater than 60000.
print(data1[np.logical_and(data1["Joining_Year"]>2019,data1["Salary"]>60000)])
#Create a new column called Salary_per_YearExp = Salary / Experience.
data2=data1["Salary"]/data1["Experience"]
data1["Salary_per_YearExp "]=data2
print(data2)
print(data1.loc[:,["Salary_per_YearExp "]])
#Sort the DataFrame by this new column in descending order.
data1_sorted=data1.sort_values(by="Salary_per_YearExp ",ascending=False)
print(data1_sorted.iloc[:,[0,1,5]])
