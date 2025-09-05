t1=(2,3,4,5)
print(sum(t1))

t3=(3,4,4,2,2,3,6,7,4,4)
print(t3.count(4))
print(t3.index(2))#returns the index of the first occurrence
print(t3.index(4,3,9))#tuple.index(x, start, end)
print(min(t3))

num=(7,2,8,5,9)
print(max(num))

a=(5,6,7,5,5,9,7)
b=("a","b","v","b")
tu1=tuple(dict.fromkeys(a))
print(tu1)
tu2=tuple(dict.fromkeys(b))
print(tu2)

first_names = ('Simon', 'Sarah', 'Mehdi', 'Fatime')
last_names = ('Sinek', 'Smith', 'Lotfinejad', 'Lopes')
ages=(49,55,39,33)
com=tuple(zip(first_names,last_names,ages))
print(com)

b=((1,2),(3,4),(5,6))
tu=tuple(item for l in b for item in l)
print(tu)