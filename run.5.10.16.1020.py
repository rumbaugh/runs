import numpy as np
from ConcaveHull import ConcaveHull,CheckPoints
from shapely.geometry import box as makebox
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/set_spec_dict.py')
execfile('/home/rumbaugh/SphDist.py')
targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053","cl1324_north","cl1324_south"])

alpha1,alphaX = 11.1,1.1
alpha2,alphaX = 50.1,1.1
mtol=1.
ldate='1.19.16'
optmatchloaddict={'names':('indX','raX','decX','errX','nummatch','raopt1','decopt1','optID1','Popt1','likeopt1','raopt2','decopt2','optID2','Popt2','likeopt2','raopt3','decopt3','optID3','Popt3','likeopt3','probnone'),'formats':('i8','f8','f8','f8','i8','f8','f8','|S32','f8','f8','f8','f8','|S32','f8','f8','f8','f8','|S32','f8','f8','f8')}

refdir='/home/rumbaugh/git/ORELSE/Catalogs/tomczak_catalogs'
reffile_dict={"cl0023":'sg0023+0423_v0.1.9','cl1604':'sc1604_v0.0.3','rxj1757':'nep200_v0.0.4','rxj1821':'nep5281_v0.0.1','rxj1716':'rxj1716+6708_v0.0.7','rxj0910':'cl0910+5422_v0.0.2'}

rfmt=('i8',)
for k in range(0,42):rfmt=rfmt+('f8',)
#for k in range(0,4):rfmt=rfmt+('i8',)
refdict={'names':('ID','z_spec','ra','dec','magaper_B','erraper_B','magaper_V','erraper_V','magaper_Rplus','erraper_Rplus','magaper_Iplus','erraper_Iplus','magaper_r','erraper_r','magaper_i','erraper_i','magaper_z','erraper_z','magaper_J','erraper_J','magaper_K','erraper_K','magcolor_ch1','magcolor_ch1err','magcolor_ch2','magcolor_ch2err','apercorr','weight_B','weight_V','weight_Rplus','weight_Iplus','weight_r','weight_i','weight_z','weight_J','weight_K','weight_ch1','weight_ch2','wmin','star','saturation','badfit','use'),'formats':rfmt}

rfmt=('i8',)
for k in range(0,36):rfmt=rfmt+('f8',)
refdict_1821={'names':('ID','z_spec','ra','dec','magaper_B','erraper_B','magaper_V','erraper_V','magaper_r','erraper_r','magaper_i','erraper_i','magaper_z','erraper_z','magaper_J','erraper_J','magaper_Ks','erraper_Ks','magcolor_ch1','errcolor_ch1','magcolor_ch2','errcolor_ch2','apercorr','weight_B','weight_V','weight_r','weight_i','weight_z','weight_J','weight_Ks','weight_ch1','weight_ch2','wmin','star','saturation','badfit','use'),'formats':rfmt}

rfmt=('i8',)
for k in range(0,33):rfmt=rfmt+('f8',)
refdict0910={'names':('ID','z_spec','ra','dec','magaper_V','erraper_V','magaper_Rc','erraper_Rc','magaper_Iplus','erraper_Iplus','magaper_Zplus','erraper_Zplus','magaper_J','erraper_J','magaper_K','erraper_K','magcolor_ch1','errcolor_ch1','magcolor_ch2','errcolor_ch2','apercorr','weight_V','weight_Rc','weight_Iplus','weight_Zplus','weight_J','weight_K','weight_ch1','weight_ch2','wmin','star','saturation','badfit','use'),'formats':rfmt}
zfmt=('i8',)
for k in range(0,14):zfmt=zfmt+('f8',)
zfmt=zfmt+('i8',)
for k in range(0,4):zfmt=zfmt+('f8',)
pzdict={'names':('id','z_spec','z_a','z_m1','chi_a','z_p','chi_p','z_m2','odds','l68','u68','l95','u95','l99','u99','nfilt','q_z','z_peak','peak_prob','z_mc'),'formats':zfmt}

rffmt=('i8',)
for k in range(0,23):rffmt=rffmt+('f8',)
rfdict={'names':('id','z','DM','restflux_NUV','p16_NUV','p84_NUV','restflux_U','p16_U','p84_U','restflux_B','p16_B','p84_B','restflux_V','p16_V','p84_V','restflux_r','p16_r','p84_r','restflux_J','p16_J','p84_J','restflux_2800','p16_2800','p84_2800'),'formats':rffmt}

rffmt=('i8',)
for k in range(0,16):rffmt=rffmt+('f8',)
rfdict0910={'names':('id','z','DM','restflux_NUV','errflux_NUV','restflux_U','errflux_U','restflux_B','errflux_B','restflux_V','errflux_V','restflux_r','errflux_r','restflux_J','errflux_J','restflux_2800','errflux_2800'),'formats':rffmt}

crcc=np.loadtxt('/home/rumbaugh/cc_out.2.19.16.dat')
D_L=crcc[:,13]*3.086E22
DM=crcc[:,15]
kpc=crcc[:,12]
cc_z=crcc[:,0]

alphas=[1.1,5.1,10.1,20.1,50.1,100.1]

for field in ['rxj0910']:
    refcat='%s/%s/%s.mag.gz'%(refdir,reffile_dict[field],reffile_dict[field])
    if field=='rxj1821':
        cr=np.loadtxt(refcat,dtype=refdict_1821)
    elif field=='rxj0910':
        cr=np.loadtxt(refcat,dtype=refdict0910)
    else:
        cr=np.loadtxt(refcat,dtype=refdict)
    crs=np.loadtxt('%s/%s'%(spec_dict['basepath'],spec_dict[field]['file']),dtype=specloaddict)
    ra_opt,dec_opt=crs['ra'],crs['dec']
    inCH_arr=np.zeros((len(cr['ra']),len(alphas)+1),dtype='i8')
    inCH_arr[:,0]=np.array(cr['ID'],dtype='i8')
        
    CH_ref = np.zeros((len(ra_opt),2))
    CH_ref[:,0],CH_ref[:,1]=ra_opt,dec_opt
    CHull_ref1,edges_ref1=ConcaveHull(CH_ref,alpha1)
    CHull_ref2,edges_ref2=ConcaveHull(CH_ref,alpha2)
    #gCH=CheckPoints(CHull_ref,cr['ra'],cr['dec'])
    #inCH_arr[:,1+ia][gCH]=1
    clf()
    plt.scatter(ra_opt,dec_opt,s=6)
    #x1,x2,y1,y2=np.zeros(np.shape(edges_ref1)[0]),np.zeros(np.shape(edges_ref2)[0]),np.zeros(np.shape(edges_ref1)[0]),np.zeros(np.shape(edges_ref2)[0])
    #for i in range(0,len(edges_ref1)):
    #    x1[i],y1[i]=edges_ref1[i][0,0],edges_ref1[i][0,1]
    #for i in range(0,len(edges_ref2)):
    #    x2[i],y2[i]=edges_ref2[i][0,0],edges_ref2[i][0,1]
    #x1,x2,y1,y2=np.append(x1,x1[0]),np.append(x2,x2[0]),np.append(y1,y1[0]),np.append(y2,y2[0])
    x1,y1=CHull_ref1.exterior.xy
    x2,y2=CHull_ref2.exterior.xy
    plot(x1,y1,color='b',label='alpha=%.1f'%alpha1)
    plot(x2,y2,color='r',label='alpha=%.1f'%alpha2)
    legend()
    savefig('/home/rumbaugh/test.CH.png')
