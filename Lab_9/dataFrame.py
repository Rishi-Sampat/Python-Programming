import pandas as pd
data={'Name':['Alice','Bob','Charlie'],
      'Age':[25,30,35],
      'City':['New York','Los Angeles','Chicago']
      }
df=pd.DataFrame(data)
print(df)

#print(df[['Nam']])--key error
print(df[['Name']])

#df['Salary']=[70000,80000,90000,90]--value error
df['Salary']=[70000,80000,90000]
print(df)

df=df.drop('City',axis=1)#axis=0 = rows (default).axis=1 = columns.
print(df)

print(df.loc[[0]])
print(df.loc[[0,1]])