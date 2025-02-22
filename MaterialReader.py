import pandas as pd
import math

#Input
#NameOfExcelFile where material data is saved
FileName = 'MaterialData.xlsx'
#Page 9 book
#MatrixMaterial = 'Hexply 8551-7 epoxy'
#FibertMaterial = 'E-glass'
#FibertMaterial = 'T-300 12K'
#Volumfraction for fiber
#vf = 0.65


def MaterialDataList(vf,MatrixMaterial,FibertMaterial):
    def Matrix_Material_Data(MatrixMaterial):
        df = pd.read_excel(FileName,sheet_name='Matrix Material' ,index_col=0)
        df = df.loc[MatrixMaterial,:]
        return df

    def Fiber_Material_Data(FibertMaterial):
        df = pd.read_excel(FileName,sheet_name='Fiber Material' ,index_col=0)
        df = df.loc[FibertMaterial,:]
        return df

    MMD = Matrix_Material_Data(MatrixMaterial)
    FMD = Fiber_Material_Data(FibertMaterial)

    print(MMD)
    print()
    print(FMD)
    #Calculating material data WORK IN PROFRESS CHECK FORMULAS
    vm = 1-vf
    Ef  = FMD[1]
    Em  = MMD[1]

    PoissonsRatioFiber  = FMD[6]
    PoissonsRatioMatrix = MMD[6]
    Gf12 = 0.0125
    GM = Em / (2 * (1 + vm))

    #Gibson Equation 3.27 page 121
    E1  = (Ef * vf) + (Em * vm)
    #E2  = ( 1 / ( (vf/Ef) + (vm/Em) ) ) #Not acceptable for design use

    #Gibson Equation 3.54 page 121
    E2 = Em * (( (1-vf) + ( (math.sqrt(vf))/(1 - math.sqrt(vf) * (1 - (Em)/(Ef))))))

    #G12 wrong nad v12 wrong at the moment
    v12 = (PoissonsRatioFiber*vf) + (PoissonsRatioMatrix * vm)
    V21 =  v12 * (E2/E1)
    G12 = ( 1 / ( (vf/Gf12) + (vm/GM) ) )

    # Out
    OutputMaterialDataList = [E1,E2,v12,V21,G12]

    return OutputMaterialDataList
    #Page 75
    #Page 111

#OutputMaterialDataList = MaterialDataList(vf,MatrixMaterial,FibertMaterial)
#print(OutputMaterialDataList)