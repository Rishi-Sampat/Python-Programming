#a. Write a Python program to convert degree to radian
import math
degree=float(input("Enter the angle in degrees:"))
radian=degree*(math.pi/180)
print(f"{degree} degrees={radian} radians")

#b. Simplest Program for y = 6x² + 4sin(x)
x = float(input("Enter value of x: "))
y=6*(x**2)+4*math.sin(x)
print("y=",y)

#c. Write a Python function that evaluates the mathematical functions 𝑓(𝑥) = 𝑐𝑜𝑠(2𝑥),𝑓′(𝑥) = ―2sin(2𝑥), 𝑎𝑛𝑑 𝑓′′(𝑥) = ―4cos(2𝑥). Return these three values. Write out the results of these values for 𝑥 = 𝜋
def fn(x):
    f=math.cos(2*x)
    f1=(int)(-2*math.sin(2*x))
    f2=-4*math.cos(2*x)
    return f,f1,f2
x=math.pi
f,f1,f2=fn(x)
print("f(x)=",f)
print("f'(x)=",f1)
print("f''(x)=",f2)