import numpy as np
import shutil

loaded_af = np.loadtxt('Airfoil_list.txt', dtype=str)

for number in range(350):

    name = loaded_af[number]

    shutil.rmtree('../fitting/%s/Plots'%name)
    shutil.rmtree('../fitting/%s/Camber'%name)
    shutil.rmtree('../fitting/%s/Results_CFD'%name)