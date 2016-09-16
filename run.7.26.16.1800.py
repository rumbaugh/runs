import numpy as np
from ConcaveHull import ConcaveHull,CheckPoints
from shapely.geometry import box as makebox
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/set_spec_dict.py')
execfile('/home/rumbaugh/setup_adam_cats.py')
execfile('/home/rumbaugh/SphDist.py')
targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053","cl1324_north","cl1324_south"])

alpha_ref,alphaX = 11.1,1.1
mtol=1.
ldate='1.19.16'
crcc=np.loadtxt('/home/rumbaugh/cc_out.2.19.16.dat')
D_L=crcc[:,13]*3.086E22
DM=crcc[:,15]
kpc=crcc[:,12]
cc_z=crcc[:,0]

alphas=[1.1,5.1,10.1,20.1,50.1,100.1]

for field in ['cl1324']:
    refcat='%s/%s/%s.mag.gz'%(refdir,reffile_dict[field],reffile_dict[field])
    if field=='rxj1821':
        cr=np.loadtxt(refcat,dtype=refdict_1821)
    elif field in ['cl1324','rxj0910']:
        cr=np.loadtxt(refcat,dtype=refdict0910)
    else:
        cr=np.loadtxt(refcat,dtype=refdict)
    #FILE=open('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s.photz_inspeccov.4.23.16.dat'%(field,field,field),'w')
    #FILE.write('# ID in ConcaveHull with alpha=1.1, 5.1, 10.1, 20.1, 50.1, 100.1\n')
    crs=np.loadtxt('%s/%s'%(spec_dict['basepath'],spec_dict[field]['file']),dtype=specloaddict)
    ra_opt,dec_opt=crs['ra'],crs['dec']
    inCH_arr=np.zeros((len(cr['ra']),len(alphas)+1),dtype='i8')
    inCH_arr[:,0]=np.array(cr['ID'],dtype='i8')
    for ia,alpha in zip(np.arange(len(alphas)),alphas):
        
        CH_ref = np.zeros((len(ra_opt),2))
        CH_ref[:,0],CH_ref[:,1]=ra_opt,dec_opt
        CHull_ref,edges_ref=ConcaveHull(CH_ref,alpha)
        gCH=CheckPoints(CHull_ref,cr['ra'],cr['dec'])
        inCH_arr[:,1+ia][gCH]=1
    np.savetxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s.photz_inspeccov.4.23.16.dat'%(field,field,field),inCH_arr,fmt='%i %i %i %i %i %i %i')
