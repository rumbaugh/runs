import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import healpy as hp
import pyfits as py
import pandas as pd
import time
st=time.time()
#nside=16384
nside=64
sdict={16:16,64:16}
mapshift=67.5
execfile('/home/rumbaugh/pythonscripts/aitoff.py')
execfile('/home/rumbaugh/pythonscripts/angconvert.py')

LSSTdf=pd.read_csv('/home/rumbaugh/LSST_bounds_radec.csv')
LSSTra,LSSTdec=LSSTdf.ra.values+180+67.5,LSSTdf.dec.values
LSSTdec=np.append(LSSTdec[LSSTra>360]-360,LSSTdec[LSSTra<360])
LSSTra=np.append(LSSTra[LSSTra>360]-360,LSSTra[LSSTra<360])

LSST_DDF_df=pd.read_csv('/home/rumbaugh/LSST_drillfields.csv')
DDFrad=1.75
MDSdf=pd.read_csv('/home/rumbaugh/PS_MDS.csv')
MDwid=np.sqrt(7)*0.5
SNdf=pd.read_csv('/home/rumbaugh/DES_SNfields.csv')
SNwid=np.sqrt(3)*0.5

xmult=1.25
desalpha=0.2
def covplot(ras,decs,pcol,nside=16):
    hpix=hp.ang2pix(nside,(90-decs)*np.pi/180.,ras*np.pi/180)
    b=np.bincount(hpix)
    hpixb=np.nonzero(b)
    b,hpixb=b[b>0],hpixb[0]
    HPang=np.array(hp.pix2ang(nside,hpixb))
    HPra,HPdec=HPang[1]*180/np.pi,90-HPang[0]*180/np.pi
    opacs=b*0.7/np.max(b)
    HPx,HPy=aitoff(HPra,HPdec)
    HPx*=xmult
    #for ra,dec,op in zip(HPx,HPy,opacs): ax.scatter(ra,dec,color=pcol,marker='h',s=sdict[nside],alpha=op)
    rgba_arr=matplotlib.colors.colorConverter.to_rgba_array(pcol)
    rgba_arr=np.repeat(rgba_arr,len(HPx),axis=0)
    rgba_arr[:,3]=opacs
    ax.scatter(HPx,HPy,color=rgba_arr,marker='h',s=sdict[nside])
    ax.set_xlabel('RA')
    ax.set_ylabel('Dec.')
    ax.set_xlim(-1.05*np.pi*xmult,1.05*np.pi*xmult)
    ax.set_ylim(-1.05*np.pi/2,1.05*np.pi/2)
def do_plots(ras,decs,pcol,nside=16):
    execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
    covplot(ras,decs,pcol,nside=nside)

try:
    cr2
except NameError:
    cr2=np.loadtxt('TID_randsamp2_rumbaugh.csv',dtype={'names':('ra','dec','id'),'formats':('f8','f8','i8')},delimiter=',',skiprows=1) 
try:
    cr3
except NameError:
    cr3=np.loadtxt('sdss-poss+healpix.txt',dtype={'names':('n','ra','dec','id'),'formats':('i8','f8','f8','i8')})
t1=time.time()
print 'Files loaded. Time Elapsed: {:.2f} seconds'.format(t1-st)
crs,cols,fnames=cr2,'magenta','/home/rumbaugh/coverage_plot.SDSS.png'
fig=plt.figure(1,figsize=(10,6))
plt.clf()
ax=fig.add_subplot(1,1,1)
ax.axis('off')
rastmp=crs['ra']+mapshift
rastmp[rastmp>360]-=360
do_plots(rastmp,crs['dec'],cols,nside)
t2=time.time()
print 'SDSS plotted. Time Elapsed: {:.2f} seconds'.format(t2-st)
rastmp=cr3['ra']+mapshift
rastmp[rastmp>360]-=360
do_plots(rastmp,cr3['dec'],'cyan',nside)
t3=time.time()
print 'POSS plotted. Time Elapsed: {:.2f} seconds'.format(t3-st)
cry=np.loadtxt('Y3A1_TILE_CORNERS.tab',usecols=(1,2,3,4,5,6,7,8),skiprows=1)
for i in range(0,np.shape(cry)[0]):
    ras,decs=cry[i][:4]+mapshift,cry[i][4:]
    ras[ras>360]-=360
    x,y=aitoff(ras,decs)
    x*=xmult
    if np.max(ras)-np.min(ras)>200:
        ghi,glo=np.where(ras>200)[0],np.where(ras<100)[0]
        rahi,ralo=np.copy(x),np.copy(x)
        dechi,declo=np.copy(y),np.copy(y)
        rahi[glo],dechi[glo]=aitoff(360,decs[glo])
        ralo[ghi],declo[glo]=aitoff(0,decs[ghi])
        dechi,declo=dechi*xmult,declo*xmult
        ax.fill(rahi,dechi,color='orange',alpha=desalpha,edgecolor='orange')
        ax.fill(ralo,declo,color='orange',alpha=desalpha,edgecolor='orange')
    else:
        ax.fill(x,y,color='orange',alpha=0.4,edgecolor='orange')
