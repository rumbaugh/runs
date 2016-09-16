import numpy as np
execfile('/home/rumbaugh/LoadEVLA_2011.py')
for source in np.concatenate((['J1414+4554','J1400+6210','J1545+4751','J0003+4807','J1823+7938','J1945+7055','J1816+3457','J1826+1831','J1734+0926'],['J0427+4133','J0204+0903','J0754+5324'],['B1938+666','B0712+472','MG0414+0534'])):
    if source == 'B1938+666':
        crS = np.loadtxt('/mnt/data2/rumbaugh/EVLA/11A-138/light_curves/lc_out.B1938+666.5.7.14.dat',dtype={'names': ('EorL','gnum','SBnum','day','fluxC1','fluxB','fluxC2','fluxA','fluxB2','fluxA2'), 'formats': ('|S8','i4','|S2','f8','f8','f8','f8','f8','f8','f8')})
        imgnames = ['fluxC1','fluxC2','fluxB','fluxA']
    elif source == 'MG0414+0524':
        crS = np.loadtxt('/mnt/data2/rumbaugh/EVLA/11A-138/light_curves/lc_out.MG0414+0534.5.7.14.dat',dtype={'names': ('EorL','gnum','SBnum','day','fluxA1','fluxA2','fluxB','fluxC'), 'formats': ('|S8','i4','|S2','f8','f8','f8','f8','f8')})
        imgnames = ['fluxA1','fluxA2','fluxB','fluxC']
    elif source == 'B0712+472':
        crS = np.loadtxt('/mnt/data2/rumbaugh/EVLA/11A-138/light_curves/lc_out.B0712+472.5.7.14.dat',dtype={'names': ('EorL','gnum','SBnum','day','fluxA','fluxB','fluxC','fluxD'), 'formats': ('|S8','i4','|S2','f8','f8','f8','f8','f8')})
        imgnames = ['fluxA','fluxB','fluxC','fluxD']
    else:
        crS = np.loadtxt('/mnt/data2/rumbaugh/EVLA/11A-138/light_curves/lc_out.%s.5.7.14.dat'%source,dtype={'names': ('EorL','gnum','SBnum','day','flux'), 'formats': ('|S8','i4','|S2','f8','f8')})
        imgnames = ['flux']
    gsort = np.argsort(crS['day'])
    FILE = open('/mnt/data2/rumbaugh/EVLA/11A-138/light_curves/lc_sort.%s.5.14.14.dat'%source,'w')
    for i in range(0,len(gsort)):
        FILE.write('%5s %i %2s %6.2f'%(crS['EorL'][gsort[i]],crS['gnum'][gsort[i]],crS['SBnum'][gsort[i]],crS['day'][gsort[i]]))
        for img in imgnames: FILE.write(' %f'%crS[img][gsort[i]])
        for img in imgnames: FILE.write(' %f'%(crS[img][gsort[i]]/np.mean(crS[img][crS[img]>0])))
        FILE.write('\n')
    FILE.close()
