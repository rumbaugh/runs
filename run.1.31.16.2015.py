import numpy as np
import pyfits as py

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","rxj1821","cl1137","rxj1716","rxj1053","cl1324_north","cl1324_south"])


zlist=np.array([0.77,1.26,1.11,0.70,0.80,0.69,0.90,0.84,0.82,0.96,0.81,1.14,0.76,0.76])

cr=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clusters_Xray.dat',dtype={'names':('field','cluster','ra','dec','z','nh','kT','lb','ub','rsn'),'formats':('|S24','|S24','f8','f8','f8','f8','f8','f8','f8','f8')})
testfield=np.zeros(np.shape(cr)[0],dtype='|S128')
for i in range(0,len(testfield)): testfield[i]=cr['field'][i].lower()

cr0=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.XYzeropoints.dat',dtype={'names':('field','x0','y0'),'formats':('|S24','i8','i8')})

crx=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clusters_Xray.dat',dtype={'names':('field','cluster','ra','dec','z','nh','kt','lb','ub','rsn'),'formats':('|S24','|S24','f8','f8','f8','f8','f8','f8','f8','f8')})
testclus=np.zeros(np.shape(crx)[0],dtype='|S128')
for i in range(0,len(testclus)): testclus[i]=crx['cluster'][i].lower()

band='full'
cutwid=25

ann_rads=np.arange(5,305,5)
maxann=ann_rads[-1]

FILE=open('/home/rumbaugh/Chandra/ORELSE.cluster_netcounts.dat','w')
FILE.write('# field cluster ncntsS cntsS bkgcntsS ncnts_noVCS cnts_noVCS bkgcnts_noVCS speccenXS speccenYS specradS ncntsH cntsH bkgcntsH ncnts_noVCH cnts_noVCH bkgcnts_noVCH speccenXH speccenYH specradH ncntsF cntsF bkgcntsF ncnts_noVCF cnts_noVCF bkgcnts_noVCF speccenXF speccenYF specradF bkgcenXF bkgcenYF bkgradF\n')

for i in np.arange(len(targets)):
    field,z=targets[i],zlist[i]
    g0=np.where(field==cr0['field'])[0][0]
    x0,y0=cr0['x0'][g0],cr0['y0'][g0]
    curdir='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s'%(field,field)
    fitsfile='%s/%s_%s_nops.vig_corr.smoothed.z_%.2f.beta_0.67.rc_180kpc.img'%(curdir,field,band,z)
    g=np.where(field==testfield)[0]
    for j in range(0,len(g)):
        cluster=cr['cluster'][g[j]]
        gx=np.where(cluster.lower()==testclus)[0][0]
        if crx['kt'][gx]>0:
            crbkg=np.array([np.loadtxt('%s/%s_bkg_spec.reg'%(curdir,cluster),dtype='|S128')])[0]
            FILE.write('%12s %12s '%(field,cluster))
            for band in ['soft','hard','full']:
                imgfile='%s/%s_%s_nops.vig_corr.img'%(curdir,field,band)
                imgfile2='%s/%s_%s_nops.img'%(curdir,field,band)
                hdux=py.open(imgfile)
                datax=hdux[0].data
                hdux2=py.open(imgfile2)
                datax2=hdux2[0].data
                crspec=np.loadtxt('%s/tmp_%s_%s_spec.reg'%(curdir,cluster,band),dtype='|S128')
                if np.shape(crspec)==():
                    crspec=np.array([crspec])[0]
                else:
                    crspec=crspec[0]
                specregstrtmp=crspec.split(',')
                xtmp,ytmp,radtmp=specregstrtmp[0].split('('),float(specregstrtmp[1]),specregstrtmp[2].split(')')
                xtmp,radt=float(xtmp[1]),float(radtmp[0])
                xt,yt=xtmp-x0,ytmp-y0
                cutoutspec=datax[yt-radt-2:yt+radt+1,xt-radt-2:xt+radt+1]
                cutoutspec2=datax2[yt-radt-2:yt+radt+1,xt-radt-2:xt+radt+1]
                y,x=np.arange(yt-radt-2,yt+radt+1),np.arange(xt-radt-2,xt+radt+1)
                yx=np.meshgrid(y,x)
                rads=np.sqrt((yx[0]-yt)**2+(yx[1]-xt)**2)
                cnts=np.sum(cutoutspec[rads<=radt])
                cnts2=np.sum(cutoutspec2[rads<=radt])

                bkgregstrtmp=crbkg.split(',')
                bxtmp,bytmp,bradtmp=bkgregstrtmp[0].split('('),float(bkgregstrtmp[1]),bkgregstrtmp[2].split(')')
                bxtmp,bradt=float(bxtmp[1]),float(bradtmp[0])
                bxt,byt=bxtmp-x0,bytmp-y0
                cutoutbkg=datax[byt-bradt-2:byt+bradt+1,bxt-bradt-2:bxt+bradt+1]
                cutoutbkg2=datax2[byt-bradt-2:byt+bradt+1,bxt-bradt-2:bxt+bradt+1]
                y,x=np.arange(byt-bradt-2,byt+bradt+1),np.arange(bxt-bradt-2,bxt+bradt+1)
                yx=np.meshgrid(y,x)
                brads=np.sqrt((yx[0]-byt)**2+(yx[1]-bxt)**2)
                bkgcnts=np.sum(cutoutbkg[brads<=bradt])
                bkgcnts2=np.sum(cutoutbkg2[brads<=bradt])
                FILE.write('%7.2f %7.2f %7.2f %7.2f %7.2f %7.2f %4i %4i %4i '%(cnts-bkgcnts*(radt*1./bradt)**2,cnts,bkgcnts,cnts2-bkgcnts2*(radt*1./bradt)**2,cnts2,bkgcnts2,xt,yt,radt))
            FILE.write('%4i %4i %4i\n'%(bxt,byt,bradt))
FILE.close()
        
        
        
        
