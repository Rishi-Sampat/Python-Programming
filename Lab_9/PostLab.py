import pandas as pd
import numpy as np
#a. Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
data1=[1,2,3,4,5]
data2=[1,2,3,4,5]
series1=pd.Series(data1)
series2=pd.Series(data2)
print(series1,"\n",series2)

seriesAdd=series1+series2
print("ADD")
print(seriesAdd)

seriesSub=series1-series2
print("Sub")
print(seriesSub)

seriesPro=series1*series2
print("Pro")
print(seriesPro)

seriesDiv=series1/series2
print("DIV")
print(seriesDiv)

#b. Write a Pandas program to convert a dictionary to a Pandas series.
dict={'a': 100, 'b': 200, 'c': 300, 'd': 400}
series=pd.Series(dict)
print("Dictionary to Series:")
print(series)

#c. Write a Pandas program to create a series from a list, numpy array and dict
list_data = [10, 20, 30, 40]
series_list = pd.Series(list_data)
print("Series from list:")
print(series_list)

arr_data = np.array([1, 2, 3, 4, 5])
series_array = pd.Series(arr_data)
print("\nSeries from NumPy array:")
print(series_array)

dict_data={'a': 10, 'b': 20, 'c': 30, 'd': 40}
series_dict=pd.Series(dict_data)
print("Dictionary to Series:")
print(series_dict)

#d. Write a Pandas program to stack two series vertically and horizontally
s1 = pd.Series([1, 2, 3, 4])
s2 = pd.Series([5, 6, 7, 8])

vertical_stack = pd.concat([s1, s2])
print("Vertical Stack:")
print(vertical_stack)

horizontal_stack = pd.concat([s1, s2], axis=1)
print("\nHorizontal Stack:")
print(horizontal_stack)