import numpy as np
import pyfits as py
from ConcaveHull import ConcaveHull,CheckPoints
from shapely.geometry import box as makebox
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/calc_Xray_lums.py')

adamcorrval=-1.3975614258700002

alpha_ref,alphaX = 11.1,1.1
execfile('/home/rumbaugh/set_spec_dict.py')
execfile('/home/rumbaugh/SphDist.py')
targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053","cl1324_north","cl1324_south"])

nh_dict={"rxj1757": 4.08,"cl1604": 1.22,"cl0023": 2.79,"cl1324_north": 1.15,"cl1324_south": 1.16, 'cl1324': 1.155,"rxj1821":5.67, 'rcs0224': 2.86, 'cl0849': 2.73, 'rxj0910': 1.98,'rxj1053': 0.58, 'rxj1221':1.44,'cl1350':1.76,'rxj1716':3.71,'cl1137':1.93}

crRSfit=np.loadtxt('/home/rumbaugh/Chandra/RS_fits.composite_colors.nofit.3.13.16.dat',dtype={'names':('field','y0','m','sig','numsig'),'formats':('|S32','f8','f8','f8','i8')})

mtol=1.
ldate='1.19.16'
optmatchloaddict={'names':('indX','raX','decX','errX','nummatch','raopt1','decopt1','optID1','Popt1','likeopt1','raopt2','decopt2','optID2','Popt2','likeopt2','raopt3','decopt3','optID3','Popt3','likeopt3','probnone'),'formats':('i8','f8','f8','f8','i8','f8','f8','|S32','f8','f8','f8','f8','|S32','f8','f8','f8','f8','|S32','f8','f8','f8')}

refdir='/home/rumbaugh/git/ORELSE/Catalogs/tomczak_catalogs'
reffile_dict={"cl0023":'sg0023+0423_v0.1.9','cl1604':'sc1604_v0.0.3','rxj1757':'nep200_v0.0.4','rxj1821':'nep5281_v0.0.1','rxj1716':'rxj1716+6708_v0.0.7'}

rfmt=('i8',)
for k in range(0,42):rfmt=rfmt+('f8',)
#for k in range(0,4):rfmt=rfmt+('i8',)
refdict={'names':('ID','z_spec','ra','dec','magaper_B','erraper_B','magaper_V','erraper_V','magaper_Rplus','erraper_Rplus','magaper_Iplus','erraper_Iplus','magaper_r','erraper_r','magaper_i','erraper_i','magaper_z','erraper_z','magaper_J','erraper_J','magaper_K','erraper_K','magcolor_ch1','magcolor_ch1err','magcolor_ch2','magcolor_ch2err','apercorr','weight_B','weight_V','weight_Rplus','weight_Iplus','weight_r','weight_i','weight_z','weight_J','weight_K','weight_ch1','weight_ch2','wmin','star','saturation','badfit','use'),'formats':rfmt}

rfmt=('i8',)
for k in range(0,36):rfmt=rfmt+('f8',)
refdict_1821={'names':('ID','z_spec','ra','dec','magaper_B','erraper_B','magaper_V','erraper_V','magaper_r','erraper_r','magaper_i','erraper_i','magaper_z','erraper_z','magaper_J','erraper_J','magaper_Ks','erraper_Ks','magcolor_ch1','errcolor_ch1','magcolor_ch2','errcolor_ch2','apercorr','weight_B','weight_V','weight_r','weight_i','weight_z','weight_J','weight_Ks','weight_ch1','weight_ch2','wmin','star','saturation','badfit','use'),'formats':rfmt}

zfmt=('i8',)
for k in range(0,14):zfmt=zfmt+('f8',)
zfmt=zfmt+('i8',)
for k in range(0,4):zfmt=zfmt+('f8',)
pzdict={'names':('id','z_spec','z_a','z_m1','chi_a','z_p','chi_p','z_m2','odds','l68','u68','l95','u95','l99','u99','nfilt','q_z','z_peak','peak_prob','z_mc'),'formats':zfmt}

rffmt=('i8',)
for k in range(0,23):rffmt=rffmt+('f8',)
rfdict={'names':('id','z','DM','restflux_NUV','p16_NUV','p84_NUV','restflux_U','p16_U','p84_U','restflux_B','p16_B','p84_B','restflux_V','p16_V','p84_V','restflux_r','p16_r','p84_r','restflux_J','p16_J','p84_J','restflux_2800','p16_2800','p84_2800'),'formats':rffmt}

