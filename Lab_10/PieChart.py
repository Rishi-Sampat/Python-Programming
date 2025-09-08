import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
# this will explode the 1st wedge
# i.e. will separate the 1st wedge
e  =(0.1, 0, 0, 0)
# This will plot a simple pie chart
plt.pie(x, explode = e)
plt.title("Pie chart")
plt.show()
