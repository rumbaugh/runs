import numpy as np
ntrials=10000000
buffcrs={}
for buff in [100,300,600]:
    buffcrs[buff]=np.loadtxt('/home/rumbaugh/mock_EVQs.buff_%i.trials_%i.5.6.17.dat'%(buff,ntrials),dtype={'names':('baseline_RFredshift','anchor_epoch','second_epoch','detected','firstspec','secondspec','lowepoch','CLQ_detected'),'formats':('|S24','f8','f8','i8','f8','f8','i8','i8')})
    print 'Buffer=%i:\nTotal CLQ detection fraction: %.5f\nEVQ CLQ detection fraction: %.5f'%(buff,np.count_nonzero(buffcrs[buff]['CLQ_detected'])*1./ntrials,np.count_nonzero(buffcrs[buff]['CLQ_detected'][buffcrs[buff]['detected']>0])*1./len(buffcrs[buff]['CLQ_detected'][buffcrs[buff]['detected']>0]))

