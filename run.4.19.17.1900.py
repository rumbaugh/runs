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

redshifts=np.zeros(len(crdb))
for i in range(0,len(crdb)):
    g=np.where(crdb['SDSSNAME'][i]==bhname)[0][0]
    redshifts[i]=bhz[g]

yearlen=365.25
halfyear=yearlen/2

SDSSstart=51000
SDSSend=55000
DESstart=56500
DESend=DESstart+yearlen*3

randzs=np.random.choice(redshifts,ntrials)
baselines_rf=np.random.uniform(100,6000,ntrials)
baselines_obs=baselines_rf*(1+randzs)
anchor_epoch=np.random.uniform(SDSSstart,DESend,ntrials)-0.5*(1+randzs)
anchor_epoch2=anchor_epoch+buff*(1+randzs)
direction=np.random.choice(np.array([-1,1]),ntrials)
second_epoch=anchor_epoch+direction*baselines_obs
second_epoch2=second_epoch+buff*(1+randzs)
detected=np.ones(ntrials,dtype='bool')
detected[((second_epoch<SDSSstart)&(second_epoch2<SDSSstart))|((second_epoch>DESend)&(second_epoch2>DESend))|((second_epoch>SDSSend)&(second_epoch2>SDSSend)&(second_epoch<DESstart)&(second_epoch2<DESstart))|((anchor_epoch<SDSSstart)&(anchor_epoch2<SDSSstart))|((anchor_epoch>DESend)&(anchor_epoch2>DESend))|((anchor_epoch>SDSSend)&(anchor_epoch2>SDSSend)&(anchor_epoch<DESstart)&(anchor_epoch2<DESstart))]=0
detected[(0.5*(second_epoch+second_epoch)<SDSSstart)|(0.5*(second_epoch+second_epoch)>DESend)]=0
detected[((second_epoch>SDSSstart)&(second_epoch<SDSSend)&(second_epoch%yearlen>halfyear))&((second_epoch2>SDSSstart)&(second_epoch2<SDSSend)&(second_epoch2%yearlen>halfyear))&(buff*(1+randzs)<halfyear)]=0
detected[((anchor_epoch>SDSSstart)&(anchor_epoch<SDSSend)&(anchor_epoch%yearlen>halfyear))&((anchor_epoch2>SDSSstart)&(anchor_epoch2<SDSSend)&(anchor_epoch2%yearlen>halfyear))&(buff*(1+randzs)<halfyear)]=0
detected[((second_epoch>DESstart)&(second_epoch<DESend)&(second_epoch%yearlen>halfyear))&((second_epoch2>DESstart)&(second_epoch2<DESend)&(second_epoch2%yearlen>halfyear))&(buff*(1+randzs)<halfyear)]=0
detected[((anchor_epoch>DESstart)&(anchor_epoch<DESend)&(anchor_epoch%yearlen>halfyear))&((anchor_epoch2>DESstart)&(anchor_epoch2<DESend)&(anchor_epoch2%yearlen>halfyear))&(buff*(1+randzs)<halfyear)]=0

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
np.savetxt('/home/rumbaugh/DetFracRF.buff_%i.4.10.17.dat'%buff,outcr,fmt='%f %f',header='DetectionFraction Epoch')

outcr=np.zeros((len(detfrac_obs),),dtype={'names':('detfrac','detepoch'),'formats':('f8','f8')})
outcr['detfrac'],outcr['detepoch']=detfrac_obs,detepoch_obs
np.savetxt('/home/rumbaugh/DetFracObs.buff_%i.4.10.17.dat'%buff,outcr,fmt='%f %f',header='DetectionFraction Epoch')

execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')

