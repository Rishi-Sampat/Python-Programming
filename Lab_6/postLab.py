#a. Write a Python program to print all odd numbers between 1 to 100 using a while loop.
i=1
while i<=100:
    if(i%2!=0):
        print(i,end=" ")
    i+=1
    
#b. Write a Python program to find the sum of all natural numbers between 1 to n.
n=int(input("\nEnter the natural number:"))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

#c.Write a Python function program to count a number of digits in a number.
n=111
c=0
while(n>0):
    c=c+1
    n//=10
print(c)

#d.Write a Python program to find the first and last digits of a number.
n=10
n=abs(n)
last=n%10
first=n
while(first>=10):
    first//=10
print(f"Last digit:{last},first digit:{first}")

n=10
n=abs(n)
last=n%10
first=n
while(first>=10):
    first//=10
temp=first
first=last
last=temp
print(f"swapped:\nfirst:{first},last:{last}")

#f.Write a Python program to calculate the product of digits of a number.
n=12
pro=1
while n>0:
    r=n%10
    pro*=r
    n//=10
print(pro)

#g.Write a Python program to enter a number and print its reverse
n=23
rev=0
while n>0:
    rev=rev*10+(n%10)
    n//=10
print(rev)
