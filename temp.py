import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from glob import glob


filenames = glob('Strain*.csv')

dataframes = [pd.read_csv(f) for f in filenames]

#for i in np.arange(0,len(dataframes)):
#    print(dataframes[i])

df1 = dataframes[0]
df2 = dataframes[1]

a = abs(df1.iloc[0:1][:])
b = abs(df2.iloc[0:1][:])

#df1.plot(kind='scatter',x='X',y=df1.index.values,color='red')
#df1.plot.bar(x='X')
#plt.show()

c = df1.index.values
d = df1['X'].tolist()
e = df2['X'].tolist()

plt.plot(c, d)
plt.plot(c, e)
plt.show()
