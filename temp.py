FiberAngle = [0,0,0]
z = [-1.5,-0.5,0.5,1.5]

a = len(FiberAngle)
print(list(range(0, a)))

X = list(range(0, len(FiberAngle)+1))

LayerThickness = 1
AmountOfLayers = len(FiberAngle)
TotalThickness = AmountOfLayers * LayerThickness

z = []
for i in X:
    z.append(TotalThickness/2 - i)

print(z)