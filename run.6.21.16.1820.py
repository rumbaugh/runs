import numpy as np
execfile('/home/rumbaugh/angconvert.py')
execfile('/home/rumbaugh/SphDist.py')

linfile='/home/rumbaugh/X-ray_lum_cat.6.21.16.dat'

lindict={'names':('field','number','RA','Dec','lum_soft','lum_hard','lum_full','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit','sigS','sigH','sigF'),'formats':('|S32','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S32','|S32','f8','f8','f8','f8','f8','f8')}

crl=np.loadtxt(linfile,dtype=lindict)
sigma=np.zeros((np.shape(crl)[0],3))
sigma[:,0],sigma[:,1],sigma[:,2]=crl['sigS'],crl['sigH'],crl['sigF']
sigma=np.max(sigma,axis=1)

crp=np.loadtxt('/home/rumbaugh/Chandra/clustocentric_dists.dat',dtype={'names':('field','number','RA','Dec','clusdist','veldist','p'),'formats':('|S24','i8','f8','f8','f8','f8','f8')})

crRS=np.loadtxt('/home/rumbaugh/Chandra/RS_offsets_wACS.6.13.16.dat',dtype={'names':('field','AGNnumber','specID','RA','Dec','RSoffset','magR','magI','magZ','SCmagRed','SCmagBlue'),'formats':('|S24','i8','|S48','f8','f8','f8','f8','f8','f8','f8','f8','f8')})
crRS=crRS[crRS['AGNnumber']>=0]

FILE=open('/home/rumbaugh/text4AGNtab.txt','w')

targets=np.array(["cl0023","rcs0224","cl0849","rxj0910","rxj1053","rxj1221","cl1324","cl1350","cl1604","rxj1716","rxj1757","rxj1821"])
names=np.array(["Cl0023","RCS0224","Cl0849","RXJ0910","RXJ1053","RXJ1221","Cl1324","Cl1350","Cl1604","RXJ1716","RXJ1757","RXJ1821"])

for field,name in zip(targets,names):
    gf=np.where((crl['field']==field)&(sigma>2))[0]
    gfp=np.where(crp['field']==field)[0]
    gfRS=np.where(crRS['field']==field)[0]
    if field=='cl1324':
        gf=np.where(((crl['field']==field)|(crl['field']=='cl1324_north')|(crl['field']=='cl1324_south'))&(sigma>2))[0]
        gfp=np.where((crp['field']==field)|(crp['field']=='cl1324_north')|(crp['field']=='cl1324_south'))[0]
        gfRS=np.where((crRS['field']==field)|(crRS['field']=='cl1324_north')|(crRS['field']=='cl1324_south'))[0]
    gas=gf[np.argsort(crl['redshift'][gf])]
    for i,icnt in zip(gas,np.arange(1,len(gas)+1)):
        tmpdist=SphDist(crl['RA'][i],crl['Dec'][i],crp['RA'][gfp],crp['Dec'][gfp])
        gp=gfp[np.argsort(tmpdist)[0]]
        tmpdist=SphDist(crl['RA'][i],crl['Dec'][i],crRS['RA'][gfRS],crRS['Dec'][gfRS])
        gRS=gfRS[np.argsort(tmpdist)[0]]
        dd,dm,ds=deg2dms(crl['Dec'][i])
        rah,ram,ras=deg2hms(crl['RA'][i])
        lums,lumh,lumf='%.1f'%(crl['lum_soft'][i]*1E-42),'%.1f'%(crl['lum_hard'][i]*1E-42),'%.1f'%(crl['lum_full'][i]*1E-42)
        if crl['lum_soft'][i]*1E-42<=0: lums='\\tablenotemark{e}'
        if crl['lum_hard'][i]*1E-42<=0<=0: lumh='\\tablenotemark{e}'
        if crl['lum_full'][i]*1E-42<=0<=0: lumf='\\tablenotemark{e}'
        FILE.write('%7s & %2i & %02i\\ %02i\\ %04.1f & %+03i\\ %02i\\ %04.1f & %5.3f & %s & %s & %s & %.2f & %.2f & %.2f \\\\\n'%(name,icnt,rah,ram,ras,dd,dm,ds,crl['redshift'][i],lums,lumh,lumf,sigma[i],crp['p'][gp],crRS['RSoffset'][gRS]))
FILE.close()
