data = {"City": ["Delhi", "Mumbai", "Kolkata"],
        "Temp": [30, 34, 29],
        "Humidity": [65, 70, 80]}
import pandas as pd
data1=pd.DataFrame(data)
data1.index=["DH","MU","KO"]
#print the data of dehli only
print(data1.loc[["DH"]])
#print the dta of delhi and kolkata
print(data1.iloc[[0,2]])
#print the only temp of mumbai
print(data1.iloc[[1],[1]])
#print only humidity of all data
print(data1.loc[:,['Humidity']])
#print temp and humidity of 1 and 0
print(data1.iloc[[1,0],[0,2]])
print(data1)