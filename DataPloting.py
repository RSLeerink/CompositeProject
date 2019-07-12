import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import sys 


#
#
#   Options start
#
#

# WhatToPlot: 1 = Strain, 2 = Stress
WhatToPlot = 2

#
#
#   Options end
#
#

#Selction for what to plot
if WhatToPlot == 1:
    WhatToPlot = "Strain"
    print('Strain')
elif WhatToPlot == 2:
    WhatToPlot = "Stress"
    print("Stress")
else:
    print('Error WhatToPlot needs to be 1 or 2')
    sys.exit() 

#   Reads the selected option to plot
filenames = glob('*' + WhatToPlot + '.csv')
print(filenames)

#   Creates dataframes from selected files
dataframes = [pd.read_csv(f) for f in filenames]
#print(dataframes)


if WhatToPlot == "Strain":
    #Strain
    Xref = 'X'
    Yref = 'Y'
    XYref = 'XY'
elif WhatToPlot == "Stress":
    #Stress
    Xref = 'Sigma X (Mpa)'
    Yref = 'Sigma Y (Mpa)'
    XYref = 'Shear XY (Mpa)'
else:
    print("Crash")
    sys.exit()

plt.title('Strain distribution in composite')
plt.grid(True)

ax1 = plt.subplot(221)
ax2 = plt.subplot(222)
ax3 = plt.subplot(223)

for i in list(range(0, len(filenames))):

    df = dataframes[i]

    #Layer number
    a = df.index.values + 1

    #X ticks lable
    X_Index = []
    k = 1
    while k < len(a):
        print(k)
        X_Index.append(str(k) + '-Top')
        k = k + 1
        X_Index.append(str(k) + '-Bottom')
        k = k + 1

    #a = str(a) + 'xxx'
    print(a)
    print(X_Index)
    #Reading each axis for each csv file
    XList = df[Xref].tolist()
    YList = df[Yref].tolist()
    XYList = df[XYref].tolist()

    
    ax1.plot(a,XList)
    ax1.title.set_text(Xref)
    #plt.ylabel(Xref)
    ax1.grid(True)
    ax1.set_xticks(a)
    ax1.set_xticklabels(X_Index)
    ax1.set_xlabel('Position')
    ax1.set_ylabel(Xref)
    
    ax2.plot(a,YList)
    ax2.title.set_text(Yref)
    #plt.xlabel('Position')
    #plt.ylabel(Yref)
    ax2.grid(True)
    ax2.set_xticks(a)
    ax2.set_xticklabels(X_Index)
    ax2.set_xlabel('Position')
    ax2.set_ylabel(Yref)

    ax3.plot(a,XYList)
    ax3.title.set_text(XYref)
    #plt.ylabel(XYref)
    ax3.grid(True)
    ax3.set_xticks(a)
    ax3.set_xticklabels(X_Index)
    ax3.set_xlabel('Position')
    ax3.set_ylabel(XYref)


plt.tight_layout()
plt.legend(filenames,loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()
print("Script ran with no problem")




