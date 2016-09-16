import numpy as np


names = np.array(['RXJ1821','RXJ1757','Cl1324+3059','Cl1324+3011','Cl1324+3013','Cl1604A','Cl1604B','0910+5422','0910+5419'])
crc = read_file("/home/rumbaugh/cc_out.6.29.12.nh.dat")
Hz = get_colvals(crc,'col5')*0.7
Ez = Hz/70.0

crl = read_file('/home/rumbaugh/paperstuff/clus.lums.bol.10.19.12.dat')
lumbol = copy_colvals(crl,'col1')*Ez
lumbol500 = copy_colvals(crl,'col2')*Ez
lumbolT = copy_colvals(crl,'col3')*Ez
lumbolerr = copy_colvals(crl,'col4')*Ez
lumbol500err = copy_colvals(crl,'col5')*Ez
lumbolTerr = copy_colvals(crl,'col6')*Ez

for i in range(0,len(Ez)): print '%12s: \nL500: %7.3f +/- %7.3f\nLtot: %7.3f +/- %7.3f\n'%(names[i],lumbol500[i],lumbol500err[i],lumbolT[i],lumbolTerr[i])
