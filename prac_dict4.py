#Create a dictionary where the keys are subjects and the values are lists of marks:
marks = {"Math": [78, 88], "Science": [90, 85], "English": [80, 75]}
#Add a new mark 95 to "Math".
marks["Math"].append(95)
sum=0
for x in marks["Science"]:
    sum=sum+x
average=sum/2
print("The average marks of science is " +str(average))