FILEl=open('/home/rumbaugh/Chandra/fluxes_newphotoz_adam.4.27.16.dat','w')
FILEl.write('# ID RA Dec z_peak nh flux_soft flux_hard flux_full\n')

crcc=np.loadtxt('/home/rumbaugh/cc_out.2.19.16.dat')
D_L=crcc[:,13]*3.086E22
DM=crcc[:,15]
kpc=crcc[:,12]
cc_z=crcc[:,0]

carr=np.array(['blue','green','orange','red','magenta','brown','gray','cyan'])
marr=np.array(['o','s','x','+','*'])

crRS = np.loadtxt('/home/rumbaugh/Chandra/RS_offsets.AGN.3.6.16.dat',dtype={'names':('field','number','RA','Dec','RSoffset','magR','magI','magZ','SCmagRed','SCmagBlue'),'formats':('|S24','i8','f8','f8','f8','f8','f8','f8','f8','f8')})

crRS_ACS = np.loadtxt('/home/rumbaugh/Chandra/RS_offsets.cl1604_ACS.3.6.16.dat',dtype={'names':('field','number','RA','Dec','RSoffset','F606W','F814W'),'formats':('|S24','i8','f8','f8','f8','f8','f8')})


plottargets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053"])#,"cl1324_north","cl1324_south"])

indict={'names':('field','number','RA','Dec','lum_soft','lum_hard','lum_full','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit'),'formats':('|S32','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S32','|S32')}

crn=np.loadtxt('/home/rumbaugh/X-ray_lum_cat.4.17.16.dat',dtype=indict)
g1324=np.where((crn['field']=='cl1324_north')|(crn['field']=='cl1324_south'))[0]
crn['field'][g1324]='cl1324'

gAGN=np.zeros(len(crRS['RA']-2),dtype='i8')
gnot1604=np.where(crRS['field']!='cl1604')[0]
RSO=np.zeros(len(gAGN))

fieldmarkers,fieldcolors={},{}

plt.figure(2)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
for field,jf in zip(plottargets,np.arange(len(plottargets))):
    gf = np.where(crn['field'][gAGN]==field)[0]
    #plt.scatter(-crRS['RSoffset'][gf],np.log10(crn['lum_full'][gAGN][gf]),color=carr[jf%len(carr)],marker=marr[jf%len(marr)],label=field)
    plt.scatter(RSO[gf],np.log10(crn['lum_full'][gAGN][gf]),color=carr[jf%len(carr)],marker=marr[jf%len(marr)],label=field,s=64)
    fieldmarkers[field],fieldcolors[field]=marr[jf%len(marr)],carr[jf%len(carr)]
plt.xlabel('RS Offset')
plt.ylabel('X-ray Luminosity')
plt.axhline(43.3,lw=2,ls='--',color='k')
plt.axvline(-1,lw=2,ls='--',color='k')
plt.axvline(-3,lw=2,ls='--',color='k')
#plt.axvline(1,lw=2,ls='--',color='k')
plt.legend(loc='lower left')
plt.xlim(-9,1.05)
plt.ylim(42,44.5)


for i in range(0,len(crRS['RA'][gnot1604])):
    tmpdist=np.sqrt((crRS['RA'][gnot1604][i]-crn['RA'])**2+(crRS['Dec'][gnot1604][i]-crn['Dec'])**2)
    gAGN[i]=np.argsort(tmpdist)[0]
    if tmpdist[gAGN[i]]>1./3600: print 'Too big! %f'%(tmpdist[gAGN[i]]*3600)
    RSO[i]=-crRS['RSoffset'][gnot1604][i]
for i in range(0,len(crRS_ACS['RA'])):
    tmpdist=np.sqrt((crRS_ACS['RA'][i]-crn['RA'])**2+(crRS_ACS['Dec'][i]-crn['Dec'])**2)
    gAGN[i+len(gnot1604)]=np.argsort(tmpdist)[0]
    if tmpdist[gAGN[i+len(gnot1604)]]>1./3600: print 'Too big! %f'%(tmpdist[gAGN[i+len(gnot1604)]]*3600)
    RSO[i+len(gnot1604)]=-crRS_ACS['RSoffset'][i]

