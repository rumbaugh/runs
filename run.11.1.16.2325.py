import numpy as np
import matplotlib.pyplot as plt

def plot_radec(DBID,savefile=None):
    cr=np.loadtxt('/home/rumbaugh/var_database/%i/LC.tab'%DBID,dtype={'names':('DBID','Survey','CoaddID','ObjID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','Flag'),'formats':('i8','|S6','i8','i8','f8','f8','f8','|S12','|S4','|S8','f8','f8','i8')},skiprows=1)
    gDES,gSDSS=np.where(cr['Survey']=='DES')[0],np.where(cr['Survey']=='SDSS')[0]
    raDES,decDES,mjdDES,raSDSS,decSDSS,mjdSDSS=cr['RA'][gDES],cr['DEC'][gDES],cr['MJD'][gDES],cr['RA'][gSDSS],cr['DEC'][gSDSS],cr['MJD'][gSDSS]
    raDES,decDES,raSDSS,decSDSS=raDES[np.argsort(mjdDES)],decDES[np.argsort(mjdDES)],raSDSS[np.argsort(mjdSDSS)],decSDSS[np.argsort(mjdSDSS)]
    raDEScen,decDEScen=np.mean(raDES),np.mean(decDES)
    raDES,decDES,raSDSS,decSDSS=np.append(raDES[0],raDES),np.append(decDES[0],decDES),np.append(raSDSS[0],raSDSS),np.append(decSDSS[0],decSDSS)
    plt.figure(1)
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_padecms(which='major',length=8,width=2,labelsize=14)
    plt.tick_padecms(which='minor',length=4,width=1.5,labelsize=14)
    plt.plot(raSDSS,decSDSS,lw=2,color='b')
    plt.plot(raDES,decDES,lw=2,color='r')
    plt.scatter(raSDSS,decSDSS,color='b')
    plt.scatter(raDES,decDES,color='r')
    thetadummy=np.linspace(0,2*np.pi,1000)
    radum,decdum=raDEScen+1./3600.*np.cos(thetadummy)*np.cos(decDEScen*np.pi/180.),decDEScen+1./3600.*np.sin(thetadummy)
    plt.plot(radum,decdum,lw=2,ls='dotted',color='k')
    plt.xlabel('RA')
    plt.ylabel('Dec')
    if savefile!=None: plt.savefig(savefile)
