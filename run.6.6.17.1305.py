import numpy as np
from qso_fit_fix import qso_fit
import matplotlib.pyplot as plt
import pydl

mcdict={'names':('DBID','RA','DEC','SDR5ID','Mi','Micorr','redshift','massBH','Lbol','u','g','r','i','z','Au'),'formats':('i8','f8','f8','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')}
delims=(8,11,11,6,8,8,7,6,7,7,7,7,7,7,7)
crmc=np.genfromtxt('/home/rumbaugh/macleodQSOs/DB_QSO_S82.dat',dtype=mcdict)#,delimiter=delims)


fname='/home/rumbaugh/master_QSO_S82.dat'
mdict={'names':('DR5ID','RA','DEC','Redshift','umag','umagerr','gmag','gmagerr','rmag','rmagerr','imag','imagerr','zmag','zmagerr','Au','lohHI','20mag','F-SN','S-Fsep','F1Flag','F2Flag','logX','X-SN','S-XSep','Jmag','Jmagerr','Hmag','Hmagerr','Kmag','Kmagerr','S-2Sep','iMag','D(g-i)','Morph','SPFlag','SMFlag','UTSFlag','B-TSFlag','Blowz','Bhiz','BFFlag','BRFlag','BSFlag','B-*Flag','BGFlag','RNum','PMJD','SMJD','SPNum','SFNum','rerun','CCol','Frame','ONum','TTsFlag','Tlowz','Thiz','TFFlag','TRFlag','TSFlag','T-*Flag','TGFlag','T-umag','T-umagerr','T-gmag','T-gmagerr','T-rmag','T-rmagerr','T-imag','T-imagerr','T-zmag','T-zmagerr','SpOID','OName'),'formats':('|S20','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','i8','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','i8','|S28')}
delims=(19,11,11,7,7,6,7,6,7,6,7,6,7,6,7,7,7,8,7,3,3,8,7,7,7,6,7,6,7,6,7,8,7,3,3,3,3,12,3,3,3,3,3,3,3,6,6,6,5,5,4,3,5,5,12,3,3,3,3,3,3,3,7,6,7,6,7,6,7,6,7,6,21,26)
cr82m=np.genfromtxt(fname,dtype=mdict,delimiter=delims)

drwname='/home/rumbaugh/s82drw_g.dat'
drwdict={'names':('SDR5ID','ra','dec','redshift','M_i','mass_BH','chi2_pdf','ltau','lsig','ltau_lim_lo','ltau_lim_hi','lsig_lim_lo','lsig_lim_hi','edge_flag','Plike','Pnoise','Pinf','mu','npts'),'formats':('i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','i4','f8','f8','f8','f8','i8')}
crdrw=np.loadtxt(drwname,dtype=drwdict)
gdrw_dict={crdrw['SDR5ID'][x]: x for x in np.arange(len(crdrw))}

mcLCdict={'names':('MJD_u','mag_u','mag_u_err','MJD_g','mag_g','mag_g_err','MJD_r','mag_r','mag_r_err','MJD_i','mag_i','mag_i_err','MJD_z','mag_z','mag_z_err','ra','dec'),'formats':('f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')}

crd=np.loadtxt('/home/rumbaugh/var_database/Y3A1/DR7_full_magdiffs_wDBID.4.28.17.tab',dtype={'names':('RA','DEC','z','mjdlo','glo','siglo','flaglo','mjdhi','ghi','sighi','flaghi','RA_DES','DEC_DES','DBID'),'formats':('f8','f8','f8','f8','f8','f8','i8','f8','f8','f8','i8','f8','f8','|S24')})
drop=np.abs(crd['glo']-crd['ghi'])
gd=np.where(drop>1)[0]

sout=pydl.pydlutils.spheregroup.spherematch(crmc['RA'],crmc['DEC'],crd['RA'][gd],crd['DEC'][gd],0.3/3600)

