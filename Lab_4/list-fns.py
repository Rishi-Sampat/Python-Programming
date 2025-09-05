list=[1,2,3,4,5]
print(sum(list))

#List=['gfg','abc','3']
#print(sum(List))--type error

List=[1,2,3,1,2,1,2,3,2,1]
print(List.count(1))
List=['a','b','c','d','a']
print(List.count('a'))
print(List.count('e'))#--0
List=[1,2,3,1,2,1,2,3,2,1]
print(len(List))
print(List.index(2))
print(List.index(2,2))

num=[5,2,8,1,9]
print("Minimum",min(num))
print("Maximum",max(num))

List=[2,3,4,445,3,5,33,1.054,2,5]
List.sort()
print(List)
List=[2.3,4.445,3,5.33,1.054,2.5]
List.sort(reverse=True)#descending
print(List)

list=[1,2,3,4,5]
list.reverse()
print(list)
#print(list.reverse())--none
