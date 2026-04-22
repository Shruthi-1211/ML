import numpy as np
import matplotlib.pyplot as plt

x=[10,20,30,40,50]
y=[100,205,310,422,500]
plt.plot(x,y,marker='o')

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Simple line plot")

plt.grid()
plt.show()