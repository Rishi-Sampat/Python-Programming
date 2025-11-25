import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="ticks")
df = sns.load_dataset("anscombe")
sns.lmplot(x="x", y="y", data=df)
plt.show()