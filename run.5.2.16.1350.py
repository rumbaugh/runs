import numpy as np
execfile('/home/rumbaugh/calc_Xray_lums.py')
execfile('/home/rumbaugh/set_spec_dict.py')

targets=['cl0023','rxj1716']

crk=np.loadtxt('/home/rumbaugh/Chandra/k_Imp.3.7.16.dat',dtype={'names':('field','k_soft','k_hard','k_full'),'formats':('|S24','f8','f8','f8')})
gk=np.zeros(2,dtype='i8')
for i in range(0,len(targets)):gk[i]=np.where(crk['field']==targets[i])[0][0]

nh_dict={"rxj1757": 4.08,"cl1604": 1.22,"cl0023": 2.79,"cl1324_north": 1.15,"cl1324_south": 1.16, 'cl1324': 1.155,"rxj1821":5.67, 'rcs0224': 2.86, 'cl0849': 2.73, 'rxj0910': 1.98,'rxj1053': 0.58, 'rxj1221':1.44,'cl1350':1.76,'rxj1716':3.71,'cl1137':1.93}

nh_arr=[nh_dict[x] for x in targets]

#fluxes=np.zeros((len(nh_arr),3))
#fluxes[:,0],fluxes[:,1],fluxes[:,2]=cr['flux_soft'],cr['flux_hard'],cr['flux_full']
fluxes=np.zeros((len(nh_arr),1))
fluxes[:,0]=6.*crk['k_full'][gk]

#calc_dict={'z': cr['redshift'], 'nh': nh_arr, 'bands':{ 'names': np.array(['soft','hard','full']), 'kev': np.array([[0.5,2.0],[2.0,7.0],[0.5,7.0]])}, 'flux':fluxes}
calc_dict={'z': [spec_dict[x]['z'][0] for x in targets], 'nh': nh_arr, 'bands':{ 'names': np.array(['full']), 'kev': np.array([[0.5,7.0]])}, 'flux':fluxes}

lums=calc_Xray_lums(calc_dict,cosmocalcin='/home/rumbaugh/tmp_cc_out.dat')
print lums,lums/22.
calc_dict['flux']*=5.6/6.
lums=calc_Xray_lums(calc_dict,cosmocalcin='/home/rumbaugh/tmp_cc_out.dat')

print lums,lums/23.
