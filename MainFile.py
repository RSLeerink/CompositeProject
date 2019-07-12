from CLT_FunctionsFile import LaminaStiffnessMatrix
from CLT_FunctionsFile import TransformedLaminaStiffnessMatrix
from CLT_FunctionsFile import z_LaminaPosition
from CLT_FunctionsFile import ABDMatrix
from CLT_FunctionsFile import Strain
from CLT_FunctionsFile import Stress
from CLT_FunctionsFile import InputData
from CLT_FunctionsFile import FileNameDef
from datetime import datetime
import numpy as np
import pandas as pd
from pandas import DataFrame


#Start of time tracking for script run time
T1 = datetime.now()

#FileNaming
ProjectName = 'Test'
LayuppNumber = '1'
#Include Time stamp?0 = no, 1 = yes
TimeStamp = 0
#Include Angle? 0 = no, 1 = yes
Angle = 1


#Inputs 
E1 = 30                 #MPa
E2 = 4                  #MPa
V12 = 0.3               #Unitless
V21 =  V12 * (E2/E1)    #Unitless
G12 = 3                 #Unitless

LayerThickness = 1
FiberAngle = [45,90,90,45]
NM = np.array([0,0,0,0,200,0])

#
#
#   Input end
#
#

Options  = {'ProjectName': [ProjectName],
            'LayuppNumber' : [LayuppNumber],
            'TimeStamp': [TimeStamp],
            'Angle': [Angle],
            }

Options =  DataFrame(Options, columns = ['ProjectName','LayuppNumber','TimeStamp','Angle'])
FileName = FileNameDef(Options,FiberAngle)
InputData(E1,E2,V12,V21,G12,FiberAngle)
LSMdf = LaminaStiffnessMatrix(E1,E2,V12,V21,G12,FiberAngle)
LSMdf = TransformedLaminaStiffnessMatrix(LSMdf, FiberAngle)
z = z_LaminaPosition(LayerThickness,FiberAngle)
ABDdf = ABDMatrix(LSMdf,FiberAngle,z)
Straindf = Strain(ABDdf,NM,z)
Stressdf = Stress(LSMdf,Straindf,z)
Stressdf = Stressdf.reset_index()

#Output to html
#Stressdf.to_html('filename.html')

#Straindf.to_csv(FileName + ' Strain.csv',index=False)
Stressdf.to_csv(FileName + ' Stress.csv',index=False)

print()
print('FileName:' + FileName)
#Shows how long the script took to run
T2 = datetime.now()
TRun = T2 - T1
print('Script took ' + str(TRun) +' to run') 
print('Script ran successfully')
