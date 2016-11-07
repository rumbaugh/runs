import numpy as np
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/pythonscripts/SDSS2DES_transform.py')
DBID=20458

WavLL,WavUL=300,1050

bands=np.array(['g','r','i','z'])
bcens={'u': 387.663943790537, 'g': 484.183358196563, 'r': 643.8534828217, 'i': 782.099282740933, 'z': 917.234266385718, 'Y': 987.780238651117}
cr=np.loadtxt('/home/rumbaugh/Downloads/VanderBerk_datafile1.txt',skiprows=23)

crdb=np.loadtxt('/home/rumbaugh/var_database/%i/LC.tab'%DBID,dtype={'names':('DBID','Survey','CoaddID','ObjID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','Flag'),'formats':('i8','|S6','i8','i8','f8','f8','f8','|S12','|S4','|S8','f8','f8','i8')},skiprows=1)

gDES,gSDSS=np.where(crdb['Survey']=='DES')[0],np.where(crdb['Survey']=='SDSS')[0]
u_sdss,g_sdss,r_sdss,i_sdss,z_sdss=crdb['MAG'][gSDSS][crdb['BAND'][gSDSS]=='u'],crdb['MAG'][gSDSS][crdb['BAND'][gSDSS]=='g'],crdb['MAG'][gSDSS][crdb['BAND'][gSDSS]=='r'],crdb['MAG'][gSDSS][crdb['BAND'][gSDSS]=='i'],crdb['MAG'][gSDSS][crdb['BAND'][gSDSS]=='z']
u_sdss,g_sdss,r_sdss,i_sdss,z_sdss,Y_sdss=SDSS2DES_mag(u_sdss,g_sdss,r_sdss,i_sdss,z_sdss)
magdict={'DES': {b: np.median(crdb['MAG'][gDES][crdb['BAND'][gDES]==b]) for b in bands}, 'SDSS': {'g': np.median(g_sdss),'r': np.median(r_sdss),'i': np.median(i_sdss),'z': np.median(z_sdss)}}

VBmax=np.max(cr[:,1][(cr[:,0]>WavLL)&(cr[:,0]<WavUL)])

fluxdict={surv: {b: 10**(magdict[surv][b]/-2.5) for b in bands} for surv in ['DES','SDSS']}

SDSSfluxmax,DESfluxmax=np.max(np.array([fluxdict['SDSS'][b] for b in bands])),np.max(np.array([fluxdict['DES'][b] for b in bands]))

relfluxdict={'DES': {b: fluxdict[surv][b]*VBmax/DESfluxmax},'SDSS': {b: fluxdict[surv][b]*VBmax/SDSSfluxmax}}

plt.figure(1)
plt.clf()
execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
plt.plot(cr[:,0],cr[:,1],color='k',lw=2)
for b in bands: 
    for surv,scol in zip(['DES','SDSS'],['r','b']):
        plt.scatter(np.array([bcens[b]]),np.array([refluxdict[surv][b]]),color=scol)
plt.xlabel('Wavelength (Angstroms)')
plt.ylabel('Flux (arbitrary units)')
plt.xlim(WavLL,WavUL)
plt.savefig('/home/rumbaugh/DBplots/SED_comp_20458.png')
