data = {
    "Name": ["Aarav", "Priya", "Kiran", "Rohan", "Sneha", "Maya"],
    "Department": ["HR", "IT", "IT", "Finance", "Finance", "HR"],
    "Joining_Year": [2020, 2019, 2021, 2018, 2022, 2020],
    "Salary": [55000, 72000, 65000, 80000, 62000, 60000],
    "Experience": [3, 5, 2, 6, 1, 3]
}
import pandas as pd
data1=pd.DataFrame(data)
data_ind=data1.set_index("Department")
print(data_ind)

print(data_ind.loc[['HR','IT'],['Name','Salary']])
print(data_ind["Salary"].agg("max"))
print(data_ind.iloc[[1,3],:])
print(data_ind["Experience"].cumprod())
print(data_ind.drop_duplicates(subset=["Experience","Joining_Year"]))
print(data_ind["Experience"].value_counts())
print(data_ind["Joining_Year"].min())
for index,row in data_ind.iterrows():
    print(index)
    print(row[["Joining_Year","Experience"]])
data2=data_ind[["Joining_Year","Salary"]]
print(data2["Salary"].mean())
data_ind["Name_len"]=data_ind["Name"].apply(len)
print(data_ind.sort_values("Name_len"))
print(data_ind.head())
print(data2.columns)
print(data2.index)