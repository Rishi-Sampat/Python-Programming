import pandas as pd
dat = pd.read_csv("E:\College\Python Programming\Lab_9\data.csv")
print(dat.info())
print(dat.head())
print(dat.tail())
print(dat.describe())

print(dat[['Name']])
print(dat[['Name','Number']])
print(dat.loc[[1]])
