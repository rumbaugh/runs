import numpy as np
import pyfits as py
from ConcaveHull import ConcaveHull,CheckPoints
from shapely.geometry import box as makebox
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/calc_Xray_lums.py')
execfile('/home/rumbaugh/setup_adam_cats.py')
execfile('/home/rumbaugh/set_spec_dict.py')
execfile('/home/rumbaugh/SphDist.py')

target_dir={"RCS0224":"rcs0224","SC0849":"cl0849","SC0910":"rxj0910","RXJ1221":"rxj1221","Cl1350":"cl1350","NEP200":"rxj1757","SG0023":"cl0023","SC1324":'cl1324',"NEP5281":"rxj1821","Cl1137":"cl1137","RXJ1716":"rxj1716","RXJ1053":"rxj1053","SC1604":"cl1604","RXJ1821":"rxj1821","RXJ1757":"rxj1757"}
adamcorrval=-1.3975614258700002

alpha_ref,alphaX = 11.1,1.1
targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053","cl1324_north","cl1324_south"])

nh_dict={"rxj1757": 4.08,"cl1604": 1.22,"cl0023": 2.79,"cl1324_north": 1.15,"cl1324_south": 1.16, 'cl1324': 1.155,"rxj1821":5.67, 'rcs0224': 2.86, 'cl0849': 2.73, 'rxj0910': 1.98,'rxj1053': 0.58, 'rxj1221':1.44,'cl1350':1.76,'rxj1716':3.71,'cl1137':1.93}

ldate='1.19.16'

FILEl=open('/home/rumbaugh/Chandra/fluxes_newphotoz_adam.1sig.7.8.16.dat','w')
FILEl.write('# field ID RA Dec z_peak nh flux_soft flux_hard flux_full P_inclus\n')

crcc=np.loadtxt('/home/rumbaugh/cc_out.2.19.16.dat')
D_L=crcc[:,13]*3.086E22
DM=crcc[:,15]
kpc=crcc[:,12]
cc_z=crcc[:,0]

crRS = np.loadtxt('/home/rumbaugh/Chandra/RS_offsets_wACS.6.13.16.dat',dtype={'names':('field','number','ID','RA','Dec','RSoffset','magR','magI','magZ','SCmagRed','SCmagBlue'),'formats':('|S24','i8','|S24','f8','f8','f8','f8','f8','f8','f8','f8')})

crRSfit=np.loadtxt('/home/rumbaugh/final_RS_values_supercolors.notes',dtype={'names':('field','y0','m','sig'),'formats':('|S32','f8','f8','f8')})
for i in range(0,len(crRSfit['field'])): crRSfit['field'][i]=target_dir[crRSfit['field'][i]]

indict={'names':('field','number','RA','Dec','lum_soft','lum_hard','lum_full','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit'),'formats':('|S32','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S32','|S32')}

crn=np.loadtxt('/home/rumbaugh/X-ray_lum_cat.4.17.16.dat',dtype=indict)
g1324=np.where((crn['field']=='cl1324_north')|(crn['field']=='cl1324_south'))[0]
crn['field'][g1324]='cl1324'

gAGN=np.zeros(len(crRS['RA']-2),dtype='i8')

