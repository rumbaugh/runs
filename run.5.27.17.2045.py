import numpy as np
import matplotlib.pyplot as plt
execfile("/home/rumbaugh/makeCMD.py")
execfile("/home/rumbaugh/set_spec_dict.py")
execfile('/home/rumbaugh/setup_adam_cats.py')
cmloaddict={'names':('field','number','RA','Dec','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','specID','mask','slit','bcnts_soft','bcnts_hard','bcnts_full','sigs','sigh','sigf'),'formats':('|S24','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S48','|S24','|S24','f8','f8','f8','f8','f8','f8')}

adamcorrval=-1.3975614258700002
ierrmax=99999999
numsig=3
crRS=np.loadtxt('/home/rumbaugh/final_RS_values_supercolors.notes',dtype={'names':('field','y0','m','sig'),'formats':('|S32','f8','f8','f8')})
crRS_ACS=np.loadtxt('/home/rumbaugh/Chandra/RS_fits.cl1604_ACS.nofit.3.6.16.dat',dtype={'names':('field','y0','m','sig','numsig'),'formats':('|S32','f8','f8','f8','i8')})

target_dir={"RCS0224":"rcs0224","SC0849":"cl0849","SC0910":"rxj0910","RXJ1221":"rxj1221","Cl1350":"cl1350","NEP200":"rxj1757","SG0023":"cl0023","SC1324":'cl1324',"NEP5281":"rxj1821","Cl1137":"cl1137","RXJ1716":"rxj1716","RXJ1053":"rxj1053","SC1604":"cl1604","RXJ1821":"rxj1821","RXJ1757":"rxj1757"}

for i in range(0,len(crRS['field'])): crRS['field'][i]=target_dir[crRS['field'][i]]

cmcat='/home/rumbaugh/combined_match_catalog.5.9.16.dat'
crcm=np.loadtxt(cmcat,cmloaddict)
testfield=np.zeros(np.shape(crcm)[0],dtype='|S24')
for i in range(0,len(testfield)):
    testfield[i]=crcm['field'][i].lower()
testfield[((testfield=='cl1324_south')|(testfield=='cl1324_north'))]='cl1324'
        
targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053"])

zlist=np.zeros(len(targets))
for i in range(0,len(targets)): zlist[i]=spec_dict[targets[i]]['z'][0]
zarr=np.linspace(0.1,2,1000)
ARed,ABlue=0.424*(1-1.794*(zarr-0.628)),0.45*(1-1.824*(zarr-0.679))
BRed,BBlue=0.576*(1.794*(zarr-0.628)),0.55*(1.824*(zarr-0.679))
ARed[zarr>1/1.794+0.628]=0
BRed[zarr<0.628]=0
ABlue[zarr>1/1.824+0.679]=0
BBlue[zarr<0.679]=0
param_dict={'ARed':ARed,'ABlue':ABlue,'BRed':BRed,'BBlue':BBlue,'z':zarr}

outcr=np.zeros((0,),dtype={'names':('field','ra','dec','redshift','q','Mred','Mblue','Mrederr','Mblueerr','rso'),'formats':('|S16','f8','f8','f8','i8','f8','f8','f8','f8','f8')})

