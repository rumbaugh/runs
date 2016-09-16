import numpy as np
import pyfits as py
from ConcaveHull import ConcaveHull,CheckPoints
from shapely.geometry import box as makebox
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/setup_adam_cats.py')

adamcorrval=-1.3975614258700002
numsig=3

alpha_ref,alphaX = 11.1,1.1
execfile('/home/rumbaugh/set_spec_dict.py')
execfile('/home/rumbaugh/SphDist.py')
execfile('/home/rumbaugh/setup_adam_cats.py')
targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053","cl1324_north","cl1324_south"])

nh_dict={"rxj1757": 4.08,"cl1604": 1.22,"cl0023": 2.79,"cl1324_north": 1.15,"cl1324_south": 1.16, 'cl1324': 1.155,"rxj1821":5.67, 'rcs0224': 2.86, 'cl0849': 2.73, 'rxj0910': 1.98,'rxj1053': 0.58, 'rxj1221':1.44,'cl1350':1.76,'rxj1716':3.71,'cl1137':1.93}


crRSfit=np.loadtxt('/home/rumbaugh/final_RS_values_supercolors.notes',dtype={'names':('field','y0','m','sig'),'formats':('|S32','f8','f8','f8')})

target_dir={"RCS0224":"rcs0224","SC0849":"cl0849","SC0910":"rxj0910","RXJ1221":"rxj1221","Cl1350":"cl1350","NEP200":"rxj1757","SG0023":"cl0023","SC1324":'cl1324',"NEP5281":"rxj1821","Cl1137":"cl1137","RXJ1716":"rxj1716","RXJ1053":"rxj1053","SC1604":"cl1604","RXJ1821":"rxj1821","RXJ1757":"rxj1757"}

for i in range(0,len(crRSfit['field'])): crRSfit['field'][i]=target_dir[crRSfit['field'][i]]

mtol=1.
ldate='1.19.16'
optmatchloaddict={'names':('indX','raX','decX','errX','nummatch','raopt1','decopt1','optID1','Popt1','likeopt1','raopt2','decopt2','optID2','Popt2','likeopt2','raopt3','decopt3','optID3','Popt3','likeopt3','probnone'),'formats':('i8','f8','f8','f8','i8','f8','f8','|S32','f8','f8','f8','f8','|S32','f8','f8','f8','f8','|S32','f8','f8','f8')}

crcc=np.loadtxt('/home/rumbaugh/cc_out.2.19.16.dat')
D_L=crcc[:,13]*3.086E22
DM=crcc[:,15]
kpc=crcc[:,12]
cc_z=crcc[:,0]

carr=np.array(['blue','green','orange','red','magenta','brown','gray','cyan'])
marr=np.array(['o','s','x','+','*'])

crRS = np.loadtxt('/home/rumbaugh/Chandra/RS_offsets.AGN.6.7.16.dat',dtype={'names':('field','number','RA','Dec','RSoffset','magR','magI','magZ','SCmagRed','SCmagBlue'),'formats':('|S24','i8','f8','f8','f8','f8','f8','f8','f8','f8')})

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


crl=np.loadtxt('/home/rumbaugh/Chandra/lums_newphotoz_adam.1sig.7.8.16.dat',dtype={'names':('field','ID','RA','Dec','z_peak','nh','lum_soft','lum_hard','lum_full','P_inclus'),'formats':('|S24','i8','f8','f8','f8','f8','f8','f8','f8','f8')})

newxray={x:0 for x in reffile_dict.keys()}
FILE=open('/home/rumbaugh/Chandra/Pz_comp_chk.7.27.16.dat','w')
FILE.write('# field RSO LumX P\n')
for i in range(0,len(crl['ID'])):
    field=crl['field'][i]
    cram=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s.adammatch.5.5.16.dat'%(field,field,field),dtype={'names':('ID_adam','RA_phot','Dec_phot','z_peak','flag','ID_spec','RA_spec','Dec_spec','z_spec','z_spec_adam','Q','ID_xray','RA_xray','Dec_xray','nummatch','ID_xray_adam','RA_xray_adam','Dec_xray_adam','nummatch_adam','mRFU','mRFB'),'formats':('|S24','f8','f8','f8','f8','|S24','f8','f8','f8','f8','i8','|S24','f8','f8','i8','|S24','f8','f8','i8','f8','f8')})
    rfcat='%s/%s/%s.restframe.gz'%(refdir,reffile_dict[field],reffile_dict[field])
    if field=='rxj0910':
        crrf=np.loadtxt(rfcat,dtype=rfdict0910)
    else:
        crrf=np.loadtxt(rfcat,dtype=rfdict)
    RFU,RFB=crrf['restflux_U'],crrf['restflux_B']
    gID=np.where(crl['ID'][i]==np.array(cram['ID_adam'],dtype='i8'))[0]
    #mRFU,mRFB=cram['mRFU'][crl['ID'][i]],cram['mRFB'][crl['ID'][i]]
    mRFU,mRFB=cram['mRFU'][gID],cram['mRFB'][gID]
    gf=np.where(crRSfit['field']==field)[0][0]
    y0,m,sig=crRSfit['y0'][gf],crRSfit['m'][gf],crRSfit['sig'][gf]
    width=2*numsig*sig
    rso=(y0+m*(mRFB+adamcorrval)-(mRFU-mRFB))/(0.5*width)
    if crl['P_inclus'][i]>0.05:
        plt.scatter(-rso,[np.log10(crl['lum_full'][i])],marker=fieldmarkers[field],color=fieldcolors[field],s=80,lw=4,alpha=2*crl['P_inclus'][i])
        plt.scatter(-rso,[np.log10(crl['lum_full'][i])],marker='s',edgecolor='k',facecolor='None',s=150,lw=2)
        newxray[field]+=crl['P_inclus'][i]
    print '%s %f %f P=%f'%(field,rso,np.log10(crl['lum_full'][i]),crl['P_inclus'][i])
    FILE.write('%s %f %f %f\n'%(field,rso,np.log10(crl['lum_full'][i]),crl['P_inclus'][i]))
FILE.close()
plt.savefig('/home/rumbaugh/Chandra/plots/RSoffset_vs_Lum.7.26.16.png')
print newxray
