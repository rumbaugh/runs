import numpy as np
execfile('/home/rumbaugh/calc_Xray_lums.py')
execfile('/home/rumbaugh/set_spec_dict.py')

fields=['cl0023','rxj1716']
bands=['soft','hard','full']
netcnts=np.zeros(2)

crk=np.loadtxt('/home/rumbaugh/Chandra/k_Imp.3.7.16.dat',dtype={'names':('field','k_soft','k_hard','k_full'),'formats':('|S24','f8','f8','f8')})
#fig=plt.figure(1)
gks={}
for i in range(len(fields)):
    gk=np.where(crk['field']==fields[i])[0]
    gks[fields[i]]=gk[0]

nh_dict={"rxj1757": 4.08,"cl1604": 1.22,"cl0023": 2.79,"cl1324_north": 1.15,"cl1324_south": 1.16, 'cl1324': 1.155,"rxj1821":5.67, 'rcs0224': 2.86, 'cl0849': 2.73, 'rxj0910': 1.98,'rxj1053': 0.58, 'rxj1221':1.44,'cl1350':1.76,'rxj1716':3.71,'cl1137':1.93}

for s in [1,2]:
    cr=np.loadtxt('/home/rumbaugh/sample%s_aperphot.dat'%s,dtype={'names':('sample','band','netflux','nflux_err','netcnts','ncnts_err','srccnts','bkgcnts','srcarea','bkgarea','numsrc'),'formats':('|S24','|S24','f8','f8','f8','f8','f8','f8','f8','f8','i8')})
    fluxes=np.zeros((len(cr['band'])/3,3))
    zs,nhs=np.zeros(2),np.zeros(2)
    for sample,ic in zip(['cut','nocut'],np.arange(0,2)):
        meannh,meanz,numsrc=0.,0.,0.
        for field in fields:
            cro=np.loadtxt('/home/rumbaugh/sample%i_%s.image_cut.w_PSF.reg'%(s,field),skiprows=3,dtype='|S256')
            crpnc=np.loadtxt('/home/rumbaugh/sample%i_%s.phys_nocut.reg'%(s,field),skiprows=3,dtype='|S256')
            crinc=np.loadtxt('/home/rumbaugh/sample%i_%s.image_nocut.reg'%(s,field),skiprows=3,dtype='|S256')
            crnc=np.loadtxt('/home/rumbaugh/sample%i_%s.image_nocut.w_PSF.reg'%(s,field),skiprows=1,dtype='|S256')
            if sample=='cut':
                crt=np.copy(cro)
            else:
                crt=np.copy(crnc)
            numsrc+=len(crt)
            meanz+=len(crt)*spec_dict[field]['z'][0]
            meannh+=len(crt)*nh_dict[field]
        meanz/=numsrc
        meannh/=numsrc
        zs[ic]=meanz
        nhs[ic]=meannh
        for band,ib in zip(bands,np.arange(0,len(bands))):
            gb=np.where((cr['sample']==sample)&(cr['band']==band))[0]
            fluxes[ic][ib]=3*cr['nflux_err'][gb]
        
    calc_dict={'z': zs, 'nh': nhs, 'bands':{ 'names': np.array(['soft','hard','full']), 'kev': np.array([[0.5,2.0],[2.0,7.0],[0.5,7.0]])}, 'flux':fluxes}
    lums=calc_Xray_lums(calc_dict)
    FILE=open('/home/rumbaugh/sample%s_aperphot_wlum.dat'%s,'w')
    FILE.write('# sample band lum_lim(3sig) netflux netflux_err netcnts netcnts_err srccnts bkgcnts srcarea bkgarea num_src\n')
    for sample,ic in zip(['cut','nocut'],np.arange(0,2)):
        for band,ib in zip(bands,np.arange(0,len(bands))):
            gb=np.where((cr['sample']==sample)&(cr['band']==band))[0]
            FILE.write('%5s %4s %E %E %E %.2f %.2f %.2f %.2f %.2f %.2f %i\n'%(sample,band,lums[ic][ib]/cr['numsrc'][gb],cr['netflux'][gb],cr['nflux_err'][gb],cr['netcnts'][gb],cr['ncnts_err'][gb],cr['srccnts'][gb],cr['bkgcnts'][gb],cr['srcarea'][gb],cr['bkgarea'][gb],cr['numsrc'][gb]))
    FILE.close()
        
        
