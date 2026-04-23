import pandas as pd

data={
    "Students":["Shruthi","Arun","Manu","Anu","Tanu","Ranu","Panu","Vanu","Ganu","Hanu"],
    "Marks":[50,40,45,56,87,93,50,86,47,90]

}
df=pd.DataFrame(data)
print(df)

print(df.loc[[2,3]])
print(df.loc[7])