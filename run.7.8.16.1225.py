import numpy as np
execfile('/home/rumbaugh/setup_adam_cats.py')
execfile('/home/rumbaugh/set_spec_dict.py')

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053","cl1324_north","cl1324_south"])
indict={'names':('field','number','RA','Dec','lum_soft','lum_hard','lum_full','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit'),'formats':('|S32','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S32','|S32')}

crn=np.loadtxt('/home/rumbaugh/X-ray_lum_cat.7.8.16.dat',dtype=indict)
crn['field'][((crn['field']=='cl1324_north')|(crn['field']=='cl1324_south'))]='cl1324'

crRS = np.loadtxt('/home/rumbaugh/Chandra/RS_offsets_wACS.6.13.16.dat',dtype={'names':('field','number','ID','RA','Dec','RSoffset','magR','magI','magZ','SCmagRed','SCmagBlue'),'formats':('|S24','i8','|S24','f8','f8','f8','f8','f8','f8','f8','f8')})

crRS=crRS[crRS['number']>-1]


for field in targets[:-2]:
    gf=np.where((crRS['field']==field)&(crRS['number']>-1))[0]
    for i in range(0,len(gf)):
        gRS=np.where((crn['field']==field)&(crn['number']==crRS['number'][gf[i]]))[0][0]
        print np.sqrt((crRS['RA'][gf[i]]-crn['RA'][gRS])**2+(crRS['Dec'][gf[i]]-crn['Dec'][gRS])**2)
