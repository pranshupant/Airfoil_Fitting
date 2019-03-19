import numpy as np

a = []
loaded_af = np.loadtxt('Airfoil_list.txt', dtype=str)

for number in range(len(loaded_af)):       #len of loaded airfoil
    name = loaded_af[number]
    p = 0
    try:
        se = np.loadtxt('../fitting/%s/Airfoil-Cost.txt'%name, dtype=float)#put in try and except   
        p = 1     
    except OSError:
        print('%s'%name)
    
    try:
        pts = np.loadtxt('coord/%s.dat'%name, dtype = float, skiprows=2)#change to coord

    except ValueError:
        print('%s pts BT'%name)
    
    if p == 1:
    
        n_pts = len(pts) + 2
    
        s = float(se)
        inv = s/n_pts
        mse = 1/inv
        #print(mse)
        a.append(mse)
    
        f = open('MSE_airfoil.txt', 'a+')
        f.write(name)
        f.write(' ')
        f.write(str(mse))
        f.write('\n')
        f.close()

