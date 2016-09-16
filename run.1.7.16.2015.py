import numpy as np

mid=30.56

cr = np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/refcats/speccat.cl1324.radec.dat')
dec=cr[:,1]
np.savetxt('/home/rumbaugh/Chandra/ImperialPipeline/refcats/speccat.cl1324_north.radec.dat',cr[dec>30.56],fmt='%f %f',header='RA DEC')
np.savetxt('/home/rumbaugh/Chandra/ImperialPipeline/refcats/speccat.cl1324_south.radec.dat',cr[dec<30.56],fmt='%f %f',header='RA DEC')
