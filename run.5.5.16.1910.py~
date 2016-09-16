import numpy as np
import pyfits as py
from ConcaveHull import ConcaveHull,CheckPoints
from shapely.geometry import box as makebox
import matplotlib.pyplot as plt

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


crl=np.loadtxt('/home/rumbaugh/Chandra/lums_newphotoz_adam.4.27.16.dat',dtype={'names':('field','ID','RA','Dec','z_peak','nh','lum_soft','lum_hard','lum_full'),'formats':('|S24','i8','f8','f8','f8','f8','f8','f8','f8')})

for i in range(0,len(crl['ID'])):
    field=crl['field'][i]
    cram=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s.adammatch.4.23.16.dat'%(field,field,field),dtype={'names':('ID_adam','RA_phot','Dec_phot','z_peak','flag','ID_spec','RA_spec','Dec_spec','z_spec','z_spec_adam','Q','ID_xray','RA_xray','Dec_xray','nummatch','ID_xray_adam','RA_xray_adam','Dec_xray_adam','nummatch_adam','mRFU','mRFB'),'formats':('|S24','f8','f8','f8','f8','|S24','f8','f8','f8','f8','i8','|S24','f8','f8','i8','|S24','f8','f8','i8','f8','f8')})
    rfcat='%s/%s/%s.restframe.gz'%(refdir,reffile_dict[field],reffile_dict[field])
    crrf=np.loadtxt(rfcat,dtype=rfdict)
    RFU,RFB=crrf['restflux_U'],crrf['restflux_B']
    gID=np.where(crl['ID'][i]==cram['ID_adam'])[0]
    #mRFU,mRFB=cram['mRFU'][crl['ID'][i]],cram['mRFB'][crl['ID'][i]]
    mRFU,mRFB=cram['mRFU'][gID],cram['mRFB'][gID]
    gf=np.where(crRSfit['field']==field)[0][0]
    y0,m,sig=crRSfit['y0'][gf],crRSfit['m'][gf],crRSfit['sig'][gf]
    width=2*numsig*sig
    rso=(y0+m*(mRFB+adamcorrval)-(mRFU-mRFB))/(0.5*width)
    plt.scatter(-rso,np.log10(crl['lum_full'][i]),marker=fieldmarkers[field],color=fieldcolors[field],s=64,lw=2)
    plt.scatter(-rso,np.log10(crl['lum_full'][i]),marker='s',edgecolor='k',facecolor='None',s=120,lw=2)
    print '%s %f %f'%(field,rso,np.log10(crl['lum_full'][i]))
plt.savefig('/home/rumbaugh/Chandra/plots/RSoffset_vs_Lum.4.26.16.png')
