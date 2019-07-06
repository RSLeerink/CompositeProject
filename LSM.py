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

    

