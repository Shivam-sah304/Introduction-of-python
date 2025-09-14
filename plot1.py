x=[2,3,4,5,6,7]
y=[5,6,2,3,13,4]
import matplotlib.pyplot as plt
plt.plot(x,y)
plt.xlabel("X values")#adding x label
plt.ylabel("Y values")#adding y labels
plt.title("Normal value")#adding title
plt.show()
plt.clf() #cleaning the graph
plt.scatter(x,y)
plt.xlabel("X value")
plt.ylabel("Y values ")
plt.show()
