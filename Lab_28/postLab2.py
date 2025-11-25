from plotnine.data import mpg
from plotnine import ggplot, aes, geom_point

pl2=ggplot(mpg) + aes(x="class", y="hwy") + geom_point()
print(pl2)
pl2.save(r"E:\College\Python Programming\Lab_28\postLab2.png")