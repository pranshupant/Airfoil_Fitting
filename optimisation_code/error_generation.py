#import the name of the airfoils from the webtry program
#Generate a new airfoil using constructor for every specie and evaluate cost
#!Rename the airfoil to airfoil.txt for evaluation!
#make a new folder for every airfoil imported with sub folders for generation and species
#save the plot of every generation and specie in their respective folder. 

#only for upper array(the same can be repeated for lower array.)
#subtract Y values of corresponding elements and compute distance 
#Minimize the inverse of the distance b/w points
#write code for choosing which x values to subrract from (possibility to add interpolation values)
#Apply same IWO GA to minimize (Decide on the number of generations and other constants based on experimentation.)
#from web_try import airfoils
from airfoil_Class import airfoil
airfoils = 's1210.dat'
Airfoil = airfoil(0, 1)

Airfoil.ctrlPoints()
Airfoil.bspline()
#Airfoil.write()
#Airfoil.savefig()
#Airfoil.show(0, 1)
Airfoil.error(airfoils)
print(airfoils)



