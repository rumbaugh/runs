import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf
execfile('/home/rumbaugh/SphDist.py')
execfile('/home/rumbaugh/cosmocalc.py')
execfile('/home/rumbaugh/KStest.py')
execfile("/home/rumbaugh/makeCMD.py")
execfile("/home/rumbaugh/set_spec_dict.py")
execfile('/home/rumbaugh/setup_adam_cats.py')
psfpdf=bpdf.PdfPages('/home/rumbaugh/Chandra/plots/CMDs_field.6.27.16.pdf')

target_dir={"RCS0224":"rcs0224","SC0849":"cl0849","SC0910":"rxj0910","RXJ1221":"rxj1221","Cl1350":"cl1350","NEP200":"rxj1757","SG0023":"cl0023","SC1324":'cl1324',"NEP5281":"rxj1821","Cl1137":"cl1137","RXJ1716":"rxj1716","RXJ1053":"rxj1053","SC1604":"cl1604","RXJ1821":"rxj1821","RXJ1757":"rxj1757"}
targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","rxj1716","rxj1053"])

adamcorrval=-1.3975614258700002

ierrmax=99999999

zarr=np.linspace(0.1,2,1000)
ARed,ABlue=0.424*(1-1.794*(zarr-0.628)),0.45*(1-1.824*(zarr-0.679))
BRed,BBlue=0.576*(1.794*(zarr-0.628)),0.55*(1.824*(zarr-0.679))
ARed[zarr>1/1.794+0.628]=0
BRed[zarr<0.628]=0
ABlue[zarr>1/1.824+0.679]=0
BBlue[zarr<0.679]=0
param_dict={'ARed':ARed,'ABlue':ABlue,'BRed':BRed,'BBlue':BBlue,'z':zarr}

crcc=np.loadtxt('/home/rumbaugh/cc_out.2.19.16.dat')
D_L=crcc[:,13]*3.086E22
kpc=crcc[:,12]
DM=crcc[:,15]
cc_z=crcc[:,0]
#gdls=np.zeros(len(crx['redshift']),dtype='i8')
#for igdl in range(0,len(gdls)):
#    gdl=np.argsort(np.abs(crx['redshift'][igdl]-cc_z))[0]
#    gdls[igdl]=gdl

full_zlb,full_zub=0.65,1.28

mblue_all,mred_all,mblue_lowz,mred_lowz,mblue_midz,mred_midz,mblue_highz,mred_highz=np.zeros(0),np.zeros(0),np.zeros(0),np.zeros(0),np.zeros(0),np.zeros(0),np.zeros(0),np.zeros(0)

for field in targets:
    pcat = '/home/rumbaugh/Chandra/photcats/%s_rizdata.corr.gz'%field
    scat='%s/%s'%(spec_dict['basepath'],spec_dict[field]['file'])
    refdict={'names':('ID','dum1','dum2','ra','dec','magR','dmagR','magI','dmagI','magZ','dmagZ'),'formats':('|S64','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')}
    useoldid=True
    if field=='cl1604':
        pcat = '/home/rumbaugh/git/ORELSE/Catalogs/ACS/Cl1604/merged.F606W_F814W_deep.all.coll.hdat'
        crp=np.loadtxt(pcat,dtype={'names':('ra','dec','magR','magI','dmagR','dmagI'),'formats':('f8','f8','f8','f8','f8','f8')})
        crs=np.loadtxt(scat,dtype=ACSspecloaddict)
    else:
        crs=np.loadtxt(scat,dtype=specloaddict)
        crp=np.loadtxt(pcat,dtype=refdict)
    r,i,redshift,q=crs['magR'],crs['magI'],crs['z'],crs['Q']
    rerr,ierr,zerr=np.zeros(len(r)),np.zeros(len(i)),np.zeros(len(i))
    for ipr in range(0,np.shape(crs)[0]):
        gp=np.where(((np.abs(crs['ra'][ipr]-crp['ra'])<0.2/3600)&(np.abs(crs['dec'][ipr]-crp['dec'])<0.2/3600)&(np.abs(r[ipr]-crp['magR'])<0.1)&(np.abs(i[ipr]-crp['magI'])<0.1)))[0]
        if ((len(gp)==0)|(field=='cl1604')):
            rerr[ipr],ierr[ipr]=99,99
        else:
            gp=gp[0]
            rerr[ipr],ierr[ipr],zerr[ipr]=crp['dmagR'][gp],crp['dmagI'][gp],crp['dmagZ'][gp]
    rerrorig,ierrorig,zerrorig=np.copy(rerr),np.copy(ierr),np.copy(zerr)
    r,i,rerr,ierr=calc_param_mags(r,i,crs['magZ'],rerr,ierr,zerr,redshift,param_dict=param_dict)
    rerrinit,ierrinit=np.copy(rerr),np.copy(ierr)    
    r,i,redshift,rerr,ierr,gCMD=r[q>2.5],i[q>2.5],redshift[q>2.5],rerr[q>2.5],ierr[q>2.5],np.arange(len(q))[q>2.5]
    g40=np.where((r<40)&(i<40)&(crs['magZ'][q>2.5]<40))[0]
    r,i,rerr,ierr,redshift,gCMD=r[g40],i[g40],rerr[g40],ierr[g40],redshift[g40],gCMD[g40]      
    zlb,zub=spec_dict[field]['z'][1],spec_dict[field]['z'][2]
    r,i,rerr,ierr,redshift,gCMD=r[(((redshift<zlb)|(redshift>zub))&(redshift>full_zlb)&(redshift<full_zub))],i[(((redshift<zlb)|(redshift>zub))&(redshift>full_zlb)&(redshift<full_zub))],rerr[(((redshift<zlb)|(redshift>zub))&(redshift>full_zlb)&(redshift<full_zub))],ierr[(((redshift<zlb)|(redshift>zub))&(redshift>full_zlb)&(redshift<full_zub))],redshift[(((redshift<zlb)|(redshift>zub))&(redshift>full_zlb)&(redshift<full_zub))],gCMD[(((redshift<zlb)|(redshift>zub))&(redshift>full_zlb)&(redshift<full_zub))]
    r,i,rerr,ierr,redshift,gCMD=r[ierr<ierrmax],i[ierr<ierrmax],rerr[ierr<ierrmax],ierr[ierr<ierrmax],redshift[ierr<ierrmax],gCMD[ierr<ierrmax]
    gdls=np.zeros(len(redshift),dtype='i8')
    for igdl in range(0,len(gdls)):
        gdl=np.argsort(np.abs(redshift[igdl]-cc_z))[0]
        gdls[igdl]=gdl
    r,i=r-DM[gdls]-2.5*np.log10(1+redshift),i-DM[gdls]-2.5*np.log10(1+redshift)
    
    r,i=r-adamcorrval,i-adamcorrval
    gcut=np.where(i<=-20.9)[0]
    mblue_all,mred_all=np.append(mblue_all,r),np.append(mred_all,i)
    mblue_lowz,mred_lowz=np.append(mblue_lowz,r[redshift<0.8]),np.append(mred_lowz,i[redshift<0.8])
    mblue_midz,mred_midz=np.append(mblue_midz,r[((redshift<0.96)&(redshift>=0.8))]),np.append(mred_midz,i[((redshift<0.96)&(redshift>=0.8))])
    mblue_highz,mred_highz=np.append(mblue_highz,r[redshift>=0.96]),np.append(mred_highz,i[redshift>=0.96])

print len(mblue_lowz),len(mblue_midz),len(mblue_highz)