maxind=100
taumc,sigmc,taumclerr,taumcherr,sigmclerr,sigmcherr,taub,sigb=np.zeros(maxind),np.zeros(maxind),np.zeros(maxind),np.zeros(maxind),np.zeros(maxind),np.zeros(maxind),np.zeros(maxind),np.zeros(maxind)

for i in np.arange(0,maxind):

    g0=np.where(crdrw['SDR5ID'][i]==crmc['SDR5ID'])[0][0]
    tau0,sig0=crdrw['ltau'][i],crdrw['lsig'][i]
    tau0lerr,tau0herr,sig0lerr,sig0herr=tau0-crdrw['ltau_lim_lo'][i],crdrw['ltau_lim_hi'][i]-tau0,sig0-crdrw['lsig_lim_lo'][i],crdrw['lsig_lim_hi'][i]-sig0
    taumc[i],sigmc[i],taumclerr[i],taumcherr[i],sigmclerr[i],sigmcherr[i]=tau0,sig0,tau0lerr,tau0herr,sig0lerr,sig0herr
    crlc=np.loadtxt('/home/rumbaugh/QSO_S82/%i'%(crmc['DBID'][g0]),dtype=mcLCdict)
    LCcr=np.zeros((len(crlc)*1,),dtype={'names':('DatabaseID','RA','DEC','MJD','BAND','MAG','MAGERR','FLAG'),'formats':('i8','f8','f8','f8','|S4','f8','f8','i8')})


    for b,ib in zip(['g'],np.arange(1)):
        LCcr['MJD'][ib*len(crlc):(ib+1)*len(crlc)],LCcr['BAND'][ib*len(crlc):(ib+1)*len(crlc)],LCcr['MAG'][ib*len(crlc):(ib+1)*len(crlc)],LCcr['MAGERR'][ib*len(crlc):(ib+1)*len(crlc)],LCcr['RA'][ib*len(crlc):(ib+1)*len(crlc)],LCcr['DEC'][ib*len(crlc):(ib+1)*len(crlc)]=crlc['MJD_%s'%b],b,crlc['mag_%s'%b],crlc['mag_%s_err'%b],crlc['ra'],crlc['dec']


    mjd,mag,magerr=LCcr['MJD'],LCcr['MAG'],LCcr['MAGERR']
    out=qso_fit(mjd,mag,magerr,return_model=True)
    ltau=out['ltau']
    lsig=np.log10((10**ltau)*0.5*10**out['lvar'])
    taub[i],sigb[i]=ltau,lsig
    print 'Butler model for %i\ntau=%f, var=%f, sig=%f'%(crmc['DBID'][i],out['ltau'],out['lvar'],lsig)
    print 'Macleod model for %i\ntau=%f -%f/+%f\nsigma=%f -%f/+%f'%(crmc['DBID'][i],tau0,tau0lerr,tau0herr,sig0,sig0lerr,sig0herr)

gevq=sout[0]

plt.figure(1)
plt.clf()
plt.scatter(taumc-taub,sigmc-sigb,s=1)
xlim=plt.xlim()
ylim=plt.ylim()
plt.plot([xlim[0],xlim[1]],[ylim[0],ylim[1]],lw=2,ls='dashed',color='k')
plt.errorbar(taumc-taub,sigmc-sigb,xerr=[taumclerr,taumcherr],yerr=[sigmclerr,sigmcherr],color='r',fmt='ro',lw=2,capsize=3,mew=1)
plt.errorbar(taumc[gevq]-taub[gevq],sigmc[gevq]-sigb[gevq],xerr=[taumclerr[gevq],taumcherr[gevq]],yerr=[sigmclerr[gevq],sigmcherr[gevq]],color='cyan',fmt='ro',lw=2,capsize=3,mew=1)
plt.xlim(0,xlim[1])
plt.ylim(-2,ylim[1])
plt.xlabel('log(tau)')
plt.ylabel('log(sigma)')
plt.savefig('/home/rumbaugh/DRW_butler_Macleod_comptest.png')
