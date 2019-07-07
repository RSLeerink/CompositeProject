import numpy as np

FiberAngle = [0,0,0]
z = [-1.5,-0.5,0.5,1.5]

a = len(FiberAngle)
print(list(range(0, a)))

X = list(range(0, len(FiberAngle)+1))

LayerThickness = 1
AmountOfLayers = len(FiberAngle)
TotalThickness = AmountOfLayers * LayerThickness

a=np.arange(1,4)
print(type(a))
a = np.vstack(a)

print(a)