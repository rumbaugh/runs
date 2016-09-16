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
    for j in range(0,len(mras)):
        gz=np.where((crs['ID']==crm['optID1'][j]))[0]
        if field=='cl1604':
            if usedACS[j]: gz=np.where((crs['ACS_ID']==crm['optID1'][j]))[0]
            if len(gz)==0:
                try:
                    if field=='rxj1757':
                        gz=np.where(crs['ID']=='F%05i'%(int(crm['optID1'][j])-1))[0]
                    else:
                        gz=np.where(crs['ID']=='F%05i'%int(crm['optID1'][j]))[0]
                except:
                    pass
        if field[:6]=='cl1324':
            gtmp=np.where((np.abs(mras[j]-crs['ra'])/np.cos(mdecs[j])<stol)&(np.abs(mdecs[j]-crs['dec'])<stol))[0]
            print len(gtmp)
            if len(gtmp)!=0: 
                disttmp=SphDist(mras[j],mdecs[j],crs['ra'][gtmp],crs['dec'][gtmp])
                gas=np.argsort(disttmp)
                gz=gtmp[gas[:1]]
        if nummatch[j]<1: gz=np.zeros(0)
        if (((field=='cl1324_southno')|(field=='cl1604no'))&(len(gz)==0)):
            gtmp=np.where((np.abs(mras2[j]-crs['ra'])/np.cos(mdecs2[j])<stol)&(np.abs(mdecs2[j]-crs['dec'])<stol))[0]
            if ((len(gtmp)!=0)&(nummatch2[j]>0)): 
                disttmp=SphDist(mras2[j],mdecs2[j],crs['ra'][gtmp],crs['dec'][gtmp])
                gas=np.argsort(disttmp)
                gz=gtmp[gas[:1]]
        if ((field=='cl1604')&(len(gz)==0)):
            gtmp=np.where((np.abs(mras[j]-crs['ra'])/np.cos(mdecs[j])<stol)&(np.abs(mdecs[j]-crs['dec'])<stol))[0]
            if ((len(gtmp)!=0)&(nummatch[j]>0)): 
                disttmp=SphDist(mras[j],mdecs[j],crs['ra'][gtmp],crs['dec'][gtmp])
                gas=np.argsort(disttmp)
                gz=gtmp[gas[:1]]
        if ((field=='cl1604no')&(len(gz)==0)):
            gtmp=np.where((np.abs(mras4[j]-crs['ra'])/np.cos(mdecs4[j])<stol)&(np.abs(mdecs4[j]-crs['dec'])<stol))[0]
            if ((len(gtmp)!=0)&(nummatch4[j]>0)): 
                disttmp=SphDist(mras4[j],mdecs4[j],crs['ra'][gtmp],crs['dec'][gtmp])
                gas=np.argsort(disttmp)
                gz=gtmp[gas[:1]]
        if len(gz)>0:
            if len(gz)>1: 
                print 'More than 1 entry for %s matched to %s - %s: '%(crm['optID1'][j],field,crm['indX'][j])
                print crs['z'][gz]
                zcur[j],magrcur[j],magicur[j],magzcur[j],zerrcur[j],qcur[j]=crs['z'][gz[0]],crs['magR'][gz[0]],crs['magI'][gz[0]],crs['magZ'][gz[0]],crs['zerr'][gz[0]],crs['Q'][gz[0]]
            else:
                zcur[j],magrcur[j],magicur[j],magzcur[j],zerrcur[j],qcur[j]=crs['z'][gz[0]],crs['magR'][gz[0]],crs['magI'][gz[0]],crs['magZ'][gz[0]],crs['zerr'][gz[0]],crs['Q'][gz[0]]



        gp=np.where((crp['ID']==crm['optID1'][j]))[0]
        if field=='cl1604':
            if usedACS[j]: gp=np.where((crp['ACS_ID']==crm['optID1'][j]))[0]
        if len(gp)==0:
            try:
                if field=='rxj1757':
                    gp=np.where(crp['ID']=='F%05i'%(int(crm['optID1'][j])-1))[0]
                else:
                    gp=np.where(crp['ID']=='F%05i'%int(crm['optID1'][j]))[0]
            except:
                pass
        if field[:6]=='cl1324':
            gtmp=np.where((np.abs(mras[j]-crp['ra'])/np.cos(mdecs[j])<stol)&(np.abs(mdecs[j]-crp['dec'])<stol))[0]
            print len(gtmp)
            if len(gtmp)!=0: 
                disttmp=SphDist(mras[j],mdecs[j],crp['ra'][gtmp],crp['dec'][gtmp])
                gas=np.argsort(disttmp)
                gp=gtmp[gas[:1]]
        if nummatch[j]<1: gp=np.zeros(0)
        if (((field=='cl1324_southno')|(field=='cl1604no'))&(len(gp)==0)):
            gtmp=np.where((np.abs(mras2[j]-crp['ra'])/np.cos(mdecs2[j])<stol)&(np.abs(mdecs2[j]-crp['dec'])<stol))[0]
            if ((len(gtmp)!=0)&(nummatch2[j]>0)): 
                disttmp=SphDist(mras2[j],mdecs2[j],crp['ra'][gtmp],crp['dec'][gtmp])
                gas=np.argsort(disttmp)
                gp=gtmp[gas[:1]]
        if ((field=='cl1604')&(len(gp)==0)):
            gtmp=np.where((np.abs(mras[j]-crp['ra'])/np.cos(mdecs[j])<stol)&(np.abs(mdecs[j]-crp['dec'])<stol))[0]
            if ((len(gtmp)!=0)&(nummatch[j]>0)): 
                disttmp=SphDist(mras[j],mdecs[j],crp['ra'][gtmp],crp['dec'][gtmp])
                gas=np.argsort(disttmp)
                gp=gtmp[gas[:1]]
        if ((field=='cl1604no')&(len(gp)==0)):
            gtmp=np.where((np.abs(mras4[j]-crp['ra'])/np.cos(mdecs4[j])<stol)&(np.abs(mdecs4[j]-crp['dec'])<stol))[0]
            if ((len(gtmp)!=0)&(nummatch4[j]>0)): 
                disttmp=SphDist(mras4[j],mdecs4[j],crp['ra'][gtmp],crp['dec'][gtmp])
                gas=np.argsort(disttmp)
                gp=gtmp[gas[:1]]
        if len(gp)>0:
            if len(gp)>1: 
                print 'More than 1 entry for %s matched to %s - %s: '%(crm['optID1'][j],field,crm['indX'][j])
                print crp['z'][gp]
                magrcurp[j],magicurp[j],magzcurp[j]=crp['magR'][gp[0]],crp['magI'][gp[0]],crp['magZ'][gp[0]]
            else:
                magrcurp[j],magicurp[j],magzcurp[j]=crp['magR'][gp[0]],crp['magI'][gp[0]],crp['magZ'][gp[0]]

        for ipr in range(0,np.shape(crs)[0]):
            gp=np.where(((np.abs(crs['ra'][ipr]-crp['ra'])<0.2/3600)&(np.abs(crs['dec'][ipr]-crp['dec'])<0.2/3600)&(np.abs(r[ipr]-crp['magR'])<0.1)&(np.abs(i[ipr]-crp['magI'])<0.1)))[0]
            if len(gp)==0:
                rerr[ipr],ierr[ipr]=99,99
            else:
                gp=gp[0]
                rerr[ipr],ierr[ipr],zerr[ipr]=crp['dmagR'][gp],crp['dmagI'][gp],crp['dmagZ'][gp]
    
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
    ax.scatter(magicurp,magrcurp-magicurp,color='green',marker='*',s=starsize)
    ax.scatter(magicurp[gbadspec],magrcurp[gbadspec]-magicurp[gbadspec],color='gold',marker='*',s=starsize)
    ax.scatter(i[gcuttarg],r[gcuttarg]-i[gcuttarg],marker='d',s=targsize,color='green')
    ax.scatter(i[gstar],r[gstar]-i[gstar],marker='s',s=specsize,color='orange')
    ax.scatter(i[gcut],r[gcut]-i[gcut],marker='s',s=specsize,color='r')
    ax.set_xlabel("i'")
    ax.set_ylabel("r' - i'")
    ax.set_title(field)
    plt.xlim(18,24.5)
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
    plt.xlim(18,24.5)
    plt.ylim(-0.5,2)

    fig.savefig(psfpdf,format='pdf')
psfpdf.close()
