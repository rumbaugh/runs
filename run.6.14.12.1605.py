import numpy as np
import math as m

names = np.array(['Cl1324+3011','Cl1324+3013','Cl1324+3059','RXJ1757','RXJ1821','Cl1604A','Cl1604B','RXJ0910+5419','RXJ0910+5422'])

decs = np.array([(30+(11+26/60.0)/60.0),(30+(12+52/60.0)/60.0),(30+(58+35/60.0)/60.0),(66+(31+29/60.0)/60.0),(68+(27+57/60.0)/60.0),(43+(4+39/60.0)/60.0),(43+(14+22/60.0)/60.0),(54+(18+56/60.0)/60.0),(54+(22+7/60.0)/60.0)])

cr = read_file("/home/rumbaugh/cc_out.6.1.12.nh.dat")
z = copy_colvals(cr,'col1')
Mpc2am  = copy_colvals(cr,'col12')*0.7
AMin250kpc = Mpc2am*0.25

for i in range(0,len(names)):
    print '%12s - 0.25 Mpc = %f as; %f$^{s}$\n'%(names[i],60*AMin250kpc[i],60*AMin250kpc[i]/m.cos(decs[i]*m.pi/180)*24/360.0)
