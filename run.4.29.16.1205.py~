import numpy as np
import matplotlib.pyplot as plt
execfile("/home/rumbaugh/makeCMD.py")
execfile("/home/rumbaugh/set_spec_dict.py")
import matplotlib.backends.backend_pdf as bpdf
psfpdf=bpdf.PdfPages('/home/rumbaugh/Chandra/plots/CMDs_spec_coverage_test.4.19.16.pdf')

ldate='1.19.16'

crcut=np.loadtxt('/home/rumbaugh/SC_to_iz_cuts.4.19.16.dat',dtype={'names':('field','icut','zcut'),'formats':('|S24','f8','f8')})

adamcorrval=-1.3975614258700002
ierrmax=99999999

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053"])
optmatchloaddict={'names':('indX','raX','decX','errX','nummatch','raopt1','decopt1','optID1','Popt1','likeopt1','raopt2','decopt2','optID2','Popt2','likeopt2','raopt3','decopt3','optID3','Popt3','likeopt3','probnone'),'formats':('i8','f8','f8','f8','i8','f8','f8','|S32','f8','f8','f8','f8','|S32','f8','f8','f8','f8','|S32','f8','f8','f8')}

zlist=np.zeros(len(targets))
for i in range(0,len(targets)): zlist[i]=spec_dict[targets[i]]['z'][0]
zarr=np.linspace(0.1,2,1000)
ARed,ABlue=0.424*(1-1.794*(zarr-0.628)),0.45*(1-1.824*(zarr-0.679))
BRed,BBlue=0.576*(1.794*(zarr-0.628)),0.55*(1.824*(zarr-0.679))
ARed[zarr>1/1.794+0.628]=0
BRed[zarr<0.628]=0
ABlue[zarr>1/1.824+0.679]=0
BBlue[zarr<0.679]=0
param_dict={'ARed':ARed,'ABlue':ABlue,'BRed':BRed,'BBlue':BBlue,'z':zarr}
fig=figure(1)
for field in targets[np.argsort(zlist)]:
    print field
    gcrc=np.where(crcut['field']==field)[0]
    icut,zcut=crcut['icut'][gcrc],crcut['zcut'][gcrc]
    pcat = '/home/rumbaugh/Chandra/photcats/%s_rizdata.corr.gz'%field
    scat='%s/%s'%(spec_dict['basepath'],spec_dict[field]['file'])
    refdict={'names':('ID','dum1','dum2','ra','dec','magR','dmagR','magI','dmagI','magZ','dmagZ'),'formats':('|S64','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')}
    crp=np.loadtxt(pcat,dtype=refdict)
    useoldid=True
    if field=='cl1604':
        crs=np.loadtxt(scat,dtype=ACSspecloaddictwnotes)
    else:
        try:
            crs=np.loadtxt(scat,dtype=specloaddictwnotes)
        except:
            crs=np.loadtxt(scat,dtype=specloaddictwnotes2)
            useoldid=False
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
    numX=len(crm['indX'])
    mras,mdecs=crm['raopt1'],crm['decopt1']
    nummatch=crm['nummatch']
    zcur,magrcur,magicur,magzcur,zerrcur,qcur=-99.*np.ones(numX),-99.*np.ones(numX),-99.*np.ones(numX),-99.*np.ones(numX),-99.*np.ones(numX),-99*np.ones(numX,dtype='i8')
    magrcurp,magicurp,magzcurp=-99.*np.ones(numX),-99.*np.ones(numX),-99.*np.ones(numX)
    r,i,z,redshift,q=crs['magR'],crs['magI'],crs['magZ'],crs['z'],crs['Q']
    rerr,ierr,zerr=np.zeros(len(r)),np.zeros(len(i)),np.zeros(len(i))    
    allsize,targsize,specsize,starsize=4,12,16,10
    rerrorig,ierrorig,zerrorig=np.copy(rerr),np.copy(ierr),np.copy(zerr)
    gcut=np.where((i<=icut)&(q>2.5))[0]
    gstar=np.where((i<=icut)&(q==-1))[0]
    gbadspec=np.where((qcur>-1)&(qcur<2.5))[0]
    gcuttarg=np.where((i<=icut))[0]
    gpcut=np.where(crp['magI']<=icut)[0]
    fig.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    ax=fig.add_subplot(1,1,1)
    ax.scatter(crp['magI'][gpcut],crp['magR'][gpcut]-crp['magI'][gpcut],color='k',s=allsize)
    ax.scatter(i[gcuttarg],r[gcuttarg]-i[gcuttarg],marker='d',s=targsize,color='green')
    ax.scatter(i[gstar],r[gstar]-i[gstar],marker='s',s=specsize,color='orange')
    ax.scatter(i[gcut],r[gcut]-i[gcut],marker='s',s=specsize,color='r')
    ax.set_xlabel("i'")
    ax.set_ylabel("r' - i'")
    ax.set_title(field)
    plt.xlim(18,24)
    plt.ylim(-0.5,2)
    xlim=plt.xlim()
    ylim=plt.ylim()
    fig.savefig(psfpdf,format='pdf')

    gcut=np.where((z<=zcut)&(q>2.5))[0]
    gcuttarg=np.where((z<=zcut))[0]
    gpcut=np.where(crp['magZ']<=zcut)[0]
    fig.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    ax=fig.add_subplot(1,1,1)
    ax.scatter(crp['magZ'][gpcut],crp['magI'][gpcut]-crp['magZ'][gpcut],color='k',s=allsize)
    ax.scatter(z[gcuttarg],i[gcuttarg]-z[gcuttarg],marker='d',s=targsize,color='green')
    ax.scatter(z[gcut],i[gcut]-z[gcut],marker='s',s=specsize,color='r')
    ax.set_xlabel("z'")
    ax.set_ylabel("i' - z'")
    ax.set_title(field)
    xlim=plt.xlim()
    ylim=plt.ylim()
    plt.xlim(18,24)
    plt.ylim(-0.5,2)

    fig.savefig(psfpdf,format='pdf')
psfpdf.close()