rkeys=np.array(reffile_dict.keys())
for field in rkeys[rkeys!='cl1324']:
    cram=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s.adammatch.5.5.16.dat'%(field,field,field),dtype={'names':('ID_adam','RA_phot','Dec_phot','z_peak','flag','ID_spec','RA_spec','Dec_spec','z_spec','z_spec_adam','Q','ID_xray','RA_xray','Dec_xray','nummatch','ID_xray_adam','RA_xray_adam','Dec_xray_adam','nummatch_adam','mRFU','mRFB'),'formats':('|S24','f8','f8','f8','f8','|S24','f8','f8','f8','f8','i8','|S24','f8','f8','i8','|S24','f8','f8','i8','f8','f8')})
    crPI=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s.P_inclus.7.1.16.dat'%(field,field,field))
    crs=np.loadtxt('%s/%s'%(spec_dict['basepath'],spec_dict[field]['file']),dtype=specloaddict)
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

    truenum=len(crRS['number'][((crRS['field']==field)&(crRS['number']>-1))])
    gknown=np.where((crpz['z_spec']>=fzl)&(crpz['z_spec']<=fzu)&(cram['Q']>2.5))[0]
    trueall=len(gknown)

    gf=np.where(crRSfit['field']==field)[0][0]
    y0,m,sig=crRSfit['y0'][gf],crRSfit['m'][gf],crRSfit['sig'][gf]
    width=6*sig
    rso=(y0+m*(mRFB+adamcorrval)-(mRFU-mRFB))/(0.5*width)

    crCH=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s.photz_inspeccov.4.23.16.dat'%(field,field,field),dtype='i8')
    inCH=crCH[:,4]
    
    gall=np.where((crpz['u99']>=fzl)&(crpz['l99']<=fzu)&(cr['use']==1)&(mRFB<-20.9)&(mRFB>-80))[0]

    P_inclus=crPI
    gold=np.where((crpz['u99']>=fzl)&(crpz['l99']<=fzu)&(cr['use']==1)&(cram['Q']>2.5)&(mRFB<-20.9)&(mRFB>-80))[0]
    gnew0=np.where((crpz['u99']>=fzl)&(crpz['l99']<=fzu)&(cr['use']==1)&(cram['Q']!=-1)&(cram['Q']<2.5)&(mRFB<-20.9)&(mRFB>-80))[0]
    gCH=np.where(inCH[gall]>=1)[0]
    gnew=np.where(inCH[gnew0]>=1)[0]
    gxray=np.where(cram['nummatch'][gnew0][gnew]>0)[0]
    gxrayold=np.where(cram['nummatch'][gold]>0)[0]
    print field,np.sum(P_inclus[gall]),np.sum(P_inclus[gnew0]),np.sum(P_inclus[gnew0][gnew]),np.sum(P_inclus[gall][gCH])
    print 'Exp. new Xray: %.2f, Exp. old Xray: %.2f, True old Xray: %i'%(np.sum(P_inclus[gnew0][gnew][gxray]),np.sum(P_inclus[gold][gxrayold]),truenum)
    print 'Exp. new: %.2f, Exp. old: %.2f, True old: %i'%(np.sum(P_inclus[gnew0][gnew]),np.sum(P_inclus[gold]),trueall)
    gRS,gGV,gBC=np.where(-rso[gnew0][gnew]>=-1)[0],np.where((-rso[gnew0][gnew]<-1)&(-rso[gnew0][gnew]>=-3))[0],np.where(-rso[gnew0][gnew]<-3)[0]
    gRSx,gGVx,gBCx=np.where(-rso[gnew0][gnew][gxray]>=-1)[0],np.where((-rso[gnew0][gnew][gxray]<-1)&(-rso[gnew0][gnew][gxray]>=-3))[0],np.where(-rso[gnew0][gnew][gxray]<-3)[0]
    print 'RS: %.1f  GV: %.1f  BC: %.1f'%(np.sum(P_inclus[gnew0][gnew][gRS]),np.sum(P_inclus[gnew0][gnew][gGV]),np.sum(P_inclus[gnew0][gnew][gBC]))
    print 'RS: %.1f  GV: %.1f  BC: %.1f'%(np.sum(P_inclus[gnew0][gnew][gRSx]),np.sum(P_inclus[gnew0][gnew][gGVx]),np.sum(P_inclus[gnew0][gnew][gBCx]))

    crxp=py.open('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/SRCv1/%s_srclist_v1.fits'%(field,field,field))
    pdata=crxp[1].data

    fluxes=np.zeros((len(gxray),3))
    fluxes[:,0],fluxes[:,1],fluxes[:,2]=pdata['Soft_flux'][np.array(cram['ID_xray'][gnew0][gnew][gxray],dtype='i8')],pdata['Hard_flux'][np.array(cram['ID_xray'][gnew0][gnew][gxray],dtype='i8')],pdata['Full_flux'][np.array(cram['ID_xray'][gnew0][gnew][gxray],dtype='i8')]
    calc_dict={'z': crpz['z_peak'][gnew0][gnew][gxray], 'nh': np.ones(len(gxray))*nh_dict[field], 'bands':{ 'names': np.array(['soft','hard','full']), 'kev': np.array([[0.5,2.0],[2.0,7.0],[0.5,7.0]])}, 'flux':fluxes}
    for iflx in range(0,len(gxray)):
        FILEl.write('%12s %i %9.5f %9.5f %f %f %E %E %E %.3f\n'%(field,cr['ID'][gnew0][gnew][gxray][iflx],cr['ra'][gnew0][gnew][gxray][iflx], cr['dec'][gnew0][gnew][gxray][iflx],crpz['z_peak'][gnew0][gnew][gxray][iflx], nh_dict[field],fluxes[iflx][0],fluxes[iflx][1],fluxes[iflx][2],P_inclus[gnew0][gnew][gxray][iflx]))
    plt.figure(2)
    plt.clf()
    plt.scatter(crpz['z_spec'][gold],P_inclus[gold])
    plt.axvline(fzl)
    plt.axvline(fzu)
    plt.xlim(fzl-0.5,fzu+0.5)
    plt.ylim(-0.01,1.01)
    plt.xlabel('Spectroscopic Redshift')
    plt.ylabel('P(in_structure)')
    plt.savefig('/home/rumbaugh/Chandra/plots/P_inclus_test.%s.7.8.16.png'%field)
    plt.figure(2)
    plt.clf()
    plt.hist(P_inclus[gold][((crpz['z_spec'][gold]>=fzl)&(crpz['z_spec'][gold]<=fzu))],range=(0,1),bins=20)
    plt.xlim(0,1)
    plt.xlabel('P(in_structure)')
    plt.savefig('/home/rumbaugh/Chandra/plots/P_inclus_test_hist.%s.7.8.16.png'%field)
    
    #plt.scatter(rso[gnew0][gnew][gxray],lums[:,2],marker=fieldmarkers[field],color=fieldcolors[field],s=100,lw=2)
#plt.figure(2)    
#plt.savefig('/home/rumbaugh/Chandra/plots/RSoffset_vs_Lum.4.26.16.png')
FILEl.close()
