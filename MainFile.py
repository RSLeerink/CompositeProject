from CLT_FunctionsFile import LaminaStiffnessMatrix
from CLT_FunctionsFile import TransformedLaminaStiffnessMatrix
from CLT_FunctionsFile import z_LaminaPosition
from CLT_FunctionsFile import ABDMatrix
from CLT_FunctionsFile import Strain
from CLT_FunctionsFile import Stress
from CLT_FunctionsFile import InputData
import numpy as np
import pandas as pd

#Inputs 
E1 = 30                 #MPa
E2 = 4                  #MPa
V12 = 0.3               #Unitless
V21 =  V12 * (E2/E1)    #Unitless
G12 = 3                 #Unitless

LayerThickness = 1
FiberAngle = [0,0,0,0]
NM = np.array([0,0,0,0,300,0])

#Calculations
#N = len(FiberAngle) #Amount of layers defined by amount of Fiber angles
InputData(E1,E2,V12,V21,G12)
LSMdf = LaminaStiffnessMatrix(E1,E2,V12,V21,G12,FiberAngle)
LSMdf = TransformedLaminaStiffnessMatrix(LSMdf, FiberAngle)
z = z_LaminaPosition(LayerThickness,FiberAngle)
ABDdf = ABDMatrix(LSMdf,FiberAngle,z)
Straindf = Strain(ABDdf,NM,z)
Stress(LSMdf,Straindf)

