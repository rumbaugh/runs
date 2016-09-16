import numpy as np
import math as m

execfile("/home/rumbaugh/Load1938.py")

ltime,Aflux,Bflux,C1flux,C2flux,Aerr,Berr,C1err,C2err,Anflux,Bnflux,C1nflux,C2nflux,Anerr,Bnerr,C1nerr,C2nerr = Load1938()

FILE = open('/home/rumbaugh/B1938+666_files/B1938+666_image_fluxes.1.24.13.dat','w')

for i in range(0,len(ltime)): FILE.write('%f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f\n'%(ltime[i],Aflux[i],Bflux[i],C1flux[i],C2flux[i],Aerr[i],Berr[i],C1err[i],C2err[i],Anflux[i],Bnflux[i],C1nflux[i],C2nflux[i],Anerr[i],Bnerr[i],C1nerr[i],C2nerr[i]))
FILE.close()
