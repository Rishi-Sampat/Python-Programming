import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = {'Name':[ 'Rishi','Sweta','Rahul','Vensi'],
        'Age':[ 30,22,29,25]}
df=pd.DataFrame(data)
sns.violinplot( data['Age'])
plt.show()