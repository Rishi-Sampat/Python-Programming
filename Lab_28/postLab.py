from plotnine.data import economics
from plotnine import ggplot, aes, geom_line
print(economics)
pl1=(
    ggplot(economics)
    + aes(x="date", y="pop")
    + geom_line()
)
print(pl1)
pl1.save(r"E:\College\Python Programming\Lab_28\postLab1.png")