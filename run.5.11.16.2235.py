import numpy as np
import pyfits as py
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/calc_Xray_lums.py')
execfile('/home/rumbaugh/setup_adam_cats.py')

adamcorrval=-1.3975614258700002

c=300000.

FILE=open('/home/rumbaugh/Chandra/Blue_fracs.w_photz.5.11.16.dat','w')
FILE.write('# field BF numgal BF_cut numgal_cut BF_photz numgal_photz\n')

crbf=np.loadtxt('/home/rumbaugh/Chandra/Blue_fracs.5.11.16.dat',dtype={'names':('field','BF','num','BF_cut','num_cut'),'formats':('|S24','f8','f8','f8','f8')})
crcc=np.loadtxt('/home/rumbaugh/cc_out.2.19.16.dat')
D_L=crcc[:,13]*3.086E22
DM=crcc[:,15]
kpc=crcc[:,12]
cc_z=crcc[:,0]

alpha_ref,alphaX = 11.1,1.1
execfile('/home/rumbaugh/set_spec_dict.py')
execfile('/home/rumbaugh/SphDist.py')
targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053","cl1324_north","cl1324_south"])

nh_dict={"rxj1757": 4.08,"cl1604": 1.22,"cl0023": 2.79,"cl1324_north": 1.15,"cl1324_south": 1.16, 'cl1324': 1.155,"rxj1821":5.67, 'rcs0224': 2.86, 'cl0849': 2.73, 'rxj0910': 1.98,'rxj1053': 0.58, 'rxj1221':1.44,'cl1350':1.76,'rxj1716':3.71,'cl1137':1.93}

crRSfit=np.loadtxt('/home/rumbaugh/Chandra/RS_fits.composite_colors.nofit.3.13.16.dat',dtype={'names':('field','y0','m','sig','numsig'),'formats':('|S32','f8','f8','f8','i8')})

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

for field in reffile_dict.keys():
    cram=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s.adammatch.5.5.16.dat'%(field,field,field),dtype={'names':('ID_adam','RA_phot','Dec_phot','z_peak','flag','ID_spec','RA_spec','Dec_spec','z_spec','z_spec_adam','Q','ID_xray','RA_xray','Dec_xray','nummatch','ID_xray_adam','RA_xray_adam','Dec_xray_adam','nummatch_adam','mRFU','mRFB'),'formats':('|S24','f8','f8','f8','f8','|S24','f8','f8','f8','f8','i8','|S24','f8','f8','i8','|S24','f8','f8','i8','f8','f8')})
    matchcat='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_optmatch_comb.%s.dat'%(field,field,field,ldate)
    crs=np.loadtxt('%s/%s'%(spec_dict['basepath'],spec_dict[field]['file']),dtype=specloaddict)
    ra_opt,dec_opt=crs['ra'],crs['dec']
    gq=np.where(crs['Q']>2.5)[0]
    gqz=np.where((crs['Q']>2.5)&(crs['z']>spec_dict[field]['z'][1])&(crs['z']<spec_dict[field]['z'][2]))[0]
    fz0,fzl,fzu=spec_dict[field]['z'][0],spec_dict[field]['z'][1],spec_dict[field]['z'][2]
    refcat='%s/%s/%s.mag.gz'%(refdir,reffile_dict[field],reffile_dict[field])
    if field=='rxj1821':
        cr=np.loadtxt(refcat,dtype=refdict_1821)
    elif field=='rxj0910':
        cr=np.loadtxt(refcat,dtype=refdict0910)
    else:
        cr=np.loadtxt(refcat,dtype=refdict)

    pzcat='%s/%s/%s.zout.gz'%(refdir,reffile_dict[field],reffile_dict[field])
    crpz=np.loadtxt(pzcat,dtype=pzdict)
    rfcat='%s/%s/%s.restframe.gz'%(refdir,reffile_dict[field],reffile_dict[field])
    if field=='rxj0910':
        crrf=np.loadtxt(rfcat,dtype=rfdict0910)
    else:
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
    
    gall=np.where((crpz['u99']>=fzl)&(crpz['l99']<=fzu)&(cr['use']==1)&(mRFB<-20.9)&(mRFB>-80))[0]


    mu,sigma=0.5*(crpz['u99']+crpz['l99']),3*0.5*(crpz['u99']-crpz['l99'])
    zdummy=np.linspace(fzl,fzu,500)
    zstep=zdummy[1]-zdummy[0]
    PDF=1./sigma.reshape((len(mu),1))/np.sqrt(2*np.pi)*np.exp(-(zdummy-mu.reshape((len(mu),1)))**2/(2*sigma.reshape((len(mu),1))**2))
    P_inclus=np.sum(PDF,axis=1)*zstep
    gnew0=np.where((crpz['u99']>=fzl)&(crpz['l99']<=fzu)&(cr['use']==1)&(cram['Q']!=-1)&(cram['Q']<2.5)&(mRFB<-20.9)&(mRFB>-80))[0]
    gCH=np.where(inCH[gall]>=1)[0]
    gnew=np.where(inCH[gnew0]>=1)[0]
    gxray=np.where(cram['nummatch'][gnew0][gnew]>0)[0]
    gbf=np.where(crbf['field']==field)[0]
    BF,numBF,BF_cut,numBF_cut=crbf['BF'][gbf][0],crbf['num'][gbf][0],crbf['BF_cut'][gbf][0],crbf['num_cut'][gbf][0]

    print field,np.sum(P_inclus[gall]),np.sum(P_inclus[gnew0]),np.sum(P_inclus[gnew0][gnew]),np.sum(P_inclus[gall][gCH])
    gRS,gGV,gBC=np.where(-rso[gnew0][gnew]>=-1)[0],np.where((-rso[gnew0][gnew]<-1)&(-rso[gnew0][gnew]>=-3))[0],np.where(-rso[gnew0][gnew]<-3)[0]
    gRSx,gGVx,gBCx=np.where(-rso[gnew0][gnew][gxray]>=-1)[0],np.where((-rso[gnew0][gnew][gxray]<-1)&(-rso[gnew0][gnew][gxray]>=-3))[0],np.where(-rso[gnew0][gnew][gxray]<-3)[0]
    pRS,pGV,pBC=np.sum(P_inclus[gnew0][gnew][gRS]),np.sum(P_inclus[gnew0][gnew][gGV]),np.sum(P_inclus[gnew0][gnew][gBC])
    newRS,newBC=pRS+numBF*(1-BF),pGV+pBC+numBF*BF
    print 'RS: %.1f  GV: %.1f  BC: %.1f'%(np.sum(P_inclus[gnew0][gnew][gRS]),np.sum(P_inclus[gnew0][gnew][gGV]),np.sum(P_inclus[gnew0][gnew][gBC]))
    print 'RS: %.1f BC: %.1f BF: %.4f'%(newRS,newBC,newBC*1./(newBC+newRS))
    FILE.write('%12s %.4f %3i %.4f %3i %.4f %6.2f\n'%(field,BF,numBF,BF_cut,numBF_cut,newBC*1./(newBC+newRS),newBC+newRS))
FILE.close()
