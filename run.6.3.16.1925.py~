import numpy as np
execfile('/home/rumbaugh/calc_Xray_lums.py')
execfile("/home/rumbaugh/set_spec_dict.py")
execfile('/home/rumbaugh/cosmocalc.py')


nh_dict={"rxj1757": 4.08,"cl1604": 1.22,"cl0023": 2.79,"cl1324_north": 1.15,"cl1324_south": 1.16, 'cl1324': 1.155,"rxj1821":5.67, 'rcs0224': 2.86, 'cl0849': 2.73, 'rxj0910': 1.98,'rxj1053': 0.58, 'rxj1221':1.44,'cl1350':1.76,'rxj1716':3.71,'cl1137':1.93}

zdummy=np.linspace(0.65,1.28,1000)

fluxes=np.zeros((len(zdummy),3))
fluxes[:,0],fluxes[:,1],fluxes[:,2]=np.ones(len(zdummy)),np.ones(len(zdummy)),np.ones(len(zdummy))
fluxes*=1E-14


targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053"])
zlist=np.zeros(len(targets))
nhlist=np.zeros(len(targets))
for i in range(0,len(targets)): 
    zlist[i]=spec_dict[targets[i]]['z'][0]
    nhlist[i]=nh_dict[targets[i]]
gzs=np.argsort(zlist)
targets,nhlist,zlist=targets[gzs],nhlist[gzs],zlist[gzs]

lumout=np.zeros((len(zdummy),3*len(nhlist)+1))
lumout[:,0]=zdummy

cosmocalcin='tmp_cc_out.dat'
cosmocalc(zdummy,outfile=cosmocalcin)

for i in range(0,len(nhlist)):
    calc_dict={'z': zdummy, 'nh': nhlist[i], 'bands':{ 'names': np.array(['soft','hard','full']), 'kev': np.array([[0.5,2.0],[2.0,7.0],[0.5,7.0]])}, 'flux':fluxes}
    lums=calc_Xray_lums(calc_dict,cosmocalcin='tmp_cc_out.dat')
    lumout[:,1+3*i:4+3*i]=lums
np.savetxt('/home/rumbaugh/fluxcalc.6.3.16.cat',lumout)
