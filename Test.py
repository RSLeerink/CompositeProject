from LSM import LaminaStiffnessMatrix
from LSM import TransformedLaminaStiffnessMatrix
from LSM import z_LaminaPosition
from LSM import ABDMatrix
import numpy as np
import pandas as pd

#Inputs
E1 = 30
E2 = 4
V12 = 0.3
V21 =  V12 * (E2/E1)
G12 = 3

LayerThickness = 0.5
FiberAngle = [45,-45,0,-45,45]
NM = np.array([0,0,0,0,300,0])


#Calculations
N = len(FiberAngle) #Amount of layers defined by amount of Fiber angles
df = LaminaStiffnessMatrix(E1,E2,V12,V21,G12,N)
df = TransformedLaminaStiffnessMatrix(df, FiberAngle)
z = z_LaminaPosition(LayerThickness,FiberAngle)
ABDdf = ABDMatrix(df,FiberAngle,z)

#Strain
ABDInverse = np.linalg.inv(ABDdf)

kth = np.dot(ABDInverse,NM*10**-3)
eps_0 = kth[0:3:1]
kap_0 = kth[3:6:1]

zsurface = np.zeros(((len(z) - 1) * 2,))

s = 0
z = np.ravel(z)

#Aranges the top and bottom for each lamina
for i in np.arange(1,int(len(zsurface)/2)):
    zsurface[i + s] = z[i]
    s = s + 1
    zsurface[i + s] = z[i]
zsurface[0] = z[0]
zsurface[-1] = z[-1]

#Makes the strain dataframe
Straindf = pd.DataFrame(columns=['X', 'Y', 'XY'])

#Loop that find the strain on eash lamina
for i in np.arange(0,len(zsurface)):
    StrainLayer =  eps_0 + zsurface[i] * kap_0
    Straindf.loc[i] = StrainLayer

print(Straindf)