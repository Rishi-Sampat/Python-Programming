import pandas as pd
df=pd.read_csv(r"E:\College\Python Programming\Lab_22\sample_data.csv")
#a
print(df.dtypes)

#b
df['Age']=df['Age'].fillna(df['Age'].mean())
print(df)

#Name,Age,City
#Alice,30,New York
#Bob,25,Los Angeles
#Charlie,35,Chicago