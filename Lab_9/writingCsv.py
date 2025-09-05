import pandas as pd
Biodata={'Name':['John','Emily','Mike','Lisa'],
         'Age':[28,23,35,31],
         'Gender':['M','F','M','F']
         }
df=pd.DataFrame(Biodata)
print(df)
df.to_csv('Biodata.csv',index=False)