from constants import maxIt, Gen0, sigma_final, sigma_initial, exponent, nPop
from airfoil_Class import airfoil#, baby_airfoil
import subprocess as sp
import os
import numpy as np
from error_reproduction import reproduction
from multiprocessing import Pool
import time as t

Airfoil = []
c = []
st = [0]
s = np.array(st)
final_cost = []
gen = 0
loaded_af = np.loadtxt('Airfoil_list.txt', dtype='str')

try:
	if not os.path.isdir('../fitting'):
		os.mkdir('../fitting')  
except FileExistsError:
	print('Fitting already Exists...')
	pass 

def run(number):

    af = loaded_af[number]
    
    name = loaded_af[number]
    #print(name) 

    os.mkdir('../fitting/%s'%name)
    os.chdir('../fitting/%s'%name)
    #os.mkdir('Plots')
    #os.mkdir('Camber')
    os.mkdir('error')
    t.sleep(2)
    
    Airfoil.clear()

    for i in range(Gen0):
        
        gen = 0
        s[0] = 0
        Airfoil.append(airfoil(0,i))
        Airfoil[i].ctrlPoints()
        Airfoil[i].bspline()
        Airfoil[i].write()
        #Airfoil[i].savefig()
        #Airfoil[i].show(gen, i)
        #Airfoil[i].camber(gen, i)


    for i in range(Gen0):
        #Airfoil[i].savefig()
        #Airfoil[i].xFoil()
        #Airfoil[i].cfd()
        try:
            Airfoil[i].error(af)
            gen = 1
        except IndexError:
            gen = maxIt

        except ValueError:
            gen = maxIt

        #print(Airfoil[i].cost)

    
    if __name__ == "__main__":

        while gen < maxIt:

            sigma = (((maxIt - float(gen-1))/maxIt)**exponent)*(sigma_initial - sigma_final) + sigma_final

            #print('SIGMA')
            #print(sigma)

            Airfoil.sort(key = lambda Airfoil: Airfoil.cost, reverse = True)

            for i in range(len(Airfoil)):
                #print(Airfoil[i].cost)
                pass

            del Airfoil[nPop:]


            for i in range(len(Airfoil)):
                #print(Airfoil[i].cost)
                pass

            for k in range(nPop):
                Airfoil[k].copy(gen, s[0])
                Airfoil[k].copy_Results(gen, s[0])
                #Airfoil[k].show(gen, s[0])
                #Airfoil[k].camber(gen, s[0])
                s[0] += 1 


            for x in range(len(Airfoil)):
                reproduction(Airfoil, gen, sigma, x, s, af)    

            Airfoil.sort(key = lambda x: x.cost, reverse = True)

            gen += 1 
            s[0] = 0   

        if gen == maxIt:
            final_cost.append(Airfoil[0].cost)
            c.append(Airfoil[0].cost)
            np.savetxt('Airfoil-Cost.txt', c, fmt= '%s')
            c.clear()
            print('%s Done'%name)
            
    os.chdir('../../optimisation_code')
    np.savetxt('Airfoil-Cost.txt', final_cost, fmt= '%s')
	
y = Pool()
y.map(run, range(len(loaded_af)))

y.close()

y.join()

    


