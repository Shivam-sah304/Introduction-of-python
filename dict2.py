""" Using dictionary comprehension, create a dictionary 
from a list of numbers where the key is
 the number and the value is its square."""
x=[]
squr_x=[]
i=int(input("Enter the number of elements : "))
for t in range(i):
    p=int(input("enter the your elements: "))
    x.append(p)
for k in  range(i):
    squr_x.append(x[k]**2)
print(squr_x)