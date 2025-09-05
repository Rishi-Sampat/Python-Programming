#a. Write a Python program to Count the occurrences of an element in a tuple
tu =('a','a','a','b','c','d','d','e')
freq={}
for i in tu:
    freq[i]=freq[i]+1 if i in freq else 1
print("Frequency of elements:",freq)

#b.Write a Python program to Check if an element exists in a tuple.
t=(10,20,30,40,50)
el=22
if el in t:
    print(f"{el} exists in the tuple")
else:
    print(f"{el} does not exist in the tuple")

#c. Write a Python program to Convert a tuple to a string.
t=('p','y','t','h','o','n')
print("Tuple converted to string:",''.join(t))

#d. Find the maximum and minimum elements in a tuple
t=(5,0,-3,1,0.6,4)
print("Maximum element:",max(t))
print("Minimum element:",min(t))

#e. Convert a tuple of strings to a single string
t=("Hello","World","Python")
print("Tuple converted to single string:"," ".join(t))

#f. Sort a tuple of integers
t=(5,1,-2,3,7)
print("Sorted:",tuple(sorted(t)))

#g. Find the first and last elements of a tuple
t = (10, 20, 30, 40, 50)

print("First element:", t[0])
print("Last element:", t[-1])