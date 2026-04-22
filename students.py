import matplotlib.pyplot as plt
import numpy as np
students=["Arun","Bina","Suru","Chetan","Manu"]
marks=[75,65,99,87,90]
plt.scatter(marks,students)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Students Marks")
plt.grid()
plt.show()