for field in reffile_dict.keys():
    cram=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s.adammatch.4.23.16.dat'%(field,field,field),dtype={'names':('ID_adam','RA_phot','Dec_phot','z_peak','flag','ID_spec','RA_spec','Dec_spec','z_spec','z_spec_adam','Q','ID_xray','RA_xray','Dec_xray','nummatch','ID_xray_adam','RA_xray_adam','Dec_xray_adam','nummatch_adam','mRFU','mRFB'),'formats':('|S24','f8','f8','f8','f8','|S24','f8','f8','f8','f8','i8','|S24','f8','f8','i8','|S24','f8','f8','i8','f8','f8')})
    matchcat='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_optmatch_comb.%s.dat'%(field,field,field,ldate)
    if field=='cl1604': 
        ACSmatchcat='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_optmatch_ACS_comb.%s.dat'%(field,field,field,ldate)
        crmACS=np.loadtxt(matchcat,dtype=optmatchloaddict)
        ACSnumX=len(crmACS['indX'])
        ACSmras,ACSmdecs=crmACS['raopt1'],crmACS['decopt1']
        ACSnummatch=crmACS['nummatch']
        tmpcrm=np.loadtxt(matchcat,dtype=optmatchloaddict)
        crm=np.copy(crmACS)
        crm[((ACSnummatch==0)&(tmpcrm['nummatch']>0))]=tmpcrm[((ACSnummatch==0)&(tmpcrm['nummatch']>0))]
        usedACS=np.ones(ACSnumX,dtype='i8')
        usedACS[((ACSnummatch==0)&(tmpcrm['nummatch']>0))]=0
    else:
        crm=np.loadtxt(matchcat,dtype=optmatchloaddict)
    crs=np.loadtxt('%s/%s'%(spec_dict['basepath'],spec_dict[field]['file']),dtype=specloaddict)
    ra_opt,dec_opt=crs['ra'],crs['dec']
    gq=np.where(crs['Q']>2.5)[0]
    fz0,fzl,fzu=spec_dict[field]['z'][0],spec_dict[field]['z'][1],spec_dict[field]['z'][2]
    refcat='%s/%s/%s.mag.gz'%(refdir,reffile_dict[field],reffile_dict[field])
    if field=='rxj1821':
        cr=np.loadtxt(refcat,dtype=refdict_1821)
    else:
        cr=np.loadtxt(refcat,dtype=refdict)
    magB=cr['magaper_B']+cr['apercorr']

    pzcat='%s/%s/%s.zout.gz'%(refdir,reffile_dict[field],reffile_dict[field])
    crpz=np.loadtxt(pzcat,dtype=pzdict)
    rfcat='%s/%s/%s.restframe.gz'%(refdir,reffile_dict[field],reffile_dict[field])
    crrf=np.loadtxt(rfcat,dtype=rfdict)

    RFU,RFB=crrf['restflux_U'],crrf['restflux_B']
    mRFU,mRFB=cram['mRFU'],cram['mRFB']


    numsig=3
    gf=np.where(crRSfit['field']==field)[0][0]
    y0,m,sig=crRSfit['y0'][gf],crRSfit['m'][gf],crRSfit['sig'][gf]
    width=2*numsig*sig
    rso=(y0+m*(mRFB+adamcorrval)-(mRFU-mRFB))/(0.5*width)

    crCH=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s.photz_inspeccov.4.23.16.dat'%(field,field,field),dtype='i8')
    inCH=crCH[:,4]

    gall=np.where((crpz['z_peak']>=fzl)&(crpz['z_peak']<=fzu)&(cr['use']==1)&(mRFB<-20.9)&(mRFB>-80))[0]
    gnew0=np.where((crpz['z_peak']>=fzl)&(crpz['z_peak']<=fzu)&(cr['use']==1)&(cram['Q']!=-1)&(cram['Q']<2.5)&(mRFB<-20.9)&(mRFB>-80))[0]
    gCH=np.where(inCH[gall]>=1)[0]
    gnew=np.where(inCH[gnew0]>=1)[0]
    gxray=np.where(cram['nummatch_adam'][gnew0][gnew]>0)[0]
    print field,len(gall),len(gnew0),len(gnew),len(gCH)
    gRS,gGV,gBC=np.where(-rso[gnew0][gnew]>=-1)[0],np.where((-rso[gnew0][gnew]<-1)&(-rso[gnew0][gnew]>=-3))[0],np.where(-rso[gnew0][gnew]<-3)[0]
    gRSx,gGVx,gBCx=np.where(-rso[gnew0][gnew][gxray]>=-1)[0],np.where((-rso[gnew0][gnew][gxray]<-1)&(-rso[gnew0][gnew][gxray]>=-3))[0],np.where(-rso[gnew0][gnew][gxray]<-3)[0]
    print 'RS: %i  GV: %i  BC: %i'%(len(gRS),len(gGV),len(gBC))
    print 'RS: %i  GV: %i  BC: %i'%(len(gRSx),len(gGVx),len(gBCx))

    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.scatter(cr['ra'],cr['dec'],color='k',s=2)
    plt.scatter(crs['ra'][gq],crs['dec'][gq],color='b',s=6)
    plt.scatter(cr['ra'][gall],cr['dec'][gall],color='green',s=16,marker='s')
    plt.scatter(cr['ra'][gall][gCH],cr['dec'][gall][gCH],color='orange',s=16,marker='s')
    plt.scatter(cr['ra'][gnew0][gnew],cr['dec'][gnew0][gnew],color='cyan',lw=2,s=22,marker='x')
    plt.scatter(cr['ra'][gnew0][gnew][gxray],cr['dec'][gnew0][gnew][gxray],color='r',lw=2,s=24,marker='x')
    plt.xlabel('RA')
    plt.ylabel('Dec')
    plt.legend()
    plt.savefig('/home/rumbaugh/Chandra/plots/adam_spec_cov_test.%s.4.25.16.png'%field)

    #mRFB,mRFU=mRFB+adamcorrval,mRFU+adamcorrval
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.scatter(mRFB[gall],mRFU[gall]-mRFB[gall])
    plt.scatter(mRFB[gall][gCH],mRFU[gall][gCH]-mRFB[gall][gCH],color='green')
    plt.scatter(mRFB[gnew0][gnew],mRFU[gnew0][gnew]-mRFB[gnew0][gnew],marker='s',color='magenta')
    plt.scatter(mRFB[gnew0][gnew][gxray],mRFU[gnew0][gnew][gxray]-mRFB[gnew0][gnew][gxray],marker='x',color='r',s=24)
    xlim=plt.xlim()
    ylim=plt.ylim()
    xdummy=np.linspace(xlim[0],xlim[1],1000)
    plt.plot(xdummy,y0+m*(xdummy+adamcorrval)+0.5*width,color='r',lw=2,ls='dashed')
    plt.plot(xdummy,y0+m*(xdummy+adamcorrval)-0.5*width,color='r',lw=2,ls='dashed')
    plt.plot(xdummy,y0+m*(xdummy+adamcorrval)-1.5*width,color='r',lw=2,ls='dashed')
    plt.xlim(-26,-20.5)
    plt.ylim(ylim)
    plt.xlabel('M_B (Restframe)')
    plt.ylabel('M_U-M_B (Restframe)')
    plt.savefig('/home/rumbaugh/Chandra/plots/test_CMD.adam_RF_colors.%s.4.25.16.png'%field)

    crxp=py.open('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/SRCv1/%s_srclist_v1.fits'%(field,field,field))
    pdata=crxp[1].data

    fluxes=np.zeros((len(gxray),3))
    fluxes[:,0],fluxes[:,1],fluxes[:,2]=pdata['Soft_flux'][np.array(cram['ID_xray_adam'][gnew0][gnew][gxray],dtype='i8')],pdata['Hard_flux'][np.array(cram['ID_xray_adam'][gnew0][gnew][gxray],dtype='i8')],pdata['Full_flux'][np.array(cram['ID_xray_adam'][gnew0][gnew][gxray],dtype='i8')],
    calc_dict={'z': crpz['z_peak'][gnew0][gnew][gxray], 'nh': np.ones(len(gxray))*nh_dict[field], 'bands':{ 'names': np.array(['soft','hard','full']), 'kev': np.array([[0.5,2.0],[2.0,7.0],[0.5,7.0]])}, 'flux':fluxes}
    for iflx in range(0,len(gxray)):
        FILEl.write('%i %9.5f %9.5f %f %f %f %f %f\n'%(cr['ID'][gnew0][gnew][gxray][iflx],crpz['z_peak'][gnew0][gnew][gxray], nh_dict[field],fluxes[iflx][0],fluxes[iflx][1],fluxes[iflx][2]))
    #plt.figure(2)
    #plt.scatter(rso[gnew0][gnew][gxray],lums[:,2],marker=fieldmarkers[field],color=fieldcolors[field],s=100,lw=2)
#plt.figure(2)    
#plt.savefig('/home/rumbaugh/Chandra/plots/RSoffset_vs_Lum.4.26.16.png')
FILEl.close()
