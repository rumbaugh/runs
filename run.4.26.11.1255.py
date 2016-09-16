import numpy as np
import os
import math as m

try:
    usegal
except NameError:
    usegal = False
try:
    icenmax
except NameError:
    icenmax = 1
if usegal: icenmax = 2

emcen = (4093.65,4920.9909)
gcen = (4052.9508,4888.3027)


inrad = 50
for icen in range(0,icenmax):
    icenstr = 'EMcen'
    if icen == 1: icenstr = 'galcen'
    cenx,ceny = emcen[0],emcen[1]
    if icen == 1: cenx,ceny = gcen[0],gcen[1]
    FILE = open('/home/rumbaugh/ChandraData/Cl1324/master/fitres.%s.4.26.11.dat'%(icenstr),'w')
    for i in range(0,34):
        inrad += 10.0
        outrad1 = inrad + 50
        if outrad1 < 300: outrad1 = 300
        outrad2 = outrad1 + 50
        load_pha("/home/rumbaugh/ChandraData/Cl1324/master/spec.4.25.11/spec_%s_r_%i_4.25.11.pi"%(icenstr,inrad))
        ignore()
        notice(0.3,8.0)
        set_model(xsraymond.rs*xswabs.abs1)
        abs1.nh = 0.0115
        freeze(abs1.nh)
        rs.kT = 1
        rs.norm = 1
        thaw(rs.norm)
        rs.abundanc = 0.3
        rs.redshift = 0.69
        subtract()
        group_counts(20)
        fit()
        freeze(rs.norm)
        proj()
        res = get_proj_results()
        mint,maxt,valt = res.parmins,res.parmaxes,res.parvals
        mint,maxt,valt = mint[0],maxt[0],valt[0]
        if maxt == None: maxt = 99
        if mint == None: mint = -99
        FILE.write('%3i %5.1f %5.2f %5.2f %6.2f\n'%(int(inrad),inrad/2.0,valt,mint,maxt))
    FILE.close()
        
