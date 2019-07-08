import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import sys 


# WhatToPlot: 1 = Strain, 2 = Stress
WhatToPlot = 2

if WhatToPlot == 1:
    WhatToPlot = "Strain"
    print('Strain')
elif WhatToPlot == 2:
    WhatToPlot = "Stress"
    print("Stress")
else:
    print('Error WhatToPlot needs to be 1 or 2')
    sys.exit() 

#filenames = glob('*Strain.csv')
filenames = glob('*' + WhatToPlot + '.csv')
print(filenames)

dataframes = [pd.read_csv(f) for f in filenames]
print(dataframes)



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

    #Reading each axis for each csv file
    XList = df[Xref].tolist()
    YList = df[Yref].tolist()
    XYList = df[XYref].tolist()

    
    ax1.plot(a,XList)
    ax1.title.set_text(Xref)
    plt.xlabel('Position')
    plt.ylabel(Xref)
    ax1.grid(True)
    plt.xticks(a)
    
    ax2.plot(a,YList)
    ax2.title.set_text(Yref)
    plt.xlabel('Position')
    plt.ylabel(Yref)
    ax2.grid(True)
    plt.xticks(a)

    ax3.plot(a,XYList)
    ax3.title.set_text(XYref)
    plt.xlabel('Position')
    plt.ylabel(XYref)
    ax3.grid(True)
    plt.xticks(a)

plt.legend(filenames,loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()
print("Script ran with no problem")




