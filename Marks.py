import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Marks.csv")
print(df)

plt.scatter(df["Name"],df["Marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Students and marks")

plt.show()