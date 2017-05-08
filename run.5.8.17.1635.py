import numpy as np
ntrials=10000000
buffcrs={}
for buff in [100,300,600]:
    buffcrs[buff]=np.loadtxt('/home/rumbaugh/mock_EVQs.buff_%i.trials_%i.5.6.17.dat'%(buff,ntrials),dtype={'names':('baseline_RFredshift','anchor_epoch','second_epoch','detected','firstspec','secondspec','lowepoch','CLQ_detected'),'formats':('|S24','f8','f8','i8','f8','f8','i8','i8')})
    outcr=np.zeros((ntrials,),dtype={'names':('a','b','c'),'formats':('|S24','i8','i8')})
    outcr['a'],outcr['b'],outcr['c']=buffcrs[buff]['baseline_RFredshift'],987654321099,987654321098
    np.savetxt('/home/rumbaugh/mock_EVQs.buff_%i.trials_%i.baseline.redshift.5.6.17.dat'%(buff,ntrials),outcr,fmt='%s.%i.%i')
