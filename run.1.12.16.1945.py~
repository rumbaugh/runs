execfile('/home/rumbaugh/git/ORELSE/Catalog Matching/optical_matching.py')

date='1.5.16'

obsdict={'RCS0224-0002': {'obsID': '3181+4987','photcatname': 'rcs0224'},'CL 0848.6+4453': {'obsID': '927+1708','photcatname': 'cl0849'},'RX J0910+5422': {'obsID': '2227+2452','photcatname': 'cl0910'},'RX J105343+5735': {'obsID': '4936','photcatname': 'rxj1053'},'V 1221+4918': {'obsID': '1662','photcatname': 'rxj1221'},'RX J1350.0+6007': {'obsID': '2229','photcatname': 'cl1350'},'RX J1716.9+6708': {'obsID': '548','photcatname': 'rxj1716'}}

cr_aim=np.loadtxt('/home/rumbaugh/Chandra/aimpnts.dat',dtype={'names':('ID','RA','DEC'),'formats':('|S16','f8','f8')})

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053","cl1324_north","cl1324_south"])

#for field in targets[8:-2]:
for field in ["rxj1053"]:
    refcat='/home/rumbaugh/Chandra/photcats/%s_rizdata.corr.gz'%field
    catin='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_xray_phot.dat'%(field,field,field)
    outcat='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_optmatch.%s.dat'%(field,field,field,date)
    outreg='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_optmatch.%s.reg'%(field,field,field,date)
    g=np.where(cr_aim['ID']==field)[0][0]
    raaim,decaim=cr_aim['RA'][g],cr_aim['DEC'][g]
    refdict={'names':('ID','dum1','dum2','ra','dec','magR','dmagR','magI','dmagI','magZ','dmagZ'),'formats':('|S64','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')}
    #MatchCat(catin,refcat,outcat,outreg,raaim,decaim,ref_load_dict=refdict)

    load_dict={'names':('raX','decX','netcnts_corrX_soft','netcnts_corrX_hard','netcnts_corrX_full'),'formats':('f8','f8','f8','f8','f8')}
    MatchCat(catin,refcat,outcat,outreg,raaim,decaim,setup='xray',load_dict=load_dict,ref_load_dict=refdict,minsrch=1.5,useConcaveHull=True,reps=10000,usesig=False)
