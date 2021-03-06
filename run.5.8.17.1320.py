import numpy as np
ntrials=10000000
buffcrs={}
for buff in [100,300,600]:
    buffcrs[buff]=np.loadtxt('/home/rumbaugh/mock_EVQs.buff_%i.trials_%i.fixed.5.6.17.dat'%(buff,ntrials),dtype={'names':('baseline_RF','redshift','anchor_epoch','second_epoch','detected','firstspec','secondspec','lowepoch','CLQ_detected'),'formats':('f8','f8','f8','f8','i8','f8','f8','i8','i8')})
    print 'Buffer=%i:\nTotal CLQ detection fraction: %.5f'%(buff,np.count_nonzero(buffcrs[buff]['CLQ_detected'])*1./ntrials)
    for LB,UB in zip(np.arange(0,6000,1000),[1000,2000,3000,4000,5000,10000]):
        g=np.where((buffcrs[buff]['baseline_RF']>LB)&(buffcrs[buff]['baseline_RF']<UB))[0]
        print '%4i-%4i: %.5f'%(LB,UB,np.count_nonzero(buffcrs[buff]['CLQ_detected'][g])*1./len(g))
    print 'EVQ CLQ detection fraction: %.5f'%(np.count_nonzero(buffcrs[buff]['CLQ_detected'][buffcrs[buff]['detected']>0])*1./len(buffcrs[buff]['CLQ_detected'][buffcrs[buff]['detected']>0]))
    for LB,UB in zip(np.arange(0,6000,1000),[1000,2000,3000,4000,5000,10000]):
        g=np.where((buffcrs[buff]['detected']>0)&(buffcrs[buff]['baseline_RF']>LB)&(buffcrs[buff]['baseline_RF']<UB))[0]
        print '%4i-%4i: %.5f'%(LB,UB,np.count_nonzero(buffcrs[buff]['CLQ_detected'][g]>0)*1./len(g))

