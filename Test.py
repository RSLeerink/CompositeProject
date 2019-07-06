from LSM import LaminaStiffnessMatrix
from LSM import TransformedLaminaStiffnessMatrix
import numpy as np
import pandas as pd

#Inputs
E1 = 30
E2 = 4
V12 = 0.3
V21 =  V12 * (E2/E1)
G12 = 3

FiberAngle = [0,0,0]
z = [-1.5,-0.5,0.5,1.5]

N = len(FiberAngle) #Amount of layers defined by amount of Fiber angles
df = LaminaStiffnessMatrix(E1,E2,V12,V21,G12,N)
df = TransformedLaminaStiffnessMatrix(df, FiberAngle)

def ABDMatrix(df):
    ABD =  np.zeros((6,6))
    ABDdf = pd.DataFrame({'Column1':ABD[:,0],
                                'Column2':ABD[:,1],
                                'Column3':ABD[:,2],
                                'Column4':ABD[:,3],
                                'Column5':ABD[:,4],
                                'Column6':ABD[:,5]})

    y = 0 
    for i in [0,1,2]:
        for j in [0,1,2]:
            sumA = 0
            sumB = 0
            sumD = 0
            for k in [0,1,2]:
                #y = 0
                #print('i=' + str(i))
                #print('j=' + str(j))
                #print('y=' + str(y))

                sumA = sumA + df.iloc[i+y][j] * (z[k+1]     - z[k])
                sumB = sumB + df.iloc[i+y][j] * (z[k+1]**2  - z[k]**2)
                sumD = sumD + df.iloc[i+y][j] * (z[k+1]**3  - z[k]**3)


                y = y + 3
                if y == 9:
                    y = 0

            ABDdf.iloc[i+y][j] =  sumA  #A extensional stiffness matrix
            ABDdf.iloc[i+y+3][j] =  (1/2) * sumB  #B coupling matrix
            ABDdf.iloc[i+y][j+3] =  (1/2) * sumB  #B coupling matrix
            ABDdf.iloc[i+y+3][j+3] = (1/3) * sumD  #D bending stiffness matrix
    print(ABDdf)        
    return ABDdf
    

ABDdf = ABDMatrix(df)