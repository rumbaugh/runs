import numpy as np
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/set_spec_dict.py')
execfile('/home/rumbaugh/CalcVelDisp.py')
execfile('/home/rumbaugh/cosmocalc.py')
execfile('/home/rumbaugh/SphDist.py')
execfile("/home/rumbaugh/scale_estimators.py")
import matplotlib.backends.backend_pdf as bpdf
psfpdf=bpdf.PdfPages('/home/rumbaugh/Chandra/plots/CMDs_clusters.6.26.17.pdf')
try:
    ntrials
except NameError:
    ntrials = 10000
numsig=3

fielddict={'rxj0910':'SC0910','cl0023':'SG0023','cl1324':'SC1324','cl0849':'SC0849','cl1604':'SC1604','cl1137':'Cl1137','cl1350':'Cl1350'}

crRS=np.loadtxt('/home/rumbaugh/final_RS_values_supercolors.notes',dtype={'names':('field','y0','m','sig'),'formats':('|S32','f8','f8','f8')})
crRS_ACS=np.loadtxt('/home/rumbaugh/Chandra/RS_fits.cl1604_ACS.nofit.3.6.16.dat',dtype={'names':('field','y0','m','sig','numsig'),'formats':('|S32','f8','f8','f8','i8')})

def read_spec_file(field):
    fname='/home/rumbaugh/git/ORELSE/Catalogs/Spec_z/%s'%spec_dict[field]['file']
    if field=='cl1604':
        loaddict=ACSspecloaddictwnotes
        uc=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)
    else:
        loaddict=specloaddictwnotes
        uc=(0,1,2,3,4,5,6,7,8,9,10,11)
    crspec=np.genfromtxt(fname,dtype=loaddict,usecols=uc)
    return crspec

def zhist(zs,zrange=None,zbins=10,fname=None,zclus=None):
    execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
    plt.hist(zs,range=zrange,bins=zbins)
    if zclus!=None: plt.axvline(zclus,lw=2,ls='dashed',color='r')
    plt.xlabel('Redshift')
    plt.ylabel('Num. of galaxies')
    if fname!=None: plt.savefig(fname)

def spatplot(ras,decs,fname=None):
    execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
    plt.scatter(ras,decs)
    plt.xlabel('RA')
    plt.ylabel('Dec.')
    xlim=plt.xlim()
    plt.xlim(xlim[1],xlim[0])
    if fname!=None: plt.savefig(fname)

crf=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.cluster_fits.dat',dtype={'names':('cluster','r0','r0-','r0+','blg','bkg-','blg+','r500','r500NC','NC'),'formats':('|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8')})
crf=crf[crf['cluster']!='0225-0019']
cr=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clusters.dat',dtype={'names':('field','cluster','RA','Dec','z','sig0.5','sig0.5err','n0.5','sig','sigerr','nsig'),'formats':('|S24','|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8')})
crx=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.X-ray_centers_for_paper.dat',dtype={'names':('field','cluster','RA','DEC'),'formats':('|S20','|S20','f8','f8')},usecols=(0,1,2,3))
crx=crx[crx['cluster']!='XLSS005']

crz=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clus_sigs_wZ.6.25.17.dat',dtype={'names':('field','cluster','sigall','saerr','Nsa','sigcut','scerr','Nsc','sigred','srerr','Nsr','sigblue','sberr','Nsb','Zlb','Zub'),'formats':('|S20','|S20','f8','f8','i8','f8','f8','i8','f8','f8','i8','f8','f8','i8','f8','f8')})


cosmocalc(cr['z'],outfile='/home/rumbaugh/cc_out_clus.1.28.17.dat',ids=cr['cluster'])

crcc=np.loadtxt('/home/rumbaugh/cc_out_clus.1.28.17.dat',usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19))
kpc = crcc[:,12]
Hz = crcc[:,16]*70.
Mpc = kpc/1000.
crCMD=np.loadtxt('/home/rumbaugh/Chandra/CMD_info_all.6.26.17.dat',dtype={'names':('mag','col','ra','dec','z','rso','field'),'formats':('f8','f8','f8','f8','f8','f8','|S20')})
crCMD=crCMD[crCMD['mag']>-40]
outcr=np.zeros((len(crf),),dtype={'names':('field','cluster','ra','dec','zcen','zmin','zmax','rad'),'formats':('|S12','|S12','f8','f8','f8','f8','f8','f8')})

outgalcr=np.zeros((0,),dtype={'names':('field','cluster','ra','dec','z','Mred','Mcol','rso'),'formats':('|S12','|S12','f8','f8','f8','f8','f8','f8')})

for clus,ic in zip(crx['cluster'],np.arange(len(crx))):
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
    gcx=np.where(crx['cluster']==clus)[0][0]
    rax,decx=crx['RA'][gcx],crx['DEC'][gcx]
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
    if zC==None: zC=0.5*(crz['Zlb'][gz]+crz['Zub'][gz])
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
    gblue,gred,gsred=np.where(crCMD['rso'][gcCMD[gz2[gclose]]]>1)[0],np.where(np.abs(crCMD['rso'][gcCMD[gz2[gclose]]])<1)[0],np.where(crCMD['rso'][gcCMD[gz2[gclose]]]<-1)[0]
    gnotred=np.union1d(gblue,gsred)
    gBCG,gallBCG=np.argsort(crCMD['mag'][gcCMD[gz2[gclose[gred]]]])[0],np.argsort(crCMD['mag'][gcCMD[gz2[gclose]]])[0]
    outcr['field'][ic],outcr['cluster'][ic],outcr['ra'][ic],outcr['dec'][ic],outcr['zcen'][ic],outcr['zmin'][ic],outcr['zmax'][ic],outcr['rad'][ic]=field,clus,rax,decx,zC,zmin,zmax,Mpc_am

    tmpgalcr=np.zeros((len(gclose),),dtype={'names':('field','cluster','ra','dec','z','Mred','Mcol','rso'),'formats':('|S12','|S12','f8','f8','f8','f8','f8','f8')})
    tmpgalcr['field'],tmpgalcr['cluster'],tmpgalcr['ra'],tmpgalcr['dec'],tmpgalcr['z'],tmpgalcr['Mred'],tmpgalcr['Mcol'],tmpgalcr['rso']=field,clus,crCMD['ra'][gcCMD[gz2[gclose]]],crCMD['dec'][gcCMD[gz2[gclose]]],crCMD['z'][gcCMD[gz2[gclose]]],crCMD['mag'][gcCMD[gz2[gclose]]],crCMD['col'][gcCMD[gz2[gclose]]],crCMD['rso'][gcCMD[gz2[gclose]]]
    outgalcr=np.concatenate((outgalcr,tmpgalcr))


np.savetxt('/home/rumbaugh/Chandra/ORELSE.cluster_bounds.6.26.17.dat',outcr,header='field cluster ra dec zcen zmin zmax rad',fmt='%12s %12s %f %f %f %f %f %f')
np.savetxt('/home/rumbaugh/Chandra/ORELSE.cluster_members.6.26.17.dat',outgalcr,header='field cluster ra dec z Mred Mred-Mblue rso',fmt='%12s %12s %f %f %f %f %f %f')
