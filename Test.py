from LSM import LaminaStiffnessMatrix
from LSM import TransformedLaminaStiffnessMatrix
import numpy as np
import pandas as pd

#Inputs
E1 = 30
E2 = 4
V12 = 0.3
V21 = 0.3
G12 = 3

FiberAngle = [0,90,45,0,90,45,0]

N = len(FiberAngle) #Amount of layers defined by amount of Fiber angles
df = LaminaStiffnessMatrix(E1,E2,V12,V21,G12,N)
df = TransformedLaminaStiffnessMatrix(df, FiberAngle)


