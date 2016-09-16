import numpy as np
import os

optmatchloaddict={'names':('indX','raX','decX','errX','nummatch','raopt1','decopt1','optID1','Popt1','likeopt1','raopt2','decopt2','optID2','Popt2','likeopt2','raopt3','decopt3','optID3','Popt3','likeopt3','probnone','ci','sigmax'),'formats':('i8','f8','f8','f8','i8','f8','f8','|S32','f8','f8','f8','f8','|S32','f8','f8','f8','f8','|S32','f8','f8','f8','i8','f8')}

specloaddict={'names':('ID','mask','slit','ra','dec','magR','magI','magZ','z','zerr','Q'),'formats':('|S16','|S16','|S8','f8','f8','f8','f8','f8','f8','f16','i8')}

band_dict={'soft': {'erange': '0.5-2.0','LB':0.5,'UB':2.0},'hard': {'erange': '2.0-8.0','LB':2.0,'UB':8.0},'full': {'erange': '0.5-8.0','LB':0.5,'UB':8.0}}

times=np.array([51730.160737324,125146.86866667,79084.755891771,61469.789688443,105735.52582365,58307.676632384,65311.025181476,14370.453707409,92237.849235535,88973.209339125])
nh = np.array([3.71,2.73,1.44,2.73,1.98,1.76,1.98,2.86,0.58,2.86])
obs = np.array(['548','927','1662','1708','2227','2229','2452','3181','4936','4987'])
obs_dict={obs[x]: {'exp': times[x], 'nh': nh[x]} for x in range(0,10)}
spec_dict= { \
'X1': {'file': 'FINAL.cl1322.lrisplusdeimos.jul2015.1322Ptmp.nodups.cat', 'loaddict': ''}, \
'X2': {'file': 'FINAL.nep5281.deimos.gioia.aug2013.nodups.cat', 'loaddict': ''}, \
'927+1708': {'file': 'FINAL.onlysemifinal.autocompile.blemaux.0849.feb2013.nodups.cat', 'loaddict': ''}, \
'X3': {'file': 'FINAL.semifinal.spectroscopic.autocompile.blemaux.XL005.targetsonly.apr2014.cat', 'loaddict': ''}, \
'X4': {'file': 'FINAL.SG0023.deimos.lris.feb2012.nodups.cat', 'loaddict': ''}, \
'X5': {'file': 'FINAL.spectra.Cl0023.edit.cat', 'loaddict': ''}, \
'X6': {'file': 'FINAL.spectra.sc1604.wcompletenessmasks.feb2012.nodups.cat', 'loaddict': ''}, \
'2229': {'file': 'FINAL.spectroscopic.autocompile.blemaux.1350.may2012.nodups.cat', 'loaddict': ''}, \
'X7': {'file': 'FINAL.spectroscopic.autocompile.blemaux.1429.may2015.nodups.cat', 'loaddict': ''}, \
'X8': {'file': 'FINAL.spectroscopic.autocompile.blemaux.N2560.apr2012.nodups.cat', 'loaddict': ''}, \
'3181+4987': {'file': 'FINAL.spectroscopic.autocompile.blemaux.RCS0224.apr2012.nodups.cat', 'loaddict': ''}, \
'1662': {'file': 'FINAL.spectroscopic.autocompile.blemaux.RXJ1221.may2015.wdups.cat', 'loaddict': ''}, \
'548': {'file': 'FINAL.spectroscopic.autocompile.blemaux.RXJ1716.jul2015.nodups.cat', 'loaddict': ''}, \
'2227+2452': {'file': 'FINAL.spectroscopic.autocompile.blemaux.sc0910.may2015.plusT08.nodups.cat', 'loaddict': ''}, \
'X9': {'file': 'FINAL.spectroscopic.autocompile.N200.blemaux.aug2013.nodups.cat', 'loaddict': ''}, \
'X10': {'file': 'spectroscopic.autocompile.blemaux.0943A.targetsonly.cat', 'loaddict': ''}, \
'X11': {'file': 'spectroscopic.autocompile.blemaux.1137.1137Ctmp.may2015.cat', 'loaddict': ''}, \
'4936': {'file': 'spectroscopic.autocompile.blemaux.RXJ1053.apr2015.BCDXtargetsonly.cat', 'loaddict': ''}}

fullcat=np.array([])

obj_dict=dict(zip(np.array(["548","1662","2229","4936","927+1708","2227+2452","3181+4987"]),np.zeros(7)))
names=obj_dict.keys()

#FILE=open('/home/rumbaugh/Chandra/full_Xray_catalog.dat','w')

