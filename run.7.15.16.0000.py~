import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

true_len,true_CKP_perc,ntrials,ndraw,nAGN,convfrac=1000,.25,10000,500,17,0.8

def CKPtest(obs_CKP_perc,ngals,nAGN,ntrials=10000,convfrac=0.5,true_len_fac=2):
    ndraw=ngals*(1-obs_CKP_perc)
    true_len=ndraw*true_len_fac
    true_CKP_perc=obs_CKP_perc/convfrac
    true_CKP=int(true_len*true_CKP_perc)
    a1=np.arange(0,true_len/2*5,5)
    a2=np.arange((true_len-true_CKP)/2*5,(true_len-true_CKP/2)*5,5)+1
    a=np.sort(np.append(a1,a2))
    a=np.append(np.zeros(int(true_len*(1-true_CKP_perc))),np.ones(int(0.5*true_len*true_CKP_perc)))

    CKPtests=np.zeros(ntrials)
    CKPfracs=np.zeros(ntrials)
    AGNtests=np.zeros(ntrials)
    for i in range(0,ntrials):
        atmp=np.sort(rand.choice(a,ndraw,replace=False))
        test=rand.rand(len(atmp[atmp==1]))
        nAGNtmp=len(test[test<convfrac])
        atmp=np.append(np.zeros(len(atmp)-nAGNtmp),np.ones(2*nAGNtmp))
        #mintmp=np.ones((ndraw,2))*99
        #mintmp[:-1,0],mintmp[1:,1]=atmp[1:]-atmp[:-1],atmp[1:]-atmp[:-1]
        #mintmp=np.min(mintmp,axis=1)
        #gkAGN=np.where(mintmp==1)[0]
        #dtmp=np.zeros(ndraw)
        #dtmp[gkAGN]=1
        #CKPtests[i]=2*np.sum(atmp[1:]-atmp[:-1]==1)
        AGNtmp=rand.choice(atmp,nAGN,replace=False)
        AGNtests[i]=np.sum(AGNtmp)
        CKPtests[i]=np.sum(atmp)
        CKPfracs[i]=np.sum(atmp)*1./len(atmp)
    plt.figure(1)
    plt.clf()
    plt.hist(CKPfracs,range=(0,0.45),bins=15)

    plt.figure(2)
    plt.clf()
    plt.hist(AGNtests,range=(0,15),bins=15)

    #print np.mean(CKPtests),np.median(CKPtests),np.std(CKPtests),0.5*(np.sort(CKPtests)[int(0.84*ntrials)]-np.sort(CKPtests)[int(0.16*ntrials)])
    #print np.mean(CKPfracs),np.median(CKPfracs),np.std(CKPfracs),0.5*(np.sort(CKPfracs)[int(0.84*ntrials)]-np.sort(CKPfracs)[int(0.16*ntrials)])
    #print np.mean(AGNtests),np.median(AGNtests),np.std(AGNtests),0.5*(np.sort(AGNtests)[int(0.84*ntrials)]-np.sort(AGNtests)[int(0.16*ntrials)])
    #print np.mean(AGNtests)/nAGN,np.median(AGNtests)/nAGN,np.std(AGNtests)/nAGN,0.5*(np.sort(AGNtests)[int(0.84*ntrials)]-np.sort(AGNtests)[int(0.16*ntrials)])/nAGN
    print 'Exp CKP Frac: %.4f +/- %.4f'%(np.median(CKPfracs),np.std(CKPfracs))
    print 'Exp AGN CKPs: %.4f +/- %.4f'%(np.median(AGNtests),np.std(AGNtests))
    print 'Exp AGN frac: %.4f +/- %.4f'%(np.median(AGNtests)/nAGN,np.std(AGNtests)/nAGN)
    return np.median(CKPfracs),np.std(CKPfracs),np.median(AGNtests),np.std(AGNtests),np.median(AGNtests)/nAGN,np.std(AGNtests)/nAGN

cr=np.loadtxt('/home/rumbaugh/Chandra/field_CKP_stat.dat',dtype={'names':('group','num_AGN_CKP','num_AGN','num_all_CKP','num_all'),'formats':('|S24','f8','f8','f8','f8')})

FILE=open('/home/rumbaugh/Chandra/field_CKP_stats_werr.dat','w')
FILE.write('# group num_AGN_CKP num_AGN num_all_CKP num_all AGN_CKP_err AGN_CKP_frac_err all_CKP_frac_err\n')

for i in range(0,len(cr['group'])):
    a,allerr,b,agnerr,c,agnfracerr=CKPtest(cr['num_all_CKP'][i]*1./cr['num_all'][i],cr['num_all'][i],cr['num_AGN'][i])
    FILE.write('%18s %i %2i %3i %4i %.4f %.4f %.4f\n'%(cr['group'][i],cr['num_AGN_CKP'][i],cr['num_AGN'][i],cr['num_all_CKP'][i],cr['num_all'][i],agnerr,agnfracerr,allerr))
FILE.close()

cr=np.loadtxt('/home/rumbaugh/Chandra/AGN_CKP_stat.dat',dtype={'names':('group','num_AGN_CKP','num_AGN','num_all'),'formats':('|S24','f8','f8','f8')})

FILE=open('/home/rumbaugh/Chandra/AGN_CKP_stats_werr.dat','w')
FILE.write('# field num_AGN_CKP num_AGN num_all AGN_CKP_err AGN_CKP_frac_err all_CKP_frac_err\n')

for i in range(0,len(cr['field'])):
    a,allerr,b,agnerr,c,agnfracerr=CKPtest(cr['num_all_CKP'][i]*1./cr['num_all'][i],cr['num_all'][i],cr['num_AGN'][i])
    FILE.write('%18s %i %2i %3i %.4f %.4f %.4f\n'%(cr['field'][i],cr['num_AGN_CKP'][i],cr['num_AGN'][i],cr['num_all'][i],agnerr,agnfracerr,allerr))
FILE.close()
