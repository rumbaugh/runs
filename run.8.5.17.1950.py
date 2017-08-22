import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
execfile('/home/rumbaugh/set_spec_dict.py')
execfile('/home/rumbaugh/CalcVelDisp.py')
execfile('/home/rumbaugh/cosmocalc.py')
execfile('/home/rumbaugh/SphDist.py')
execfile("/home/rumbaugh/scale_estimators.py")
try:
    ntrials
except NameError:
    ntrials = 10000


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

#crCMD=np.loadtxt('/home/rumbaugh/Chandra/CMD_info_all.6.26.17.dat',dtype={'names':('mag','col','ra','dec','z','rso','field'),'formats':('f8','f8','f8','f8','f8','f8','|S20')})

MMCGdf=pd.read_csv('/home/rumbaugh/MMCGs_fotNick/MMCG_tot_1.5Rvir.08.02.17.cat',delim_whitespace=True,usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,))


FILE=open('/home/rumbaugh/Chandra/ORELSE.veldiffs.RF.dat','w')
FILE.write('#Field Cluster SF_vel_cen Q_vel_cen perc perc_bwl_BS\n')
FILE2=open('/home/rumbaugh/Chandra/ORELSE.clus_sigs_RF.dat','w')
FILE2.write('#Field Cluster Sig_all Sig_all_Error Sig_all_N Sig_Q Sig_Q_Error Sig_Q_N Sig_SF Sig_SF_Error Sig_SF_N\n')

for clus in crf['cluster']:
    try:
        CMdf=pd.read_csv('/home/rumbaugh/MMCGs_fotNick/cluster_member_1Mpc/Cluster_member_{}_spec_1Mpc.cat'.format(clus),delim_whitespace=True)
    except IOError:
        continue
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
    allsig,allsigerr=CalcVelDisp(CMdf.z_spec.values)
    Qzs,SFzs=CMdf.z_spec.values[CMdf.Quiescent.values==1],CMdf.z_spec.values[CMdf.Quiescent.values==0]
    if len(Qzs)>2:
        Qsig,Qsigerr=CalcVelDisp(Qzs)
    else:
        Qsig,Qsigerr=0,0
    if len(SFzs)>2:
        SFsig,SFsigerr=CalcVelDisp(SFzs)
    else:
        SFsig,SFsigerr=0,0
    Qvelcen,SFvelcen,perc_bwl,perc_bwl_BS=0,0,0,0
    if ((len(Qzs) > 4.5) & (len(SFzs) > 4.8)):
        Q_bwl,SF_bwl=biweight_loc(Qzs),biweight_loc(SFzs)
        diffs_bwl = np.zeros(ntrials)
        diffs_bwl_BS = np.zeros(ntrials)
        for j in range(0,ntrials):
            Qvels_t,SFvels_t =np.random.choice(Qzs,len(Qzs)),np.random.choice(SFzs,len(SFzs))
            Q_bwl_BS = biweight_loc(Qvels_t)
            SF_bwl_BS = biweight_loc(SFvels_t)
            diffs_bwl_BS[j] = np.fabs(Q_bwl_BS-SF_bwl_BS)
            grnd=np.arange(len(CMdf.z_spec.values))
            np.random.shuffle(grnd)
            Qt_bwl = biweight_loc(CMdf.z_spec.values[grnd[:len(Qzs)]])
            SFt_bwl = biweight_loc(CMdf.z_spec.values[grnd[len(Qzs):]])
            diffs_bwl[j] =np.abs(Qt_bwl-SFt_bwl)
        sort_bwl = np.sort(diffs_bwl)
        sort_BWL_BS = np.sort(diffs_bwl_BS)
        gsbwl = np.where(sort_bwl > np.abs(Q_bwl-SF_bwl))[0]
        gsbwlBS = np.where(sort_BWL_BS > np.abs(Q_bwl-SF_bwl))[0]
        perc_bwl =len(gsbwl)*1.0/ntrials
        perc_bwl_BS = len(gsbwlBS)*1.0/ntrials
        Qvelcen,SFvelcen=Q_bwl,SF_bwl
    FILE.write('%12s %14s %f %f %f %f\n'%(field,clus,Qvelcen,SFvelcen,perc_bwl,perc_bwl_BS))
    FILE2.write('%12s %14s %f %f %i %f %f %i %f %f %i\n'%(field,clus,allsig,allsigerr,len(CMdf),Qsig,Qsigerr,len(Qzs),SFsig,SFsigerr,len(SFzs)))
FILE.close()
FILE2.close()
