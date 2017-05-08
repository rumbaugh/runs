import numpy as np
ntrials=10000000
buffcrs={}
for buff in [100,300,600]:
    buffcrs[buff]=np.loadtxt('/home/rumbaugh/mock_EVQs.buff_%i.trials_%i.fixed.5.6.17.dat'%(buff,ntrials),dtype={'names':('baseline_RF','redshift','anchor_epoch','second_epoch','detected','firstspec','secondspec','lowepoch','CLQ_detected'),'formats':('f8','f8','f8','f8','i8','f8','f8','i8','i8')})
    print 'Buffer=%i:\nTotal CLQ detection fraction: %.5f\n'%(buff,np.count_nonzero(buffcrs[buff]['CLQ_detected'])*1./ntrials)
    for LB,UB in zip(np.arange(0,6000,1000),[1000,2000,3000,4000,5000,10000]):
        g=np.where((buffcrs[buff]['baseline_
    print 'EVQ CLQ detection fraction: %.5f'%(np.count_nonzero(buffcrs[buff]['CLQ_detected'][buffcrs[buff]['detected']>0])*1./len(buffcrs[buff]['CLQ_detected'][buffcrs[buff]['detected']>0]))
