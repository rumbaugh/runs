import numpy as np
execfile('/home/rumbaugh/calc_Xray_lums.py')


nh_dict={"rxj1757": 4.08,"cl1604": 1.22,"cl0023": 2.79,"cl1324_north": 1.15,"cl1324_south": 1.16, 'cl1324': 1.155,"rxj1821":5.67, 'rcs0224': 2.86, 'cl0849': 2.73, 'rxj0910': 1.98,'rxj1053': 0.58, 'rxj1221':1.44,'cl1350':1.76,'rxj1716':3.71,'cl1137':1.93}

infile='/home/rumbaugh/combined_match_catalog.7.17.16.dat'

indict={'names':('field','number','RA','Dec','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','specID','mask','slit','bcnts_soft','bcnts_hard','bcnts_full','sigS','sigH','sigF'),'formats':('|S32','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S32','|S32','|S32','f8','f8','f8','f8','f8','f8')}

cr=np.loadtxt(infile,dtype=indict)


field='cl0849'
#oldfile='/home/rumbaugh/X-ray_lum_cat.1.13.16.dat'
#olddict={'names':('field','number','RA','Dec','lum_soft','lum_hard','lum_full','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit'),'formats':('|S32','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S32','|S32')}
#cro=np.loadtxt(oldfile,olddict)
#gf=np.zeros(0,dtype='i8')
#for i in range(0,np.shape(cr)[0]):
#    if cr['field'][i] in nh_dict.keys():
#        gf=np.append(gf,i)

g=np.where(cr['mask']=='Mei')[0]

nh=nh_dict[field]

fluxes=np.zeros((1,3))
fluxes[:,0],fluxes[:,1],fluxes[:,2]=cr['flux_soft'][g],cr['flux_hard'][g],cr['flux_full'][g]

calc_dict={'z': cr['redshift'][g], 'nh': nh, 'bands':{ 'names': np.array(['soft','hard','full']), 'kev': np.array([[0.5,2.0],[2.0,7.0],[0.5,7.0]])}, 'flux':fluxes}

lums=calc_Xray_lums(calc_dict)#,cosmocalcin='/home/rumbaugh/cc_out.1.7.16.dat')

FILE=open('/home/rumbaugh/X-ray_lum_cat.7.17.16.dat','w')
FILE.write('# field number RA Dec lum_soft lum_hard lum_full flux_soft flux_hard flux_full ncnts_soft ncnts_hard ncnts_full redshift mask slit sig_soft sig_hard sig_full\n')
for i in range(0,len(cr)): 
    FILE.write('%10s %2i %7.5f %7.5f %E %E %E %E %E %E %6.1f %6.1f %6.1f %5.3f %s %s %f %f %f\n'%(cr['field'][i],cr['number'][i],cr['RA'][i],cr['Dec'][i],lums[i][0],lums[i][1],lums[i][2],cr['flux_soft'][i],cr['flux_hard'][i],cr['flux_full'][i],cr['ncnts_soft'][i],cr['ncnts_hard'][i],cr['ncnts_full'][i],cr['redshift'][i],cr['mask'][i],cr['slit'][i],cr['sigS'][i],cr['sigH'][i],cr['sigF'][i]))#,cr['ncnts_soft'][i]/(1.+np.sqrt(0.75+cr['bcnts_soft'][i])),cr['ncnts_hard'][i]/(1.+np.sqrt(0.75+cr['bcnts_hard'][i])),cr['ncnts_full'][i]/(1.+np.sqrt(0.75+cr['bcnts_full'][i]))))
    #FILE.write('%10s %2i %7.5f %7.5f %E %E %E %E %E %E %6.1f %6.1f %6.1f %5.3f %s %s %6.1f %6.1f %6.1f \n'%(cr['field'][gf][i],cr['number'][gf][i],cr['RA'][gf][i],cr['Dec'][gf][i],cro['lum_soft'][i],cro['lum_hard'][i],cro['lum_full'][i],cr['flux_soft'][gf][i],cr['flux_hard'][gf][i],cr['flux_full'][gf][i],cr['ncnts_soft'][gf][i],cr['ncnts_hard'][gf][i],cr['ncnts_full'][gf][i],cr['redshift'][gf][i],cr['mask'][gf][i],cr['slit'][gf][i],cr['ncnts_soft'][gf][i]/(1.+np.sqrt(0.75+cr['bcnts_soft'][gf][i])),cr['ncnts_hard'][gf][i]/(1.+np.sqrt(0.75+cr['bcnts_hard'][gf][i])),cr['ncnts_full'][gf][i]/(1.+np.sqrt(0.75+cr['bcnts_full'][gf][i]))))
FILE.close()
