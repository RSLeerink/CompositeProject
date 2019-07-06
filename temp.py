z = [-1.5,-0.5,0.5,1.5]


v = 0
y = 0 
for i in [0,1,2]:
    for j in [0,1,2]:
        sumA = 0
        for k in [0,1,2]:

            #print('y=' + str(y))
            print('k=' + str(k))
            print('z[k+1]=' + str(z[k+1]))
            print('z[k]=' + str(z[k]))
            print('z[k+1] - z[k]=' + str(z[k+1] - z[k]))
            #print(z[k+1] - z[k])
            
            y = y + 2
            if y == 6:
                y = 0

            #print('i=' + str(i))
            #print('j=' + str(j))
            #print(v)
            
            #v = v + 1 
print(z[0])
print(z[1])
print(z[2])
print(z[3])
