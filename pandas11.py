retail_data = {
    "CustomerID": ["C101", "C102", "C103", "C104", "C105", "C106", "C107", "C108", "C109", "C110"],
    "Name": ["Aarav Mehta", "Priya Sharma", "Rohan Gupta", "Isha Verma", "Aditya Singh",
             "Neha Kapoor", "Kabir Das", "Simran Kaur", "Vikram Joshi", "Ananya Rai"],
    "City": ["Delhi", "Mumbai", "Delhi", "Bangalore", "Delhi",
             "Chennai", "Mumbai", "Delhi", "Chennai", "Bangalore"],
    "Category": ["Electronics", "Clothing", "Electronics", "Books", "Clothing",
                 "Electronics", "Books", "Clothing", "Electronics", "Books"],
    "Quantity": [2, 5, 1, 3, 2, None, 4, 3, 2, 1],
    "Amount": [1200, 500, 1200, 300, None, 1500, 200, 450, 800, 150],
    "PurchaseDate": ["2023-03-15", "2023-01-10", "2023-07-25", "2023-06-01",
                     "2022-11-30", "2023-02-20", "2023-05-12", "2023-03-18",
                     "2022-09-10", "2023-04-05"]
}
import pandas as pd
data=pd.DataFrame(retail_data)
#Explore the data: check first/last rows, data types, missing values.

print(type(data))
print(data.isna().any())
#Select columns and rows, filter customers by city, total spending, or purchase category.
print(data[["City","PurchaseDate"]])
#Handle missing values in Amount or Quantity.
data_filled=data.fillna(data.mean(numeric_only=True))
#Create new columns like TotalAmount = Quantity * Amount
data_filled["TotalAmount"]=data_filled["Quantity"]*data_filled["Amount"]

#categorize customers (High/Medium/Low spender)
bins=[500,1000,1500,data_filled["TotalAmount"].max()+1]
level=["Low","Medium","High"]
data_filled["Spendercategory"]=pd.cut(data_filled["TotalAmount"],bins=bins,labels=level)
print(data_filled.head())
#Rank customers by total spending.
data_filled["Rank"]=data_filled["TotalAmount"].rank(method="dense",ascending=False)
print(data_filled[["Name","Spendercategory","TotalAmount","Rank"]].sort_values("Rank"))
#uppercase names, extract first/last names
data_filled["Name"]=data_filled["Name"].str.upper()
data_filled[["FirstName","LastName"]]=data_filled["Name"].str.split(" ",expand=True)
print(data_filled.head())
#Sort data, pivot/melt to reshape if needed, and visualize distributions (optional).