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

LayerThickness = 1
FiberAngle = [0,0,0,0,0,0,0]

N = len(FiberAngle) #Amount of layers defined by amount of Fiber angles
df = LaminaStiffnessMatrix(E1,E2,V12,V21,G12,N)
df = TransformedLaminaStiffnessMatrix(df, FiberAngle)
z = z_LaminaPosition(LayerThickness,FiberAngle)
ABDdf = ABDMatrix(df,FiberAngle,z)