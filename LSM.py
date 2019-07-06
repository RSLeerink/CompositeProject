import numpy as np
import pandas as pd

def LaminaStiffnessMatrix(E1,E2,V12,V21,G12,N):
    #Calculations
    Q11 = (E1/(1-V12*V21))          
    Q12 = ((V12*E1)/(1-V12*V21))    
    Q21 = Q12                       
    Q22 = (E2/(1-V12*V21))          
    Q66 = G12                       

    #Create lamina stifness matirx
    LSM =  np.zeros((3,3))
    LSM[0][0] = Q11
    LSM[0][1] = Q12
    LSM[1][0] = Q21
    LSM[1][1] = Q22
    LSM[2][2] = Q66

    #Creation of DataFrame for all of the composite
    df = pd.DataFrame({'Column1':LSM[:,0],
                            'Column2':LSM[:,1],
                            'Column3':LSM[:,2]})

    df = pd.concat([df]*N)

    #Export the DataFrame to text and csv 
    np.savetxt(r'LSM.txt', df.values, fmt='%5.2f', header  = 'Lamina stiffness matrix')
    df.to_csv (r'LSM.csv', index = True, header=True)
    return df 

def TransformedLaminaStiffnessMatrix(df,FiberAngle):
    
    Q11 = df.iloc[0][0]
    Q12 = df.iloc[0][1]
    Q22 = df.iloc[1][1]
    Q66 = df.iloc[2][2]

    i = 0
    for Angle in FiberAngle:
        s = np.sin(np.deg2rad(Angle)) 
        c = np.cos(np.deg2rad(Angle)) 

        Q_11 = Q11*c**4 + Q22*s**4+2*(Q12 + 2*Q66)*s**2*c**2
        Q_12 = (Q11 + Q22 -4*Q66)*s**2*c**2 + Q12*(c**4+s**4)
        Q_22 = Q11*s**4 +Q22*c**4 + 2*(Q12+2*Q66)*s**2*c**2
        Q_16 = (Q11 - Q12 - 2*Q66)*c**3*s - (Q22 - Q12 - 2*Q66)*c*s**3
        Q_26 = (Q11 - Q12 - 2*Q66)*s**3*c - (Q22 - Q12 - 2*Q66)*c**3*s
        Q_66 = (Q11 + Q22 - 2*Q12 - 2*Q66)*c**2*s**2 + Q66*(s**4 + c**4)

        # First row
        df.iloc[0+i][0] = Q_11
        df.iloc[0+i][1] = Q_12
        df.iloc[0+i][2] = Q_16
        # Secound row
        df.iloc[1+i][0] = Q_12
        df.iloc[1+i][1] = Q_22
        df.iloc[1+i][2] = Q_26
        # Third row
        df.iloc[2+i][0] = Q_16
        df.iloc[2+i][1] = Q_26
        df.iloc[2+i][2] = Q_66

        i = i + 3

    #print(df)

    #Export the DataFrame to text and csv 
    np.savetxt(r'LSM_Transformed.txt', df.values, fmt='%5.2f', header  = 'Lamina stiffness matrix')
    df.to_csv (r'LSM_Transformed.csv', index = True, header=True)
    return df

def ABDMatrix(df,FiberAngle,z):
    AmountLayers = list(range(0, len(FiberAngle)))
    
    #Create empty 6x6 matrix
    ABD =  np.zeros((6,6))
    ABDdf = pd.DataFrame({'Column1':ABD[:,0],
                                'Column2':ABD[:,1],
                                'Column3':ABD[:,2],
                                'Column4':ABD[:,3],
                                'Column5':ABD[:,4],
                                'Column6':ABD[:,5]})

    print('Amount of Layers= ' + str(AmountLayers))
    print('z= ' + str(z))

    y = 0 
    for i in [0,1,2]:
        for j in [0,1,2]:
            sumA = 0
            sumB = 0
            sumD = 0
            for k in AmountLayers:
                #print('i=' + str(i))
                #print('j=' + str(j))
                #print('y=' + str(y))

                sumA = sumA + df.iloc[i+y][j] * (z[k+1]     - z[k])
                sumB = sumB + df.iloc[i+y][j] * (z[k+1]**2  - z[k]**2)
                sumD = sumD + df.iloc[i+y][j] * (z[k+1]**3  - z[k]**3)


                y = y + 3
                if y == len(AmountLayers)*3:
                    y = 0

            ABDdf.iloc[i+y][j] =  sumA  #A extensional stiffness matrix
            ABDdf.iloc[i+y+3][j] =  (1/2) * sumB  #B coupling matrix
            ABDdf.iloc[i+y][j+3] =  (1/2) * sumB  #B coupling matrix
            ABDdf.iloc[i+y+3][j+3] = (1/3) * sumD  #D bending stiffness matrix

    np.savetxt(r'ABDMatrix.txt', ABDdf.values, fmt='%5.2f', header  = 'ABDMatrix')

    print(ABDdf)        
    return ABDdf

def z_LaminaPosition(LayerThickness,FiberAngle):
    AmountOfLayers = len(FiberAngle)
    TotalThickness = AmountOfLayers * LayerThickness

    z_LaminaPositions = []
    for i in list(range(0, len(FiberAngle)+1)):
        z_LaminaPositions.append(TotalThickness/2 - i*LayerThickness)
    
    z_LaminaPositions.reverse()
    print(z_LaminaPositions)
    
    return z_LaminaPositions

    

    

