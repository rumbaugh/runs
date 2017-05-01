import numpy as np

mjdthresh=0.01

crybh=np.loadtxt('/home/rumbaugh/dr7_bh_lightcurve_entries_y3a1_wspread.tab',dtype={'names':('SDSSNAME','cid','mjd','ra','dec','imageid','ofilename','OBJECT_ID','mag','magerr','mag_auto','mag_auto_err','band','flags','flags_detmodel','flags_model','flags_weight','spread','spreaderr'),'formats':('|S24','i8','f8','f8','f8','i8','|S64','i8','f8','f8','f8','f8','|S12','i8','i8','i8','i8','f8','f8')},skiprows=1)
crybh=crybh[crybh['band']=='g']

cr=np.loadtxt('/home/rumbaugh/var_database/Y3A1/DR7_full_magdiffs_wDBID.4.28.17.tab',dtype={'names':('RA','DEC','z','mjdlo','glo','siglo','flaglo','mjdhi','ghi','sighi','flaghi','RA_DES','DEC_DES','DBID'),'formats':('f8','f8','f8','f8','f8','f8','i8','f8','f8','f8','i8','f8','f8','|S24')})
crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/database_index.dat',dtype={'names':('DBID','CID','thingid','sdr7id','MQrownum','SP_rownum','SDSSNAME'),'formats':('|S64','i8','i8','|S24','i8','i8','|S64')})
db2sn={crdb['DBID'][x]: crdb['SDSSNAME'][x] for x in np.arange(len(crdb))}
SNs=np.array([db2sn[cr['DBID'][x]] for x in np.arange(0,len(cr))])
spreadhi,spreadlo=np.zeros(len(cr)),np.zeros(len(cr))
spreaderrhi,spreaderrlo=np.zeros(len(cr)),np.zeros(len(cr))
magautohi,magautolo=np.zeros(len(cr)),np.zeros(len(cr))
magautoerrhi,magautoerrlo=np.zeros(len(cr)),np.zeros(len(cr))
for i in range(0,len(cr)):
    crlctmp=crybh[crybh['SDSSNAME']==SNs[i]]
    glo,ghi=np.where(np.abs(crlctmp['mjd']-cr['mjdlo'][i])<mjdthresh)[0],np.where(np.abs(crlctmp['mjd']-cr['mjdhi'][i])<mjdthresh)[0]
    if len(glo)>1:
        tdists=np.abs(crlctmp['mjd'][glo]-cr['mjdlo'][i])
        glo=glo[np.argsort(tdists)]
    if len(ghi)>1:
        tdists=np.abs(crlctmp['mjd'][ghi]-cr['mjdhi'][i])
        ghi=ghi[np.argsort(tdists)]
    if len(glo)>0:
        glo=glo[0]
        spreadlo[i]=crlctmp['spread'][glo]
        spreaderrlo[i]=crlctmp['spreaderr'][glo]
        magautolo[i]=crlctmp['mag_auto'][glo]
        magautoerrlo[i]=crlctmp['mag_auto_err'][glo]
    if len(ghi)>0:
        ghi=ghi[0]
        spreadhi[i]=crlctmp['spread'][ghi]
        spreaderrhi[i]=crlctmp['spreaderr'][ghi]
        magautohi[i]=crlctmp['mag_auto'][ghi]
        magautoerrhi[i]=crlctmp['mag_auto_err'][ghi]
outcr=np.zeros((len(spreadhi),8))
outcr[:,0],outcr[:,1],outcr[:,2],outcr[:,3],outcr[:,4],outcr[:,5],outcr[:,6],outcr[:,7]=spreadlo,spreadhi,spreaderrlo,spreaderrhi,magautolo,magautohi,magautoerrlo,magautoerrhi
np.savetxt('/home/rumbaugh/var_database/Y3A1/DR7.evq_spreads.4.30.17.dat',outcr,fmt='%f %f %f %f %f %f %f %f',header='spread_lo spread_hi spreaderr_lo spreaderr_hi magauto_lo magauto_hi magautoerr_lo magautoerr_hi')
    
