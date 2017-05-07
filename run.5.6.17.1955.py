execfile('/home/rumbaugh/pythonscripts/plot_DB_lightcurves.py')
import matplotlib
import pyfits as py
import time
try:
    ntrials
except NameError:
    ntrials=10000
try:
    buff
except NameError:
    buff=100
clqsize=16

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)
crdb=crdb[crdb['SDSSNAME']!='-1']
 
hdubh=py.open('/home/rumbaugh/dr7_bh_Nov19_2013.fits')
bhdata=hdubh[1].data
hduc=py.open('/home/rumbaugh/dr7_control.fits')
cdata=hduc[1].data
bhz,bhname,bhL=bhdata['REDSHIFT'],bhdata['SDSS_NAME'],bhdata['LOGLBOL']
cz,cname,cL=cdata['REDSHIFT'],cdata['SDSS_NAME'],cdata['LOGLBOL']

sn2z={bhname[x]:bhz[x] for x in np.arange(len(bhz))}
redshifts=np.array([sn2z[crdb['SDSSNAME'][x]] for x in np.arange(len(crdb))])

yearlen=365.25
halfyear=yearlen/2

SDSSstart=51000
SDSSend=55000
DESstart=56500
DESend=DESstart+yearlen*3
firstspec=np.zeros(ntrials)
observed=np.zeros(ntrials,dtype='bool')
cnt=0
while np.count_nonzero(observed)!=ntrials:
    g0=np.where(observed==False)[0]
    firstspec[g0]=np.random.uniform(SDSSstart,54000,len(g0))
    observed[g0][(firstspec[g0]-SDSSstart)%yearlen<halfyear]=True
    cnt+=1
    print cnt,len(g0)

secondspec=np.zeros(ntrials)
observed=np.zeros(ntrials,dtype='bool')
cnt=0
while np.count_nonzero(observed)!=ntrials:
    g0=np.where(observed==False)[0]
    secondspec[g0]=np.random.uniform(firstspec+1000,DESend-halfyear,len(g0))
    observed[g0][((secondspec[g0]<SDSSend)&((secondspec[g0]-SDSSstart)%yearlen<halfyear))|((secondspec[g0]>DESstart)&((secondspec[g0]-DESstart)%yearlen<halfyear))]=True
    cnt+=1
    print cnt,len(g0)

lowepoch=np.random.choice([0,1],ntrials,p=[0.34,0.66])
CLQdetected=np.zeros(ntrials,dtype='bool')    


randzs=np.random.choice(redshifts,ntrials)
baselines_rf=np.random.uniform(100,6000,ntrials)
baselines_obs=baselines_rf*(1+randzs)
anchor_epoch=np.random.uniform(SDSSstart,DESend,ntrials)-0.5*(1+randzs)
anchor_epoch2=anchor_epoch+buff*(1+randzs)
direction=np.random.choice(np.array([-1,1]),ntrials)
second_epoch=anchor_epoch+direction*baselines_obs
second_epoch2=second_epoch+buff*(1+randzs)

g0=np.where(lowepoch==0)[0]
CLQdetected[g0[(firstspec[g0]>anchor_epoch[g0])&(firstspec[g0]<anchor_epoch2[g0])]]=1
g1=np.where(lowepoch==1)[0]
CLQdetected[g1[(firstspec[g1]>second_epoch[g1])&(firstspec[g1]<second_epoch2[g1])]]=1

