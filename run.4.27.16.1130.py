import numpy as np
execfile('/home/rumbaugh/calc_Xray_lums.py')

refdir='/home/rumbaugh/git/ORELSE/Catalogs/tomczak_catalogs'
reffile_dict={"cl0023":'sg0023+0423_v0.1.9','cl1604':'sc1604_v0.0.3','rxj1757':'nep200_v0.0.4','rxj1821':'nep5281_v0.0.1','rxj1716':'rxj1716+6708_v0.0.7'}

FILE=open('/home/rumbaugh/Chandra/lums_newphotoz_adam.4.27.16.dat','w')
FILE.write('# ID RA Dec z_peak nh lum_soft lum_hard lum_full\n')
cr=np.loadtxt('/home/rumbaugh/Chandra/fluxes_newphotoz_adam.4.27.16.dat',dtype={'names':('field','ID','RA','Dec','z_peak','nh','flux_soft','flux_hard','flux_full'),'formats':('|S24','i8','f8','f8','f8','f8','f8','f8','f8')})
fluxes=np.zeros((len(cr['ID']),3))
fluxes[:,0],fluxes[:,1],fluxes[:,2]=cr['flux_soft'],cr['flux_hard'],cr['flux_full']
calc_dict={'z': cr['z_peak'], 'nh': cr['nh'], 'bands':{ 'names': np.array(['soft','hard','full']), 'kev': np.array([[0.5,2.0],[2.0,7.0],[0.5,7.0]])}, 'flux':fluxes}

lums=calc_Xray_lums(calc_dict)
for i in range(0,len(cr['ID'])):
    FILE.write('%12s %i %9.5f %9.5f %f %f %E %E %E\n'%(cr['field'][i],cr['ID'][i],cr['RA'][i], cr['Dec'][i],cr['z_peak'][i], cr['nh'][i],lums[i][0],lums[i][1],lums[i][2]))
FILE.close()
