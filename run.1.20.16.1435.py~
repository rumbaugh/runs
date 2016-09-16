import numpy as np
execfile('/home/rumbaugh/calc_Xray_lums.py')

nh_dict={"rxj1757": 4.08,"cl1604": 1.22,"cl0023": 2.79,"cl1324_north": 1.15,"cl1324_south": 1.16,"rxj1821":5.67}

infile='/home/rumbaugh/combined_match_catalog.1.7.16.dat'

indict={'names':('field','number','RA','Dec','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit'),'formats':('|S32','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S32','|S32')}

cr=np.loadtxt(infile,dtype=indict)

nh_arr=np.zeros(len(cr['redshift']))
for field in nh_dict.keys():
    nh_arr[cr['field']==field]=nh_dict[field]

fluxes=np.zeros((len(nh_arr),3))
fluxes[:,0],fluxes[:,1],fluxes[:,2]=cr['flux_soft'],cr['flux_hard'],cr['flux_full']

calc_dict={'z': cr['redshift'], 'nh': nh_arr, 'bands':{ 'names': np.array(['soft','hard','full']), 'kev': np.array([[0.5,2.0],[2.0,7.0],[0.5,7.0]])}, 'flux':fluxes}

lums=calc_Xray_lums(calc_dict,cosmocalcin='/home/rumbaugh/cc_out.1.7.16.dat')

FILE=open('/home/rumbaugh/X-ray_lum_cat.1.13.16.dat','w')
FILE.write('# field number RA Dec lum_soft lum_hard lum_full flux_soft flux_hard flux_full ncnts_soft ncnts_hard ncnts_full redshift mask slit\n')
for i in range(0,len(nh_arr)):
    FILE.write('%10s %2i %7.5f %7.5f %E %E %E %E %E %E %6.1f %6.1f %6.1f %5.3f %s %s\n'%(cr['field'][i],cr['number'][i],cr['RA'][i],cr['Dec'][i],lums[i][0],lums[i][1],lums[i][2],cr['flux_soft'][i],cr['flux_hard'][i],cr['flux_full'][i],cr['ncnts_soft'][i],cr['ncnts_hard'][i],cr['ncnts_full'][i],cr['redshift'][i],cr['mask'][i],cr['slit'][i]))
FILE.close()
