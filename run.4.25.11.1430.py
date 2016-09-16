import numpy as np
import os

emcen = (4093.65,4920.9909)
gcen = (4052.9508,4888.3027)
crps = read_file("/home/rumbaugh/ChandraData/Cl1324/master/psources.9403+9840.full.reg")
psarr = get_colvals(crps,'col1')

inrad = 50
for icen in range(0,2):
    icenstr = 'EMcen'
    if icen == 1: icenstr = 'galcen'
    cenx,ceny = emcen[0],emcen[1]
    if icen == 1: cenx,ceny = gcen[0],gcen[1]
    for i in range(0,34):
        inrad += 10.0
        outrad1 = inrad + 50
        if outrad1 < 300: outrad1 = 300
        outrad2 = outrad1 + 50
        FILE = open('/home/rumbaugh/ChandraData/Cl1324/master/sources.4.25.11/EM.%s.r_%i.4.25.11.reg'%(icenstr,inrad),'w')
        FILE.write('circle(%f,%f,%f)\n'%(cenx,ceny,inrad))
        for ps in psarr: FILE.write(ps + '\n')
        FILE.close()
        FILE = open('/home/rumbaugh/ChandraData/Cl1324/master/sources.4.25.11/BG.%s.r_%i.4.25.11.reg'%(icenstr,inrad),'w')
        FILE.write('circle(%f,%f,%f)\n-circle(%f,%f,%f)\n'%(cenx,ceny,outrad2,cenx,ceny,outrad1))
        for ps in psarr: FILE.write(ps + '\n')
        FILE.close()
        ost = os.system('specextract infile="/home/rumbaugh/ChandraData/Cl1324/master/acis9403+9840.evt2.fits[sky=region(/home/rumbaugh/ChandraData/Cl1324/master/sources.4.25.11/EM.%s.r_%i.4.25.11.reg)]" bkgfile="/home/rumbaugh/ChandraData/Cl1324/master/acis9403+9840.evt2.fits[sky=region(/home/rumbaugh/ChandraData/Cl1324/master/sources.4.25.11/BG.%s.r_%i.4.25.11.reg)]" outroot="/home/rumbaugh/ChandraData/Cl1324/master/spec.4.25.11/spec_%s_r_%i_4.25.11" pbkfile="/home/rumbaugh/ChandraData/Cl1324/master/acis9403.pbk.fits" grouptype=NUM_CTS binspec=15 clob+'%(icenstr,inrad,icenstr,inrad,icenstr,inrad))

