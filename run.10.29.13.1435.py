import numpy as np
execfile('/home/rumbaugh/arrconv.py')
fields = ['Cl0023','Cl1324','RXJ1757','NEP5281','Cl1604']

bounds_dict = {'Cl0023': [0.82,0.87], 'Cl1324': [0.65,0.79], 'RXJ1757': [0.68,0.71], 'NEP5281': [0.8,0.84], 'Cl1604': [0.84,0.96]}
for field in fields:
    matchfile = '/home/rumbaugh/ORELSE/paperstuff/matched.%s.Xray_opt_spec.bothmatches_serendips.8.9.11.cat'%field
    cr = np.loadtxt(matchfile,dtype='string')
    q,z,pnm = str2int(cr[:,19]),str2float(cr[:,20]),str2float(cr[:,26])
    if field == 'Cl1604': pnm = str2float(cr[:,28])
    g = np.where((q > 2.5) & (pnm < 0.15) & ((z < bounds_dict[field][0]) | (z > bounds_dict[field][1])))[0]
    g2 = np.where((q > 2.5) & (pnm < 0.15) & (((z < bounds_dict[field][0]) & (z > 0.6)) | ((z > bounds_dict[field][1])&(z < 1.3))))[0]
    print '\n%s\nAll fore/background sources: %i\nORELSE fore/background sources: %i\n'%(field,len(g),len(g2))
    