t4=time.time()
print 'Y3A1 plotted. Time Elapsed: {:.2f} seconds'.format(t4-st)


for imd in np.arange(0,len(LSST_DDF_df)):
    ra=hms2deg(LSST_DDF_df.RAh.iloc[imd],LSST_DDF_df.RAm.iloc[imd],LSST_DDF_df.RAs.iloc[imd])
    dec=dms2deg(LSST_DDF_df.DECd.iloc[imd],LSST_DDF_df.DECm.iloc[imd],LSST_DDF_df.DECs.iloc[imd])
    phidummy=np.linspace(0,3*np.pi,1000)
    decs=dec+DDFrad*np.sin(phidummy)
    ras=ra+DDFrad*np.cos(phidummy)+mapshift
    ras[ras>360]-=360
    x,y=aitoff(ras,decs)
    x*=xmult
    plt.plot(x,y,color='blue',lw=1)
    #ax.fill(x,y,color='blue',alpha=0.9,edgecolor='None')
tdd=time.time()
print 'DDF plotted. Time Elapsed: {:.2f} seconds'.format(tdd-st)

for imd in np.arange(0,len(MDSdf)):
    decs=MDSdf.DEC.iloc[imd]+np.array([-MDwid,MDwid,MDwid,-MDwid])
    ras=MDSdf.RA.iloc[imd]+np.array([-MDwid,-MDwid,MDwid,MDwid])/np.cos(decs*np.pi/180.)+mapshift
    ras[ras>360]-=360
    x,y=aitoff(ras,decs)
    x*=xmult
    ax.fill(x,y,color='green',alpha=0.9,edgecolor='None')
t5=time.time()
print 'MDF plotted. Time Elapsed: {:.2f} seconds'.format(t5-st)

for imd in np.arange(0,len(SNdf)):
    ra=hms2deg(SNdf.RAh.iloc[imd],SNdf.RAm.iloc[imd],SNdf.RAs.iloc[imd])
    dec=dms2deg(SNdf.DECd.iloc[imd],SNdf.DECm.iloc[imd],SNdf.DECs.iloc[imd])
    decs=dec+np.array([-SNwid,SNwid,SNwid,-SNwid])
    ras=ra+np.array([-SNwid,-SNwid,SNwid,SNwid])/np.cos(decs*np.pi/180.)+mapshift
    ras[ras>360]-=360
    x,y=aitoff(ras,decs)
    x*=xmult
    ax.fill(x,y,color='red',alpha=0.5,edgecolor='None')
tsn=time.time()
print 'SN fields plotted. Time Elapsed: {:.2f} seconds'.format(tsn-st)


LSSTx,LSSTy=aitoff(LSSTra,LSSTdec)
LSSTx*=xmult
plt.plot(LSSTx,LSSTy,color='blue',lw=2,ls='dotted')


xdummy,ydummy=aitoff(360.,np.linspace(0,90,1000))
xdummy*=xmult
ax.plot(xdummy,ydummy,color='k')
ax.plot(-xdummy,ydummy,color='k')
ax.plot(-xdummy,-ydummy,color='k')
ax.plot(xdummy,-ydummy,color='k')
for psi in np.arange(-75,90,15):
    xdummy,ydummy=aitoff(np.linspace(0,360,5000),psi)
    xdummy*=xmult
    ax.plot(xdummy,ydummy,color='k',alpha=0.3)
