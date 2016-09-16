import numpy as np
import pyfits as py

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","rxj1821","cl1137","rxj1716","rxj1053","cl1324_north","cl1324_south"])


zlist=np.array([0.77,1.26,1.11,0.70,0.80,0.69,0.90,0.84,0.82,0.96,0.81,1.14,0.76,0.76])

cr=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.init_smooth_peaks.dat',dtype={'names':('field','id','ra','dec','imageX','imageY'),'formats':('|S24','|S24','f8','f8','f8','f8')})

band='full'
cutwid=25

ann_rads=np.arange(5,305,5)
maxann=ann_rads[-1]

FILE=open('/home/rumbaugh/Chandra/cl1604.cluster_ann_counts.dat','w')
FILE.write('# field cluster Xcen Ycen anncounts\n')
FILE2=open('/home/rumbaugh/Chandra/cl1604.cluster_ann_counts_noVC.dat','w')
FILE2.write('# field cluster Xcen Ycen anncounts\n')

for i in [6]:
    field,z=targets[i],zlist[i]
    curdir='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s'%(field,field)
    fitsfile='%s/%s_%s_nops.vig_corr.smoothed.z_%.2f.beta_0.67.rc_180kpc.img'%(curdir,field,band,z)
    imgfile='%s/%s_%s_nops.vig_corr.img'%(curdir,field,band)
    imgfile2='%s/%s_%s_nops.img'%(curdir,field,band)
    hdu=py.open(fitsfile)
    data=hdu[0].data
    hdux=py.open(imgfile)
    datax=hdux[0].data
    hdux2=py.open(imgfile2)
    datax2=hdux2[0].data
    g=np.where(field==cr['field'])[0]
    for j in range(0,len(g)):
        xt,yt=cr['imageX'][g[j]],cr['imageY'][g[j]]
        cutoutsml=data[yt-cutwid-1:yt+cutwid,xt-cutwid-1:xt+cutwid]
        centmp=np.where(cutoutsml==np.max(cutoutsml))
        xcen,ycen=centmp[1]+xt-cutwid-1,centmp[0]+yt-cutwid-1
        FILE.write('%12s %12s %7.2f %7.2f'%(field,cr['id'][g[j]],xcen,ycen))
        FILE2.write('%12s %12s %7.2f %7.2f'%(field,cr['id'][g[j]],xcen,ycen))
        cutout=datax[ycen-maxann-5:ycen+maxann+5,xcen-maxann-5:xcen+maxann+5]
        cutout2=datax[ycen-maxann-5:ycen+maxann+5,xcen-maxann-5:xcen+maxann+5]
        y,x=np.arange(ycen-maxann-5,ycen+maxann+5),np.arange(xcen-maxann-5,xcen+maxann+5)
        yx=np.meshgrid(y,x)
        rads=np.sqrt((yx[0]-ycen)**2+(yx[1]-xcen)**2)
        prevcnts=0
        prevcnts2=0
        for rad in ann_rads:
            cnts=np.sum(cutout[rads<=rad])
            cnts2=np.sum(cutout2[rads<=rad])
            FILE.write(' %7.2f'%(cnts-prevcnts))
            FILE2.write(' %7.2f'%(cnts2-prevcnts2))
            prevcnts=cnts
            prevcnts2=cnts2
        FILE.write('\n')
        FILE2.write('\n')
FILE.close()
FILE2.close()
        
        
        
        
