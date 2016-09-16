import numpy as np
import pyfits as py
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/set_spec_dict.py')
execfile('/home/rumbaugh/SphDist.py')
namedict={'rxj1757':'RXJ1757','rxj1221':'RXJ1221','cl1324':'SC1324','rcs0224':'RCS0224','cl1350':'Cl1350','rxj1716':'RXJ1716','rxj1821':'RXJ1821','cl0023':'SG0023','cl1604':'SC1604','cl1137':'Cl1137','rxj0910':'RXJ0910','rxj1053':'RXJ1053','cl0849':'Cl0849'}
optmatchloaddict={'names':('indX','raX','decX','errX','nummatch','raopt1','decopt1','optID1','Popt1','likeopt1','raopt2','decopt2','optID2','Popt2','likeopt2','raopt3','decopt3','optID3','Popt3','likeopt3','probnone'),'formats':('i8','f8','f8','f8','i8','f8','f8','|S32','f8','f8','f8','f8','|S32','f8','f8','f8','f8','|S32','f8','f8','f8')}
cmloaddict={'names':('field','number','RA','Dec','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','specID','mask','slit','bcnts_soft','bcnts_hard','bcnts_full','sigs','sigh','sigf'),'formats':('|S24','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S48','|S24','|S24','f8','f8','f8','f8','f8','f8')}

cmcat='/home/rumbaugh/combined_match_catalog.6.21.16.dat'
crcm=np.loadtxt(cmcat,cmloaddict)
msig=np.zeros((len(crcm['RA']),3))
msig[:,0],msig[:,1],msig[:,2]=crcm['sigs'],crcm['sigh'],crcm['sigf']
msig=np.max(msig,axis=1)
ldate='1.19.16'
mtol=1.
targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","rxj1716","rxj1053"])
#FILE=open('/home/rumbaugh/spectab.ORELSE.7.27.16.txt','w')
for field in targets:
    scat='%s/%s'%(spec_dict['basepath'],spec_dict[field]['file'])
    if field=='cl1604':
        crs=np.loadtxt(scat,dtype=ACSspecloaddict)
    else:
        crs=np.loadtxt(scat,dtype=specloaddict)
    if field=='cl1324':
        matchcat1='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_optmatch_comb.%s.dat'%('cl1324_north','cl1324_north','cl1324_north',ldate)
        matchcat2='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_optmatch_comb.%s.dat'%('cl1324_south','cl1324_south','cl1324_south',ldate)
        crm1,crm2=np.loadtxt(matchcat1,dtype=optmatchloaddict),np.loadtxt(matchcat2,dtype=optmatchloaddict)
        crm=np.concatenate((crm1,crm2),axis=1)
        hdu2=py.open('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/SRCv1/%s_srclist_v1.fits'%('cl1324_south','cl1324_south','cl1324_south'))
        hdu1=py.open('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/SRCv1/%s_srclist_v1.fits'%('cl1324_north','cl1324_north','cl1324_north'))
        data1,data2=hdu1[1].data,hdu2[1].data
        data=np.concatenate((data1,data2))
    elif field=='cl1604':
        matchcat='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_optmatch_comb.%s.dat'%(field,field,field,ldate)
        ACSmatchcat='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_optmatch_ACS_comb.%s.dat'%(field,field,field,ldate)
        crmACS=np.loadtxt(ACSmatchcat,dtype=optmatchloaddict)
        ACSnumX=len(crmACS['indX'])
        ACSmras,ACSmdecs=crmACS['raopt1'],crmACS['decopt1']
        ACSnummatch=crmACS['nummatch']
        tmpcrm=crmACS
        #tmpcrm=np.loadtxt(matchcat,dtype=optmatchloaddict)
        #crm=np.copy(crmACS)
        crm=np.loadtxt(matchcat,dtype=optmatchloaddict)
        crm[((ACSnummatch>0)&(crm['nummatch']==0))]=tmpcrm[((ACSnummatch>0)&(tmpcrm['nummatch']==0))]
        hdu=py.open('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/SRCv1/%s_srclist_v1.fits'%(field,field,field))
        data=hdu[1].data
    else:
        matchcat='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_optmatch_comb.%s.dat'%(field,field,field,ldate)
        crm=np.loadtxt(matchcat,dtype=optmatchloaddict)
        hdu=py.open('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/SRCv1/%s_srclist_v1.fits'%(field,field,field))
        data=hdu[1].data
    gs=-1*np.ones(len(crm),dtype='i8')
    for i in range(0,len(crm)):
        gnoz=np.where((np.abs(crs['ra']-crm['raopt1'][i])*np.cos(crs['dec']*np.pi/180)<mtol/3600.)&(np.abs(crs['dec']-crm['decopt1'][i])<mtol/3600.))
        gnoz=gnoz[0]
        if len(gnoz)>0:
            tmpdist=SphDist(crs['ra'][gnoz],crs['dec'][gnoz],crm['raopt1'][i],crm['decopt1'][i])
            gs[i]=gnoz[np.argsort(tmpdist)[0]]
    sig=np.zeros((len(data),3))
    sig[:,0],sig[:,1],sig[:,2]=data['Soft_net_cts']/(1+np.sqrt(0.75+data['Soft_bkg_cts'])),data['Hard_net_cts']/(1+np.sqrt(0.75+data['Hard_bkg_cts'])),data['Full_net_cts']/(1+np.sqrt(0.75+data['Full_bkg_cts']))
    sig=np.max(sig,axis=1)
    numtargets=len(crs['Q'])
    numspec=len(crs['Q'][(crs['Q']==-1)|(crs['Q']>2.5)])
    numxray=(len(sig[sig>3]),len(sig[sig>2]))
    nummatch=(len(crm['nummatch'][(crm['nummatch']>0)&(sig>3)]),len(crm['nummatch'][(crm['nummatch']>0)&(sig>2)]))
    numattempt=(len(gs[(gs!=-1)&(sig>3)]),len(gs[(gs!=-1)&(sig>2)]))
    Qstmp=(crs['Q'][gs[(gs!=-1)&(sig>3)&(crm['nummatch']>0)]],crs['Q'][gs[(gs!=-1)&(sig>2)&(crm['nummatch']>0)]])
    numconf=(len(Qstmp[0][(Qstmp[0]==-1)|(Qstmp[0]>2)]),len(Qstmp[1][(Qstmp[1]==-1)|(Qstmp[1]>2)]))

    plt.figure(1)
    plt.clf()
    plt.scatter(crs['ra'],crs['dec'],s=1,color='k')
    plt.scatter(crs['ra'][crs['Q']>2.5],crs['dec'][crs['Q']>2.5],s=2,color='r')
    plt.scatter(crm['raopt1'][(crm['nummatch']>0)&(sig>3)],crm['decopt1'][(crm['nummatch']>0)&(sig>3)],marker='o',facecolor='None',edgecolor='cyan')
    if field=='cl1604':
        plt.xlim(241.25,240.85)
        plt.ylim(43.05,43.475)
    plt.savefig('/home/rumbaugh/Chandra/plots/specchk.%s.7.27.16.png'%field)

    #FILE.write('%12s & %4i & %4i & %3i(%i) & %3i(%i) & %3i(%i) & %3i(%i) \\\\\n'%(namedict[field],numtargets,numspec,numxray[0],numxray[1],nummatch[0],nummatch[1],numattempt[0],numattempt[1],numconf[0],numconf[1]))
#FILE.close()
    

    
