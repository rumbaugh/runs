import numpy as np
ntrials=10000000
buffcrs={}
for buff in [100,300,600]:
    buffcrs[buff]=np.loadtxt('/home/rumbaugh/mock_EVQs.buff_%i.trials_%i.5.6.17.dat'%(buff,ntrials),dtype={'names':('baseline_RFredshift','anchor_epoch','second_epoch','detected','firstspec','secondspec','lowepoch','CLQ_detected'),'formats':('|S24','f8','f8','i8','f8','f8','i8','i8')})
    np.savetxt('/home/rumbaugh/mock_EVQs.buff_%i.trials_%i.baseline.redshift.5.6.17.dat'%(buff,ntrials),buffcrs[buff]['baseline_RFredshift'],fmt='%s')
