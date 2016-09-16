import numpy as np
execfile('/home/rumbaugh/calc_Xray_lums.py')
execfile('/home/rumbaugh/angconvert.py')
execfile('/home/rumbaugh/SphDist.py')

nh_dict={"rxj1757": 4.08,"cl1604": 1.22,"cl0023": 2.79,"cl1324_north": 1.15,"cl1324_south": 1.16,"rxj1821":5.67}

infile='/home/rumbaugh/combined_match_catalog.1.5.16.dat'

indict={'names':('field','number','RA','Dec','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit'),'formats':('|S32','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S32','|S32')}

cr=np.loadtxt(infile,dtype=indict)

nh_arr=np.zeros(len(cr['redshift']))
for field in nh_dict.keys():
    nh_arr[cr['field']==field]=nh_dict[field]

fluxes=np.zeros((len(nh_arr),3))
fluxes[:,0],fluxes[:,1],fluxes[:,2]=cr['flux_soft'],cr['flux_hard'],cr['flux_full']

calc_dict={'z': cr['redshift'], 'nh': nh_arr, 'bands':{ 'names': np.array(['soft','hard','full']), 'kev': np.array([[0.5,2.0],[2.0,7.0],[0.5,7.0]])}, 'flux':fluxes}

lums=calc_Xray_lums(calc_dict,cosmocalcin='/home/rumbaugh/cc_out.1.5.16.dat')

FILE=open('/home/rumbaugh/X-ray_lum_nonh_cat.1.5.16.dat','w')
FILE.write('# field number RA Dec lum_soft lum_hard lum_full flux_soft flux_hard flux_full ncnts_soft ncnts_hard ncnts_full redshift mask slit\n')
for i in range(0,len(nh_arr)):
    nncS,nfS,nncH,nfH,nncF,nfF=0.,0.,0.,0.,0.,0.
    field=cr['field']
    if field != 'cl1604':
        cr_op=np.loadtxt('/home/rumbaugh/Chandra/%s/photometry/%s.xray_phot.soft_hard_full.dat'%(obsid_dict[field],obsid_dict[field]))
    else:
        crtmp1,crtmp2=np.loadtxt('/home/rumbaugh/Chandra/6932/photometry/6932.xray_phot.soft_hard_full.dat'),np.loadtxt('/home/rumbaugh/Chandra/6933+7343/photometry/6933+7343.xray_phot.soft_hard_full.dat')
        cr_op=np.append(crtmp1,crtmp2,axis=0)
        oldra,olddec,oldfluxS,oldfluxH,oldfluxF,oldncntsS,oldncntsH,oldncntsF=cr_op[:,0],cr_op[:,1],cr_op[:,2],cr_op[:,3],cr_op[:,4],cr_op[:,5],cr_op[:,6],cr_op[:,7]
        gtmp=np.where((np.abs(oldra-cr['ra'][i])/np.cos(cr['dec'][i])<stol)&(np.abs(olddec-cr['dec'][i])<stol))[0]
        if len(gtmp)!=0: 
            disttmp=SphDist(oldra[gtmp],olddec[gtmp],crs['ra'][i],crs['dec'][i])
            gas=np.argsort(disttmp)
            gz=gtmp[gas[:1]]
            nncS,nncH,nncF,nfS,nfH,nfF=oldncntsS[gz],oldncntsH[gz],oldncntsF[gz],oldfluxS[gz],oldfluxH[gz],oldfluxF[gz]
    FILE.write('%10s %2i %7.5f %7.5f %E %E %E %E %E %E %6.1f %6.1f %6.1f %5.3f %s %s\n'%(cr['field'][i],cr['number'][i],cr['RA'][i],cr['Dec'][i],lums[i][0],lums[i][1],lums[i][2],cr['flux_soft'][i],cr['flux_hard'][i],cr['flux_full'][i],cr['ncnts_soft'][i],cr['ncnts_hard'][i],cr['ncnts_full'][i],cr['redshift'][i],cr['mask'][i],cr['slit'][i]))
FILE.close()
