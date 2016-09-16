execfile('/home/rumbaugh/optical_matching.py')

obsdict={'RCS0224-0002': {'obsID': '3181+4987','photcatname': 'rcs0224'},'CL 0848.6+4453': {'obsID': '927+1708','photcatname': 'cl0849'},'RX J0910+5422': {'obsID': '2227+2452','photcatname': 'cl0910'},'RX J105343+5735': {'obsID': '4936','photcatname': 'rxj1053'},'V 1221+4918': {'obsID': '1662','photcatname': 'rxj1221'},'RX J1350.0+6007': {'obsID': '2229','photcatname': 'cl1350'},'RX J1716.9+6708': {'obsID': '548','photcatname': 'rxj1716'}}

cr_aim=np.loadtxt('/home/rumbaugh/Chandra/aimpnts.dat',dtype={'names':('ID','RA','DEC'),'formats':('|S16','f8','f8')})

for field in obsdict.keys():
    obsID,photcatname=obsdict[field]['obsID'],obsdict[field]['photcatname']
    refcat='/home/rumbaugh/Chandra/photcats/%s_rizdata.corr.gz'%photcatname
    catin='/home/rumbaugh/Chandra/%s/photometry/%s.xray_phot.soft_hard_full.dat'%(obsID,obsID)
    outcat='/home/rumbaugh/Chandra/%s/optmatch.%s.dat'%(obsID,obsID)
    outreg='/home/rumbaugh/Chandra/%s/optmatch.%s.reg'%(obsID,obsID)
    g=np.where(cr_aim['ID']==obsID)[0][0]
    raaim,decaim=cr_aim['RA'][g],cr_aim['DEC'][g]
    refdict={'names':('ID','dum1','dum2','ra','dec','magR','dmagR','magI','dmagI','magZ','dmagZ'),'formats':('|S8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')}
    MatchCat(catin,refcat,outcat,outreg,raaim,decaim,ref_load_dict=refdict)
