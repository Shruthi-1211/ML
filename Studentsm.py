import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Student.csv")
print(df)

#plt.pie(df["Sum"],labels=df["Students"])
plt.pie(df["Average"],labels=df["Students"],autopct='%1.1f%%')
#plt.title("Students and marks")
plt.title("Students average marks")

plt.show()