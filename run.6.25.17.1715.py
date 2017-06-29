import numpy as np
import matplotlib.pyplot as plt
import matplotlib
execfile('/home/rumbaugh/set_spec_dict.py')
execfile('/home/rumbaugh/CalcVelDisp.py')
execfile('/home/rumbaugh/cosmocalc.py')
execfile('/home/rumbaugh/SphDist.py')
execfile('/home/rumbaugh/DStest.py')
execfile("/home/rumbaugh/scale_estimators.py")
degree_symbol = unichr(176)
html_purp = '#9933FF'
html_teal = '#33FFFF'
html_brwn = '#996600'
html_orng = '#FFCC00'
html_pink = '#FF00FF'

try:
    ntrials
except NameError:
    ntrials = 10000
c=3.*10**5

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
cr=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clusters.dat',dtype={'names':('field','cluster','RA','Dec','z','sig0.5','sig0.5err','n0.5','sig','sigerr','nsig'),'formats':('|S24','|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8')})
crx=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.X-ray_centers_for_paper.dat',dtype={'names':('field','cluster','RA','DEC'),'formats':('|S20','|S20','f8','f8')},usecols=(0,1,2,3))

crz=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clus_sigs_wZ.6.25.17.dat',dtype={'names':('field','cluster','sigall','saerr','Nsa','sigcut','scerr','Nsc','sigred','srerr','Nsr','sigblue','sberr','Nsb','Zlb','Zub'),'formats':('|S20','|S20','f8','f8','i8','f8','f8','i8','f8','f8','i8','f8','f8','i8','f8','f8')})


cosmocalc(cr['z'],outfile='/home/rumbaugh/cc_out_clus.1.28.17.dat',ids=cr['cluster'])

crcc=np.loadtxt('/home/rumbaugh/cc_out_clus.1.28.17.dat',usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19))
kpc = crcc[:,12]
Hz = crcc[:,16]*70.
Mpc = kpc/1000.

FILE=open('/home/rumbaugh/Chandra/ORELSE.DStests.6.25.17.dat','w')
FILE.write('#Field Cluster DSstat P\n')

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
    crspec=read_spec_file(field)
    try:
        gz=np.where(crz['cluster']==clus)[0][0]
    except:
        print "Didn't use this one before"
        continue
    matplotlib.rcParams['figure.figsize'] = [7,7]
    matplotlib.rcParams['axes.linewidth'] = 3
    matplotlib.pyplot.tick_params(width=2,length=4)
    fig = matplotlib.figure.Figure()
    plt.figure(1)
    plt.clf()
    sig=crz['sigall'][gz]
    gspecz=np.where((crspec['Q']>2.5)&(crspec['z']>crz['Zlb'][gz])&(crspec['z']<crz['Zub'][gz]))[0]
    tdists=SphDist(crspec['ra'][gspecz],crspec['dec'][gspecz],raC,decC)
    gclose=np.where(tdists<Mpc_am)[0]
    zs,ras,decs=crspec['z'][gspecz][gclose],crspec['ra'][gspecz][gclose],crspec['dec'][gspecz][gclose]
    avg_z=biweight_loc(zs)
    zsig = sig*(1+avg_z)/c
    
    if len(zs)<=0:
        print 'Nothing close to %s'%clus
        continue
    zmin,zmax=crz['Zlb'][gz],crz['Zub'][gz]
    #gz2=np.where((crCMD[gcCMD]['z']>zmin-0.00001)&(crCMD[gcCMD]['z']<zmax+0.00001))[0]

    #tdists=SphDist(crCMD['ra'][gcCMD[gz2]],crCMD['dec'][gcCMD[gz2]],raC,decC)
    #gclose=np.where(tdists<Mpc_am)[0]
    #allzs2=crCMD['z'][gcCMD[gz2[gclose]]]
    if len(zs)>10:
        DSstat,P,delta=DStest(ras,decs,zs,use_vel_in=False,reps=ntrials)
        print clus,DSstat,P
        FILE.write('%12s %14s %f %f\n'%(field,clus,DSstat,P))
    else:
        continue
FILE.close()