matplotlib.rcParams['axes.linewidth']=4
matplotlib.rcParams['font.size']=18
fig=plt.figure(1)
fig.clf()
plt.clf()
plt.rc('axes',linewidth=2)
ax=fig.add_subplot(1,1,1)
ax2=ax.twinx()
ax.tick_params(which='major',length=12,width=3,labelsize=17)
ax.tick_params(which='minor',length=6,width=2,labelsize=17)
ax2.tick_params(which='major',length=12,width=3,labelsize=17)
ax2.tick_params(which='minor',length=6,width=2,labelsize=17)
a=ax.hist(baselines_rf,range=(0,6000),bins=24,color='k',edgecolor='k',facecolor='None',lw=2)
b=ax2.plot(np.sort(baselines_rf),(np.arange(len(baselines_rf))+1.)/len(baselines_rf),lw=2,color='r')
ax.set_xlabel('True Maximum Change Baseline (restframe days)')
ax.set_ylabel(r'N$_{obj}$')
ax2.set_ylabel('Cumulative Fraction')
#ax.axhline(lw=4,color='k')
#ax.axvline(lw=4,color='k')
#ax2.axhline(lw=4,color='k')
#ax2.axvline(lw=4,color='k')
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(3)
ax.set_xlim(0,6000)
ax2.set_xlim(0,6000)
ax2.set_ylim(0,1)
fig.savefig('/home/rumbaugh/var_database/Y3A1/plots/BaselineMC.MaxChangeBaselinePlot.TrueDistRF.buff_%i.4.10.17.png'%buff)

fig=plt.figure(1)
fig.clf()
plt.clf()
plt.rc('axes',linewidth=2)
ax=fig.add_subplot(1,1,1)
ax2=ax.twinx()
ax.tick_params(which='major',length=12,width=3,labelsize=17)
ax.tick_params(which='minor',length=6,width=2,labelsize=17)
ax2.tick_params(which='major',length=12,width=3,labelsize=17)
ax2.tick_params(which='minor',length=6,width=2,labelsize=17)
a=ax.hist(baselines_obs,range=(0,20000),bins=40,color='k',edgecolor='k',facecolor='None',lw=2)
b=ax2.plot(np.sort(baselines_obs),(np.arange(len(baselines_obs))+1.)/len(baselines_obs),lw=2,color='r')
ax.set_xlabel('True Maximum Change Baseline (observed days)')
ax.set_ylabel(r'N$_{obj}$')
ax2.set_ylabel('Cumulative Fraction')
#ax.axhline(lw=4,color='k')
#ax.axvline(lw=4,color='k')
#ax2.axhline(lw=4,color='k')
#ax2.axvline(lw=4,color='k')
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(3)
ax.set_xlim(0,20000)
ax2.set_xlim(0,20000)
ax2.set_ylim(0,1)
fig.savefig('/home/rumbaugh/var_database/Y3A1/plots/BaselineMC.MaxChangeBaselinePlot.TrueDistObs.buff_%i.4.10.17.png'%buff)


matplotlib.rcParams['axes.linewidth']=4
matplotlib.rcParams['font.size']=18
fig=plt.figure(1)
fig.clf()
plt.clf()
plt.rc('axes',linewidth=2)
ax=fig.add_subplot(1,1,1)
ax2=ax.twinx()
ax.tick_params(which='major',length=12,width=3,labelsize=17)
ax.tick_params(which='minor',length=6,width=2,labelsize=17)
ax2.tick_params(which='major',length=12,width=3,labelsize=17)
ax2.tick_params(which='minor',length=6,width=2,labelsize=17)
a=ax.hist(baselines_rf[detected],range=(0,6000),bins=24,color='k',edgecolor='k',facecolor='None',lw=2)
b=ax2.plot(np.sort(baselines_rf[detected]),(np.arange(len(baselines_rf[detected]))+1.)/len(baselines_rf[detected]),lw=2,color='r')
ax.set_xlabel('Maximum Change Baseline (restframe days)')
ax.set_ylabel(r'N$_{obj}$')
ax2.set_ylabel('Cumulative Fraction')
#ax.axhline(lw=4,color='k')
#ax.axvline(lw=4,color='k')
#ax2.axhline(lw=4,color='k')
#ax2.axvline(lw=4,color='k')
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(3)
ax.set_xlim(0,6000)
ax2.set_xlim(0,6000)
ax2.set_ylim(0,1)
fig.savefig('/home/rumbaugh/var_database/Y3A1/plots/BaselineMC.MaxChangeBaselinePlot.DetDistRF.buff_%i.4.10.17.png'%buff)

