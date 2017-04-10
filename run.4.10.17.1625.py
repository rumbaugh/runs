execfile('/home/rumbaugh/pythonscripts/plot_DB_lightcurves.py')
import pyfits as py
import time

ntrials=100
clqsize=16

hdubh=py.open('/home/rumbaugh/dr7_bh_Nov19_2013.fits')
bhdata=hdubh[1].data
hduc=py.open('/home/rumbaugh/dr7_control.fits')
cdata=hduc[1].data
bhz,bhname,bhL=bhdata['REDSHIFT'],bhdata['SDSS_NAME'],bhdata['LOGLBOL']
cz,cname,cL=cdata['REDSHIFT'],cdata['SDSS_NAME'],cdata['LOGLBOL']

yearlen=365.25
halfyar=yearlen/2

SDSSstart=51000
SDSSend=55000
DESstart=56500
DESend=DESstart+yearlen*3

randzs=np.random.choice(bhz,ntrials)
baselines_rf=np.random.uniform(100,6000,ntrials)
baselines_obs=baselines_rf*(1+randzs)
anchor_epoch=np.uniform(SDSSstart,DESend,ntrials)
direction=np.random.choice(np.array([-1,1]),ntrials)
second_epoch=anchor_epoch+direction*baselines_obs
detected=np.ones(ntrials,dtype='bool')
detected[(second_epoch<SDSSstart)|(second_epoch>DESend)|((second_epoch>SDSSend)&(second_epoch<DESstart))|((anchor_epoch>SDSSend)&(anchor_epoch<DESstart))]=0
detected[(second_epoch>SDSSstart)&(second_epoch<SDSSend)&(second_epoch%yearlen>halfyear)]=0
detected[(anchor_epoch>SDSSstart)&(anchor_epoch<SDSSend)&(anchor_epoch%yearlen>halfyear)]=0
detected[(second_epoch>DESstart)&(second_epoch<DESend)&(second_epoch%yearlen>halfyear)]=0
detected[(anchor_epoch>DESstart)&(anchor_epoch<DESend)&(anchor_epoch%yearlen>halfyear)]=0

detfrac_rf,detfrac_obs=np.zeros(0),np.zeros(0)
detepoch_rf,detepoch_obs=np.zeros(0),np.zeros(0)
fracbinwid=100
for t in np.linspace(100,6000,100):
    g=np.where(np.abs(baseline_rf-t)<fracbinwid)[0]
    if len(g)>0:
        detfrac_rf,detepoch_rf=np.append(detfrac_rf,np.count_nonzero(detected[g])*1./len(g)),np.append(detepochrf_t)
for t in np.linspace(0,10000,100):
    g=np.where(np.abs(baseline_obs-t)<fracbinwid)[0]
    if len(g)>0:
        detfrac_obs,detepoch_obs=np.append(detfrac_obs,np.count_nonzero(detected[g])*1./len(g)),np.append(detepochrf_t)

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
b=ax2.plot(baselines_rf,(np.arange(len(cr))+1.)/len(cr),lw=2,color='r')
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
fig.savefig('/home/rumbaugh/var_database/Y3A1/plots/BaselineMC.MaxChangeBaselinePlot.TrueDistRF.4.10.17.png')

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
a=ax.hist(baselines_obs,range=(0,10000),bins=40,color='k',edgecolor='k',facecolor='None',lw=2)
b=ax2.plot(baselines_obs,(np.arange(len(cr))+1.)/len(cr),lw=2,color='r')
ax.set_xlabel('True Maximum Change Baseline (observed days)')
ax.set_ylabel(r'N$_{obj}$')
ax2.set_ylabel('Cumulative Fraction')
#ax.axhline(lw=4,color='k')
#ax.axvline(lw=4,color='k')
#ax2.axhline(lw=4,color='k')
#ax2.axvline(lw=4,color='k')
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(3)
ax.set_xlim(0,10000)
ax2.set_xlim(0,10000)
ax2.set_ylim(0,1)
fig.savefig('/home/rumbaugh/var_database/Y3A1/plots/BaselineMC.MaxChangeBaselinePlot.TrueDistObs.4.10.17.png')


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
b=ax2.plot(baselines_rf[detected],(np.arange(len(cr))+1.)/len(cr),lw=2,color='r')
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
fig.savefig('/home/rumbaugh/var_database/Y3A1/plots/BaselineMC.MaxChangeBaselinePlot.DetDistRF.4.10.17.png')

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
a=ax.hist(baselines_obs[detected],range=(0,10000),bins=40,color='k',edgecolor='k',facecolor='None',lw=2)
b=ax2.plot(baselines_obs[detected],(np.arange(len(cr))+1.)/len(cr),lw=2,color='r')
ax.set_xlabel('Maximum Change Baseline (observed days)')
ax.set_ylabel(r'N$_{obj}$')
ax2.set_ylabel('Cumulative Fraction')
#ax.axhline(lw=4,color='k')
#ax.axvline(lw=4,color='k')
#ax2.axhline(lw=4,color='k')
#ax2.axvline(lw=4,color='k')
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(3)
ax.set_xlim(0,10000)
ax2.set_xlim(0,10000)
ax2.set_ylim(0,1)
fig.savefig('/home/rumbaugh/var_database/Y3A1/plots/BaselineMC.MaxChangeBaselinePlot.DetDistObs.4.10.17.png')

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
ax.plot(detepoch_rf[detected],detfrac_rf[detected],lw=2,color='r')
ax.set_xlabel('Maximum Change Baseline (observed days)')
ax.set_ylabel('Detection Fraction')
#ax.axhline(lw=4,color='k')
#ax.axvline(lw=4,color='k')
#ax2.axhline(lw=4,color='k')
#ax2.axvline(lw=4,color='k')
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(3)
ax.set_xlim(0,10000)
ax.set_ylim(0,1)
fig.savefig('/home/rumbaugh/var_database/Y3A1/plots/BaselineMC.MaxChangeBaselinePlot.DetFracRF.4.10.17.png')



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
ax.plot(detepoch_obs[detected],detfrac_obs[detected],lw=2,color='r')
ax.set_xlabel('Maximum Change Baseline (observed days)')
ax.set_ylabel('Detection Fraction')
#ax.axhline(lw=4,color='k')
#ax.axvline(lw=4,color='k')
#ax2.axhline(lw=4,color='k')
#ax2.axvline(lw=4,color='k')
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(3)
ax.set_xlim(0,10000)
ax.set_ylim(0,1)
fig.savefig('/home/rumbaugh/var_database/Y3A1/plots/BaselineMC.MaxChangeBaselinePlot.DetFracObs.4.10.17.png')

