import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from glob import glob


filenames = glob('*Strain.csv')
print(filenames)

dataframes = [pd.read_csv(f) for f in filenames]
print(dataframes)

#for i in np.arange(0,len(dataframes)):
#    print(dataframes[i])

df1 = dataframes[0]
df2 = dataframes[1]

a = abs(df1.iloc[0:1][:])
b = abs(df2.iloc[0:1][:])

#df1.plot(kind='scatter',x='X',y=df1.index.values,color='red')
#df1.plot.bar(x='X')
#plt.show()

#c = df1.index.values
#d = df1['X'].tolist()
#e = df2['X'].tolist()


#plt.xlabel('Layer')
#plt.ylabel('X Strain')
plt.title('Strain distribution in composite')
plt.grid(True)

#fig, (ax1, ax2) = plt.subplots(1, 2)
ax1 = plt.subplot(221)
ax2 = plt.subplot(222)
ax3 = plt.subplot(223)

for i in [0,1,2]:
    df = dataframes[i]
    #a = df.index.values
    #a = df.index.values
    a = df.index.values + 1
    XList = df['X'].tolist()
    YList = df['Y'].tolist()
    XYList = df['XY'].tolist()




    #ax1 = plt.subplot()
    ax1.plot(a,XList)
    ax1.title.set_text('X strain distribution')
    plt.xlabel('Layer')
    plt.ylabel('X Strain')
    ax1.grid(True)
    plt.xticks(a)
    
    #ax2 = plt.subplot()
    ax2.plot(a,YList)
    ax2.title.set_text('Y strain distribution')
    plt.xlabel('Layer')
    plt.ylabel('Y Strain')
    ax2.grid(True)
    plt.xticks(a)

    #ax3 = plt.subplot(223)
    ax3.plot(a,XYList)
    ax3.title.set_text('XY strain distribution')
    plt.xlabel('Layer')
    plt.ylabel('XY Strain')
    ax3.grid(True)
    plt.xticks(a)

plt.legend(filenames,loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()





