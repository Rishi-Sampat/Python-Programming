import numpy as np
import pandas as pd
#manipulation
data={
    'A':[np.nan,2,3,4,5,6,7,8,9,10],
    'B':np.random.normal(50,15,10),
    'C':np.random.rand(10)*100,
    'D':np.linspace(1,10,10),
    'E':np.logspace(1,2,10)
}
df=pd.DataFrame(data)
print(df)