for i in range(0,7): 
    strname=names[i]
    crm=np.loadtxt('/home/rumbaugh/Chandra/%s/optmatch.%s.dat'%(strname,strname),dtype=optmatchloaddict)
    crs=np.loadtxt(spec_dict[strname]['file'],dtype=specloaddict)
    crxp=np.loadtxt('/home/rumbaugh/Chandra/%s/photometry/%s.xray_phot.soft_hard_full.dat'%(strname,strname))
    numX=len(crm['indX'])
    #fullcattmp = np.append(np.reshape(crm['indX'],(numX,1)),crxp,axis=1)
    zcur,magrcur,magicur,magzcur,zerrcur,qcur=-99.*np.ones(numX),-99.*np.ones(numX),-99.*np.ones(numX),-99.*np.ones(numX),-99.*np.ones(numX),-99*np.ones(numX,dtype='i8')
    for j in range(0,len(crm['indX'])):
        gz=np.where(crs['ID']==crm['optID1'][j])[0]
        if len(gz)==0:
            gz=np.where(crs['ID']=='F'+crm['optID1'][j])[0]
        if len(gz)>0:
            if len(gz)>1: 
                print 'More than 1 entry for %s matched to %s - %s: '%(crm['optID1'][j],strname,crm['indX'][j])
                print crs['z'][gz]
                zcur[j],magrcur[j],magicur[j],magzcur[j],zerrcur[j],qcur[j]=crs['z'][gz[0]],crs['magR'][gz[0]],crs['magI'][gz[0]],crs['magZ'][gz[0]],crs['zerr'][gz[0]],crs['Q'][gz[0]]
            else:
                zcur[j],magrcur[j],magicur[j],magzcur[j],zerrcur[j],qcur[j]=crs['z'][gz[0]],crs['magR'][gz[0]],crs['magI'][gz[0]],crs['magZ'][gz[0]],crs['zerr'][gz[0]],crs['Q'][gz[0]]
    tmpObsID = np.array([strname for x in range(0,numX)])
    fullcattmp = np.concatenate((np.reshape(tmpObsID,(numX,1)),np.reshape(crm['indX'],(numX,1)),crxp,np.reshape(crm['errX'],(numX,1)),np.reshape(crm['nummatch'],(numX,1)),np.reshape(crm['raopt1'],(numX,1)),np.reshape(crm['decopt1'],(numX,1)),np.reshape(crm['optID1'],(numX,1)),np.reshape(crm['Popt1'],(numX,1)),np.reshape(crm['likeopt1'],(numX,1)),np.reshape(crm['raopt2'],(numX,1)),np.reshape(crm['decopt2'],(numX,1)),np.reshape(crm['optID2'],(numX,1)),np.reshape(crm['Popt2'],(numX,1)),np.reshape(crm['likeopt2'],(numX,1)),np.reshape(crm['raopt3'],(numX,1)),np.reshape(crm['decopt3'],(numX,1)),np.reshape(crm['optID3'],(numX,1)),np.reshape(crm['Popt3'],(numX,1)),np.reshape(crm['likeopt3'],(numX,1)),np.reshape(crm['probnone'],(numX,1)),np.reshape(crm['ci'],(numX,1)),np.reshape(zcur,(numX,1)),np.reshape(zerrcur,(numX,1)),np.reshape(magrcur,(numX,1)),np.reshape(magicur,(numX,1)),np.reshape(magzcur,(numX,1)),np.reshape(qcur,(numX,1))),axis=1)
    if i==0: 
        fullcat=np.copy(fullcattmp)
    else:
        fullcat=np.append(fullcat,fullcattmp,axis=0)
#fullcat=np.array(fullcat,dtype={'names':('obsID','xrayID','RAX','DecX','Xflux_soft','Xflux_hard','Xflux_full','Xnetcnts_soft','Xnetcnts_hard','Xnetcnts_full','Xsig_soft','Xsig_hard','Xsig_full','Xwd_sig_soft','Xwd_sig_hard','Xwd_sig_full','Xdetcode','Xerr','nummatch','raopt1','decopt1','optID1','Popt1','likeopt1','raopt2','decopt2','optID2','Popt2','likeopt2','raopt3','decopt3','optID3','Popt3','likeopt3','probnone','ci','redshift','zerr','magR','magI','magZ','Q'),'formats':('|S16','i8','f8','f8','e8','e8','e8','e8','e8','e8','f8','f8','f8','f8','f8','f8','i8','f8','2i8','f8','f8','|S16','f8','f8','f8','f8','|S16','f8','f8','f8','f8','|S16','f8','f8','f8','i8','f8','f8','f8','f8','e8','i8')})
#np.savetxt('/home/rumbaugh/Chandra/full_Xray_catalog.dat',fullcat,fmt='%10s %5i %f %f %E %E %E %E %E %E %f %f %f %f %f %f %i %8.5f %2i %9.5f %9.5f %15s %6.3f %7.1f %9.5f %9.5f %15s %6.3f %7.1f %9.5f %9.5f %15s %6.3f %7.1f %6.3f %3i %f %f %f %f %E %3i',header='# obsID xrayID RAX DecX Xflux_soft Xflux_hard Xflux_full Xnetcnts_soft Xnetcnts_hard Xnetcnts_full Xsig_soft Xsig_hard Xsig_full Xwd_sig_soft Xwd_sig_hard Xwd_sig_full Xdetcode Xerr nummatch raopt1 decopt1 optID1 Popt1 likeopt1 raopt2 decopt2 optID2 Popt2 likeopt2 raopt3 decopt3 optID3 Popt3 likeopt3 probnone ci redshift zerr magR magI magZ Q')
np.savetxt('/home/rumbaugh/Chandra/full_Xray_catalog.dat',fullcat,fmt='%10s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %15s %s %s %s %s %15s %s %s %s %s %15s %s %s %s %s %s %s %s %s %s %s',header='# obsID xrayID RAX DecX Xflux_soft Xflux_hard Xflux_full Xnetcnts_soft Xnetcnts_hard Xnetcnts_full Xsig_soft Xsig_hard Xsig_full Xwd_sig_soft Xwd_sig_hard Xwd_sig_full Xdetcode Xerr nummatch raopt1 decopt1 optID1 Popt1 likeopt1 raopt2 decopt2 optID2 Popt2 likeopt2 raopt3 decopt3 optID3 Popt3 likeopt3 probnone ci redshift zerr magR magI magZ Q')
