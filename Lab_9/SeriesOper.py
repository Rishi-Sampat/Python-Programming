import pandas as pd
data=[1,2,3,4,5]
series=pd.Series(data)
series2=series+10
print(series2)

filtered=series[series>2]
print(filtered)

mean=series.mean()
print(mean)