#PANSTARRS 3pi
psi=-30
xdummy,ydummy=aitoff(np.linspace(0,360,5000),psi)
xdummy*=xmult
ax.plot(xdummy,ydummy,color='green',lw=2,ls='dashed')
for lam in np.arange(22.5,360,45):
    xdummy,ydummy=aitoff(lam,np.linspace(-90,90,5000))
    xdummy*=xmult
    ax.plot(xdummy,ydummy,color='k',alpha=0.3)
for psi in np.arange(-60,90,30):
    x,y=aitoff(360,psi*1.05)
    x*=xmult
    if y<0:x*=1.02
    if y<-1./3.*np.pi:
        x*=1.04
        y*=1.02
    ax.text(x+np.pi*0.01,y,'%+i'%(psi)+r'$^\circ$',horizontalalignment='right',verticalalignment='center')
for lam,ra in zip(np.arange(22.5,360,45),np.arange(3,27,3)):
    x,y=aitoff(lam,5)
    x*=xmult
    ax.text(x,y,' %i'%((ra-6)%24)+r'$^h$',horizontalalignment='center',verticalalignment='center')

t6=time.time()
print 'Grid plotted. Time Elapsed: {:.2f} seconds'.format(t6-st)

s82ra,s82dec=np.array([-50,59,59,-50,-50])+90,np.array([-1.25,-1.25,1.25,1.25,-1.25])
s82x,s82y=aitoff(s82ra,s82dec)
s82x*=xmult
plt.plot(s82x,s82y,color='k',lw=2)

ldumx,ldumy=[-np.pi,-np.pi+0.001],[-np.pi/2,-np.pi/2.001]
lfillx,lfilly=[-np.pi+0.3,-np.pi+0.3,-np.pi-0.3,-np.pi-0.3],[-np.pi/2-0.3,-np.pi/2+0.3,-np.pi/2+0.3,-np.pi/2-0.3]

line3pi, =plt.plot(ldumx,ldumy,color='green',ls='dashed',lw=2,label=r'Pan-STARRS 3$\pi$')
linelsst, =plt.plot(ldumx,ldumy,color='blue',ls='dotted',lw=2,label='LSST')
lines82 =plt.scatter(ldumx,ldumy,s=40,marker='s',edgecolor='k',facecolor='None',lw=2,label='Stripe82')
leg1=plt.legend(handles=[line3pi,linelsst,lines82],loc='upper right',frameon=False,numpoints=2,scatterpoints=1,fontsize=12)
ax = plt.gca().add_artist(leg1)

liney3a1 =plt.scatter(ldumx,ldumy,s=40,color='orange',marker='s',edgecolor='None',label='DES Y3A1')
linesdss =plt.scatter(ldumx,ldumy,s=30,color='magenta',marker='h',alpha=0.75,edgecolor='None',label='SDSS')
lineposs =plt.scatter(ldumx,ldumy,s=30,color='cyan',marker='h',alpha=0.75,edgecolor='None',label='POSS')
leg2=plt.legend(handles=[liney3a1,linesdss,lineposs],loc='lower right',frameon=False,numpoints=2,scatterpoints=1,fontsize=12)

ax = plt.gca().add_artist(leg2)

lineDDF =plt.scatter(ldumx,ldumy,s=40,color='blue',alpha=0.9,facecolor='None',lw=1,edgecolor='blue',label='LSST Deep Drilling Fields')
lineMDF =plt.scatter(ldumx,ldumy,s=40,color='green',marker='s',alpha=0.9,edgecolor='None',label='Pan-STARRS1 MDF')
lineSNF =plt.scatter(ldumx,ldumy,s=40,color='red',marker='s',alpha=0.6,edgecolor='None',label='DES SN Fields')
leg3=plt.legend(handles=[lineDDF,lineMDF,lineSNF],loc='upper left',frameon=False,numpoints=2,scatterpoints=1,fontsize=12)

plt.fill(lfillx,lfilly,color='white',edgecolor='white',label=None)

xlim=plt.xlim()
plt.xlim(xlim[1],xlim[0])

fig.tight_layout()
fig.subplots_adjust(left=0.025,right=1,bottom=0,top=1)
plt.savefig('coverage_plot_full.shift.png')

tend=time.time()
print 'Plot saved. Time Elapsed: {:.2f} seconds'.format(tend-st)
