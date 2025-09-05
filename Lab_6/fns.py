add=lambda x,y:x+y
print(add(3,5))


def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)
print(fact(5))