fig=plt.figure(1)
fig.clf()
plt.clf()
plt.rc('axes',linewidth=2)
ax=fig.add_subplot(1,1,1)
ax2=ax.twinx()
ax.tick_params(which='major',length=12,width=3,labelsize=17)
ax.tick_params(which='minor',length=6,width=2,labelsize=17)
ax2.tick_params(which='major',length=12,width=3,labelsize=17)
ax2.tick_params(which='minor',length=6,width=2,labelsize=17)
a=ax.hist(baselines_obs[detected],range=(0,6500),bins=40,color='k',edgecolor='k',facecolor='None',lw=2)
b=ax2.plot(np.sort(baselines_obs[detected]),(np.arange(len(baselines_obs[detected]))+1.)/len(baselines_obs[detected]),lw=2,color='r')
ax.set_xlabel('Maximum Change Baseline (observed days)')
ax.set_ylabel(r'N$_{obj}$')
ax2.set_ylabel('Cumulative Fraction')
#ax.axhline(lw=4,color='k')
#ax.axvline(lw=4,color='k')
#ax2.axhline(lw=4,color='k')
#ax2.axvline(lw=4,color='k')
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(3)
ax.set_xlim(0,6500)
ax2.set_xlim(0,6500)
ax2.set_ylim(0,1)
fig.savefig('/home/rumbaugh/var_database/Y3A1/plots/BaselineMC.MaxChangeBaselinePlot.DetDistObs.buff_%i.4.10.17.png'%buff)

fig=plt.figure(1)
fig.clf()
plt.clf()
plt.rc('axes',linewidth=2)
ax=fig.add_subplot(1,1,1)
#ax2=ax.twinx()
ax.tick_params(which='major',length=12,width=3,labelsize=17)
ax.tick_params(which='minor',length=6,width=2,labelsize=17)
#ax2.tick_params(which='major',length=12,width=3,labelsize=17)
#ax2.tick_params(which='minor',length=6,width=2,labelsize=17)
ax.plot(detepoch_rf,detfrac_rf,lw=2,color='r')
ax.set_xlabel('Maximum Change Baseline (observed days)')
ax.set_ylabel('Detection Fraction')
#ax.axhline(lw=4,color='k')
#ax.axvline(lw=4,color='k')
#ax2.axhline(lw=4,color='k')
#ax2.axvline(lw=4,color='k')
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(3)
ax.set_xlim(0,6500)
ax.set_ylim(0,1)
fig.savefig('/home/rumbaugh/var_database/Y3A1/plots/BaselineMC.MaxChangeBaselinePlot.DetFracRF.buff_%i.4.10.17.png'%buff)



fig=plt.figure(1)
fig.clf()
plt.clf()
plt.rc('axes',linewidth=2)
ax=fig.add_subplot(1,1,1)
#ax2=ax.twinx()
ax.tick_params(which='major',length=12,width=3,labelsize=17)
ax.tick_params(which='minor',length=6,width=2,labelsize=17)
#ax2.tick_params(which='major',length=12,width=3,labelsize=17)
#ax2.tick_params(which='minor',length=6,width=2,labelsize=17)
ax.plot(detepoch_obs,detfrac_obs,lw=2,color='r')
ax.set_xlabel('Maximum Change Baseline (observed days)')
ax.set_ylabel('Detection Fraction')
#ax.axhline(lw=4,color='k')
#ax.axvline(lw=4,color='k')
#ax2.axhline(lw=4,color='k')
#ax2.axvline(lw=4,color='k')
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(3)
ax.set_xlim(0,6500)
ax.set_ylim(0,1)
fig.savefig('/home/rumbaugh/var_database/Y3A1/plots/BaselineMC.MaxChangeBaselinePlot.DetFracObs.buff_%i.4.10.17.png'%buff)

