import numpy as np
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/set_spec_dict.py')
execfile('/home/rumbaugh/cosmocalc.py')
execfile('/home/rumbaugh/SphDist.py')
execfile("/home/rumbaugh/scale_estimators.py")


fielddict={'rxj0910':'SC0910','cl0023':'SG0023','cl1324':'SC1324','cl0849':'SC0849','cl1604':'SC1604','cl1137':'Cl1137','cl1350':'Cl1350'}
crx=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.X-ray_centers_for_paper.dat',dtype={'names':('field','cluster','RA','DEC'),'formats':('|S20','|S20','f8','f8')},usecols=(0,1,2,3))
crf=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.cluster_fits.dat',dtype={'names':('cluster','r0','r0-','r0+','blg','bkg-','blg+','r500','r500NC','NC'),'formats':('|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8')})
cr=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clusters.dat',dtype={'names':('field','cluster','RA','Dec','z','sig0.5','sig0.5err','n0.5','sig','sigerr','nsig'),'formats':('|S24','|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8')})
crCMD=np.loadtxt('/home/rumbaugh/Chandra/CMD_info_all.6.26.17.dat',dtype={'names':('mag','col','ra','dec','z','rso','field'),'formats':('f8','f8','f8','f8','f8','f8','|S20')})

crBCG=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.BCGS.6.26.17.dat',dtype={'names':('field','cluster','BCGra','BCGdec','BCG_Mred','BCGcol','BCGrso','BCGz','allBCGra','allBCGdec','allBCG_Mred','allBCGcol','allBCGrso','allBCGz'),'formats':('|S12','|S12','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')})
gBCGdict={crBCG['cluster'][x]: x for x in np.arange(len(crBCG))}

outcr=np.zeros((0,),dtype={'names':('field','cluster','ra','dec','z','mag','col','rso','isBCG','isBCG_tot'),'formats':('|S12','|S12','f8','f8','f8','f8','f8','f8','i8','i8')})
for clus,ic in zip(crBCG['cluster'],np.arange(len(crBCG))):
    gBCG=gBCGdict[clus]
    try:
        gcr=np.where(cr['cluster']==clus)[0][0]
        raC,decC,zC=cr['RA'][gcr],cr['Dec'][gcr],cr['z'][gcr]
        Mpc_am=1./Mpc[gcr]/60.
        field=cr['field'][gcr].lower()
    except:
        print '%s not found, using X-ray center'%clus
        try:
            gcr=np.where(crx['cluster']==clus)[0][0]
            raC,decC=crx['RA'][gcr],crx['DEC'][gcr]
            field=crx['field'][gcr].lower()
            zf=spec_dict[field]['z'][0]
            cosmocalc(zf,outfile='/home/rumbaugh/temp_cc.2.1.17.dat')
            crcctmp=np.loadtxt('/home/rumbaugh/temp_cc.2.1.17.dat')
            Mpc_am=1./(crcctmp[12]/1000.)/60.
            zC=None
        except:
            print 'X-ray center not found either'
            continue
    try:
        propername=fielddict[field]
    except KeyError:
        propername=field.upper()

    gf=np.where(crRS['field']==propername)[0][0]
    y0,m,sig=crRS['y0'][gf],crRS['m'][gf],crRS['sig'][gf]
    if field=='cl1604':y0,m,sig=crRS_ACS['y0']+0,crRS_ACS['m']+0,crRS_ACS['sig']+0
    width=2*numsig*sig

    gcCMD=np.where(crCMD['field']==field)[0]
    crspec=read_spec_file(field)
    try:
        gz=np.where(crz['cluster']==clus)[0][0]
    except:
        print "Didn't use this one before"
        continue
    gspecz=np.where((crspec['Q']>2.5)&(crspec['z']>crz['Zlb'][gz])&(crspec['z']<crz['Zub'][gz]))[0]
    tdists=SphDist(crspec['ra'][gspecz],crspec['dec'][gspecz],raC,decC)
    gclose=np.where(tdists<Mpc_am)[0]
    allzs=crspec['z'][gspecz][gclose]
    if len(allzs)<=0:
        print 'Nothing close to %s'%clus
        continue
    zmin,zmax=crz['Zlb'][gz],crz['Zub'][gz]
    gz2=np.where((crCMD[gcCMD]['z']>zmin-0.00001)&(crCMD[gcCMD]['z']<zmax+0.00001))[0]

    tdists=SphDist(crCMD['ra'][gcCMD[gz2]],crCMD['dec'][gcCMD[gz2]],raC,decC)
    gclose=np.where(tdists<Mpc_am)[0]
    allzs2=crCMD['z'][gcCMD[gz2[gclose]]]
    gblue,gRS,gsred=np.where(crCMD['rso'][gcCMD[gz2[gclose]]]>1)[0],np.where(np.abs(crCMD['rso'][gcCMD[gz2[gclose]]])<1)[0],np.where(crCMD['rso'][gcCMD[gz2[gclose]]]<-1)[0]
    gnotred,gred=np.union1d(gblue,gsred),np.union1d(gRS,gsred)
    BCGdist=SphDist(crCMD['ra'][gcCMD[gz2[gclose]]],crCMD['dec'][gcCMD[gz2[gclose]]],crBCG['BCGra'][gBCG],crBCG['BCGdec'][gBCG])
    allBCGdist=SphDist(crCMD['ra'][gcCMD[gz2[gclose]]],crCMD['dec'][gcCMD[gz2[gclose]]],crBCG['allBCGra'][gBCG],crBCG['allBCGdec'][gBCG])
    outcrT=np.zeros((len(gclose),),dtype={'names':('field','cluster','ra','dec','z','mag','col','rso','isBCG','isBCG_tot'),'formats':('|S12','|S12','f8','f8','f8','f8','f8','f8','i8','i8')})
    outcrT['field'],outcrT['cluster'],outcrT['ra'],outcrT['dec'],outcrT['z'],outcrT['mag'],outcrT['col'],outcrT['rso'],outcrT['isBCG'],outcrT['isBCG_tot']=field,clus,crCMD['ra'][gcCMD[gz2[gclose]]],crCMD['dec'][gcCMD[gz2[gclose]]],crCMD['z'][gcCMD[gz2[gclose]]],crCMD['mag'][gcCMD[gz2[gclose]]],crCMD['col'][gcCMD[gz2[gclose]]],crCMD['rso'][gcCMD[gz2[gclose]]],np.arange(len(outcrT))==np.argsort(BCGdist)[0],np.arange(len(outcrT))==np.argsort(allBCGdist)[0]
    outcr=np.append(outcr,outcrT)
np.savetxt('/home/rumbaugh/Chandra/ORELSE_cluster_member_info_all.6.26.17.dat',outcr,header='field cluster ra dec z mag col rso isBCG isBCG_tot',fmt='%12s %12s %f %f %f %f %f %f %i %i')