detected=np.ones(ntrials,dtype='bool')
detected[((second_epoch<SDSSstart)&(second_epoch2<SDSSstart))|((second_epoch>DESend)&(second_epoch2>DESend))|((second_epoch>SDSSend)&(second_epoch2>SDSSend)&(second_epoch<DESstart)&(second_epoch2<DESstart))|((anchor_epoch<SDSSstart)&(anchor_epoch2<SDSSstart))|((anchor_epoch>DESend)&(anchor_epoch2>DESend))|((anchor_epoch>SDSSend)&(anchor_epoch2>SDSSend)&(anchor_epoch<DESstart)&(anchor_epoch2<DESstart))]=0
detected[(0.5*(second_epoch+second_epoch2)<SDSSstart)|(0.5*(second_epoch+second_epoch2)>DESend)]=0
detected[((second_epoch>SDSSstart)&(second_epoch<SDSSend)&((second_epoch-SDSSstart)%yearlen>halfyear))&((second_epoch2>SDSSstart)&(second_epoch2<SDSSend)&((second_epoch2-SDSSstart)%yearlen>halfyear))&(buff*(1+randzs)<halfyear)]=0
detected[((anchor_epoch>SDSSstart)&(anchor_epoch<SDSSend)&((anchor_epoch-SDSSstart)%yearlen>halfyear))&((anchor_epoch2>SDSSstart)&(anchor_epoch2<SDSSend)&((anchor_epoch2-SDSSstart)%yearlen>halfyear))&(buff*(1+randzs)<halfyear)]=0
detected[((second_epoch>DESstart)&(second_epoch<DESend)&((second_epoch-DESstart)%yearlen>halfyear))&((second_epoch2>DESstart)&(second_epoch2<DESend)&((second_epoch2-DESstart)%yearlen>halfyear))&(buff*(1+randzs)<halfyear)]=0
detected[((anchor_epoch>DESstart)&(anchor_epoch<DESend)&((anchor_epoch-DESstart)%yearlen>halfyear))&((anchor_epoch2>DESstart)&(anchor_epoch2<DESend)&((anchor_epoch2-DESstart)%yearlen>halfyear))&(buff*(1+randzs)<halfyear)]=0

outcr=np.zeros((ntrials,),dtype={'names':('baseline_RF','redshift','anchor_epoch','second_epoch','detected','firstspec','secondspec','lowepoch','CLQ_detected'),'formats':('f8','f8','f8','f8','i8','f8','f8','i8','i8')})
outcr['baseline_RF'],outcr['redshift'],outcr['anchor_epoch'],outcr['second_epoch'],outcr['detected'],outcr['firstspec'],outcr['secondspec'],outcr['lowepoch'],outcr['CLQ_detected']=baselines_rf,randzs,0.5*(anchor_epoch+anchor_epoch2),0.5*(second_epoch+second_epoch2),detected,firstspec,secondspec,lowepoch,CLQdetected
np.savetxt('/home/rumbaugh/mock_EVQs.buff_%i.trials_%i.5.6.17.dat'%(buff,ntrials),outcr,fmt='%f%f %f %f %i %f %f %i %i',header='baseline_RF redshift anchor_epoch second_epoch detected firstspec secondspec lowepoch CLQ_detected')

detfrac_rf,detfrac_obs=np.zeros(0),np.zeros(0)
detepoch_rf,detepoch_obs=np.zeros(0),np.zeros(0)
try:
    fracbinwid
except NameError:
    fracbinwid=100
for t in np.arange(100,6000,10):
    g=np.where(np.abs(baselines_rf-t)<fracbinwid)[0]
    if len(g)>0:
        detfrac_rf,detepoch_rf=np.append(detfrac_rf,np.count_nonzero(detected[g])*1./len(g)),np.append(detepoch_rf,t)
for t in np.arange(0,20000,10):
    g=np.where(np.abs(baselines_obs-t)<fracbinwid)[0]
    if len(g)>0:
        detfrac_obs,detepoch_obs=np.append(detfrac_obs,np.count_nonzero(detected[g])*1./len(g)),np.append(detepoch_obs,t)
outcr=np.zeros((len(detfrac_rf),),dtype={'names':('detfrac','detepoch'),'formats':('f8','f8')})
outcr['detfrac'],outcr['detepoch']=detfrac_rf,detepoch_rf
np.savetxt('/home/rumbaugh/DetFracRF.buff_%i.5.6.17.dat'%buff,outcr,fmt='%f %f',header='DetectionFraction Epoch')

outcr=np.zeros((len(detfrac_obs),),dtype={'names':('detfrac','detepoch'),'formats':('f8','f8')})
outcr['detfrac'],outcr['detepoch']=detfrac_obs,detepoch_obs
np.savetxt('/home/rumbaugh/DetFracObs.buff_%i.5.6.17.dat'%buff,outcr,fmt='%f %f',header='DetectionFraction Epoch')

execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
