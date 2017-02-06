import numpy as np
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/set_spec_dict.py')
execfile('/home/rumbaugh/CalcVelDisp.py')
execfile('/home/rumbaugh/cosmocalc.py')
execfile('/home/rumbaugh/SphDist.py')

def read_spec_file(field):
    fname='/home/rumbaugh/Chandra/speccats/%s'%spec_dict[field]['file']
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
cr=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clusters.dat',dtype={'names':('field','cluster','RA','Dec','z','sig0.5','sig0.5err','n0.5','sig','sigerr','nsig'),'formats':('|S24','|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8')})
crx=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.X-ray_centers_for_paper.dat',dtype={'names':('field','cluster','RA','DEC'),'formats':('|S20','|S20','f8','f8')},usecols=(0,1,2,3))

crz=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clus_sigs_wZ.dat',dtype={'names':('field','cluster','sigall','saerr','Nsa','sigcut','scerr','Nsc','sigred','srerr','Nsr','sigblue','sberr','Nsb','Zlb','Zub'),'formats':('|S20','|S20','f8','f8','i8','f8','f8','i8','f8','f8','i8','f8','f8','i8','f8','f8')})


cosmocalc(cr['z'],outfile='/home/rumbaugh/cc_out_clus.1.28.17.dat',ids=cr['cluster'])

crcc=np.loadtxt('/home/rumbaugh/cc_out_clus.1.28.17.dat',usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19))
kpc = crcc[:,12]
Hz = crcc[:,16]*70.
Mpc = kpc/1000.
crCMD=np.loadtxt('/home/rumbaugh/Chandra/CMD_info_all.1.29.17.dat',dtype={'names':('mag','col','ra','dec','z','rso','field'),'formats':('f8','f8','f8','f8','f8','f8','|S20')})
FILE=open('/home/rumbaugh/Chandra/ORELSE.clus_sigs.dat','w')
FILE.write('# Field Cluster Sig_all Error N Sig_all_cut Error N Sig_red Error N Sig_blue Error N\n')
for clus in crf['cluster']:
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
    allsig=CalcVelDisp(allzs,returnclipped=True)
    print clus,allsig[0]
    plt.figure(1)
    plt.clf()
    zhist(allzs[allsig[2]],zclus=zC,fname='/home/rumbaugh/Chandra/plots/clus_sig.%s.%s.zhist.wbounds.2.1.17.png'%(field,clus),zrange=(spec_dict[field]['z'][1],spec_dict[field]['z'][2]),zbins=int((-spec_dict[field]['z'][1]+spec_dict[field]['z'][2])/0.001))
    plt.figure(2)
    plt.clf()
    #spatplot(crspec['ra'][gspecz[gclose[allsig[2]]]],crspec['dec'][gspecz[gclose[allsig[2]]]],fname='/home/rumbaugh/Chandra/plots/clus_sig.%s.%s.spatplot.2.1.17.png'%(field,clus))
    gz2=np.where((crCMD[gcCMD]['z']>spec_dict[field]['z'][1])&(crCMD[gcCMD]['z']<spec_dict[field]['z'][2]))[0]

    tdists=SphDist(crCMD['ra'][gcCMD[gz2]],crCMD['dec'][gcCMD[gz2]],raC,decC)
    gclose=np.where(tdists<Mpc_am)[0]
    allzs2=crCMD['z'][gcCMD[gz2[gclose]]]
    allsig2=CalcVelDisp(allzs2,returnclipped=True)
    gblue,gred=np.where(crCMD['rso'][gcCMD[gz2[gclose]]]>1)[0],np.where(crCMD['rso'][gcCMD[gz2[gclose]]]<1)[0]
    if (len(gblue)>0)&(len(gred)>0):
        bluesig,redsig=CalcVelDisp(allzs2[gblue],returnclipped=True),CalcVelDisp(allzs2[gred],returnclipped=True)
    else:
        bluesig,redsig=(0,0),(0,0)
    print allsig2[0]
    print bluesig[0]
    print redsig[0]
    FILE.write('%12s %14s %6.1f %6.1f %3i %6.1f %6.1f %3i %6.1f %6.1f %3i %6.1f %6.1f %3i\n'%(field,clus,allsig[0],allsig[1],len(allzs),allsig2[0],allsig2[1],len(allzs2),bluesig[0],bluesig[1],len(gblue),redsig[0],redsig[1],len(gred)))
FILE.close()
