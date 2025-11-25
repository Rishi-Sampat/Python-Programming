from plotnine import *
from plotnine.data import mtcars
print(mtcars.head())
p1=(ggplot(data=mtcars)
 + geom_point(mapping=aes(x="wt", y="mpg", color="factor(gear)"))
 + facet_wrap("~gear"))
print(p1)
p1.save("E:\College\Python Programming\Lab_28\plot1.png")

p2=(ggplot(data=mtcars)
 + geom_point(aes("wt","mpg",color="factor(gear)"))
)
print(p2)
p2.save("E:\College\Python Programming\Lab_28\plot2.png")

p3=(ggplot(data=mtcars)
 + geom_point(aes("wt","mpg",size="factor(gear)"))
)
print(p3)
p3.save("E:\College\Python Programming\Lab_28\plot3.png")

p4=(ggplot(data=mtcars)
+ geom_point(aes("wt", "mpg"), color='red')
)
print(p4)
p4.save("E:\College\Python Programming\Lab_28\plot4.png")