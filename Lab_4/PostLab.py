#a. Multiply all the items in a list
import math
list1=[2,3,4]
print("Product of elements:",math.prod(list1))

res=1
for num in list1:
    res*=num
print("Product of elements:",res)

#b. Get the largest number from a list
list2=[3,90,123,1,-3]
print("Largest number:",max(list2))

#c. Remove duplicates from a list
list3=['a','a','a','b','c','d','d','e']
list3=list(dict.fromkeys(list3))
print(list3)

#d.Get the frequency of elements in a list
list4 = ['a','a','a','b','c','d','d','e']
freq={}
for i in list4:
    freq[i]=freq[i]+1 if i in freq else 1
print("Frequency of elements:",freq)

#e.find common items from two lists
list51=[1,2,3,4,5]
list52=[4,5,6,7,8]
print(list(set(list51)&set(list52)))

#f.Convert a list of multiple integers into a single integer
list6=[3,4,5,6,7]
print(int("".join(map(str,list6))))