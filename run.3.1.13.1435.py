import numpy as np
import matplotlib.pyplot as py
import smoothing_1d as sm
execfile("/home/rumbaugh/arrconv.py")
execfile("/home/rumbaugh/Load1938.py")
ltime,Aflux,Bflux,C1flux,C2flux,Aerr,Berr,C1err,C2err,Anflux,Bnflux,C1nflux,C2nflux,Anerr,Bnerr,C1nerr,C2nerr = Load1938(obskey1938='/home/rumbaugh/B1938+666_files/PartialObskey_Late.8.30.12.dat')

FILE = open('/home/rumbaugh/B1938+666_files/B1938+666_reduced_fluxes.3.1.13.dat','w')

for i in range(0,len(ltime)): FILE.write('%f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f\n'%(ltime[i],Aflux[i],Bflux[i],C1flux[i],C2flux[i],Aerr[i],Berr[i],C1err[i],C2err[i],Anflux[i],Bnflux[i],C1nflux[i],C2nflux[i],Anerr[i],Bnerr[i],C1nerr[i],C2nerr[i]))
FILE.close()