for field in targets[np.argsort(zlist)]:
    pcat = '/home/rumbaugh/Chandra/photcats/%s_rizdata.corr.gz'%field
    scat='%s/%s'%(spec_dict['basepath'],spec_dict[field]['file'])
    refdict={'names':('ID','dum1','dum2','ra','dec','magR','dmagR','magI','dmagI','magZ','dmagZ'),'formats':('|S64','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')}
    useoldid=True
    if field=='cl1604':
        pcat = '/home/rumbaugh/git/ORELSE/Catalogs/ACS/Cl1604/merged.F606W_F814W_deep.all.coll.hdat'
        crp=np.loadtxt(pcat,dtype={'names':('ra','dec','magR','magI','dmagR','dmagI'),'formats':('f8','f8','f8','f8','f8','f8')})
        crs=np.loadtxt(scat,dtype=ACSspecloaddict,usecols=ACStc)
    else:
        crs=np.loadtxt(scat,dtype=specloaddict,usecols=tc)
        crp=np.loadtxt(pcat,dtype=refdict,usecols=ptc)
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
    r,i,rerr,ierr,redshift,gCMD=r[((redshift>spec_dict[field]['z'][1])&(redshift<spec_dict[field]['z'][2]))],i[((redshift>spec_dict[field]['z'][1])&(redshift<spec_dict[field]['z'][2]))],rerr[((redshift>spec_dict[field]['z'][1])&(redshift<spec_dict[field]['z'][2]))],ierr[((redshift>spec_dict[field]['z'][1])&(redshift<spec_dict[field]['z'][2]))],redshift[((redshift>spec_dict[field]['z'][1])&(redshift<spec_dict[field]['z'][2]))],gCMD[((redshift>spec_dict[field]['z'][1])&(redshift<spec_dict[field]['z'][2]))]
    r,i,rerr,ierr,redshift,gCMD=r[ierr<ierrmax],i[ierr<ierrmax],rerr[ierr<ierrmax],ierr[ierr<ierrmax],redshift[ierr<ierrmax],gCMD[ierr<ierrmax]
    crcc=np.loadtxt('/home/rumbaugh/cc_out.2.19.16.dat')
    D_L=crcc[:,13]*3.086E22
    DM=crcc[:,15]
    cc_z=crcc[:,0]
    gdls=np.zeros(len(redshift),dtype='i8')
    for igdl in range(0,len(gdls)):
        gdl=np.argsort(np.abs(redshift[igdl]-cc_z))[0]
        gdls[igdl]=gdl
    r,i=r-DM[gdls]-2.5*np.log10(1+redshift),i-DM[gdls]-2.5*np.log10(1+redshift)
    
    r,i=r-adamcorrval,i-adamcorrval
    gcut=np.where(i<=-20.9)[0]
    gf=np.where(field==testfield)[0]

    crcc=np.loadtxt('/home/rumbaugh/cc_out.2.19.16.dat')
    D_L=crcc[:,13]*3.086E22
    DM=crcc[:,15]
    cc_z=crcc[:,0]
    ras,decs=crs['ra'][gCMD],crs['dec'][gCMD]
    if field=='cl1604':
        r,i=crs['F606W'][gCMD],crs['F814W'][gCMD]
        ras,decs=crs['ACS_RA'][gCMD],crs['ACS_DEC'][gCMD]

    gf=np.where(crRS['field']==field)[0][0]
    y0,m,sig=crRS['y0'][gf],crRS['m'][gf],crRS['sig'][gf]
    if field=='cl1604':y0,m,sig=crRS_ACS['y0']+0,crRS_ACS['m']+0,crRS_ACS['sig']+0
    width=2*numsig*sig

    rso_all=(y0+m*i-(r-i))/(0.5*width)

    outcrT=np.zeros((len(rso_all),),dtype={'names':('field','ra','dec','redshift','q','Mred','Mblue','Mrederr','Mblueerr','rso'),'formats':('|S16','f8','f8','f8','i8','f8','f8','f8','f8','f8')})
    outcrT['field'],outcrT['ra'],outcrT['dec'],outcrT['redshift'],outcrT['q'],outcrT['Mred'],outcrT['Mblue'],outcrT['Mrederr'],outcrT['Mblueerr'],outcrT['rso']=field,ras,decs,redshift,q[gCMD],r,i,rerr,ierr,rso_all
    outcr=np.append(outcr,outcrT)
np.savetxt('/home/rumbaugh/Chandra/info.all_members.dat',outcr,header='field ra dec redshift q Mred Mblue Mrederr Mblueerr rso',fmt='%16s %f %f %f %2i %f %f %f %f %f')
