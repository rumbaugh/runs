import numpy as np
ntrials=10000000
buffcrs={}
for buff in [100,300,600]:
    buffcrs[buff]=np.loadtxt('/home/rumbaugh/mock_EVQs.buff_%i.trials_%i.5.6.17.dat'%(buff,ntrials),dtype={'names':('baseline_RFredshift','anchor_epoch','second_epoch','detected','firstspec','secondspec','lowepoch','CLQ_detected'),'formats':('|S24','f8','f8','i8','f8','f8','i8','i8')})
    buffcrs0[buff]=np.loadtxt('/home/rumbaugh/mock_EVQs.buff_%i.trials_%i.baseline.redshift.5.6.17.dat'%(buff,ntrials),dtype={'names':('baseline_RF','baselinedecredshift','redshiftdec'),'formats':('i8','i8','i8')},delimiter='.')
    baselinedec=np.int(np.floor(buffcrs0[buff]['baselinedecredshift']/10.))
    redshift=buffcrs0[buff]['baselinedecredshift']-baselindec
    print buff,len(buffcrs0[buff][buffcrs0[buff]['redshiftdec']==987654321099]),len(buffcrs0[buff][buffcrs0[buff]['redshiftdec']==987654321098])
    buffcrs0[buff]['redshiftdec'][buffcrs0[buff]['redshiftdec']==987654321099]=0
    outcr=np.zeros((ntrials,),dtype={'names':('baseline_RF','baseline_RFdec','redshift','redshiftdec','anchor_epoch','second_epoch','detected','firstspec','secondspec','lowepoch','CLQ_detected'),'formats':('i8','i8','i8','i8','f8','f8','i8','f8','f8','i8','i8')})
    outcr['baseline_RF'],outcr['baseline_RFdec'],outcr['redshift'],outcr['redshiftdec'],outcr['anchor_epoch'],outcr['second_epoch'],outcr['detected'],outcr['firstspec'],outcr['secondspec'],outcr['lowepoch'],outcr['CLQ_detected']=buffcrs0[buff]['baseline_RF'],baseline_RFdec,buffcrs0[buff]['redshift'],redshiftdec,buffcrs[buff]['anchor_epoch'],buffcrs[buff]['second_epoch'],buffcrs[buff]['detected'],buffcrs[buff]['firstspec'],buffcrs[buff]['secondspec'],buffcrs[buff]['lowepoch'],buffcrs[buff]['CLQ_detected']
    np.savetxt('/home/rumbaugh/mock_EVQs.buff_%i.trials_%i.fixed.5.6.17.dat'%(buff,ntrials),outcr,fmt='%i.%i %i.%i %f %i %f %f %i %i',header='baseline_RF redshift anchor_epoch second_epoch detected firstspec secondspec lowepoch CLQ_detected')
