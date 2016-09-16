execfile('/home/rumbaugh/git/ORELSE/python/Catalog Matching/optical_matching.py')
ldate='1.19.16'
date='4.21.16'
reps=10000

obsdict={'RCS0224-0002': {'obsID': '3181+4987','photcatname': 'rcs0224'},'CL 0848.6+4453': {'obsID': '927+1708','photcatname': 'cl0849'},'RX J0910+5422': {'obsID': '2227+2452','photcatname': 'cl0910'},'RX J105343+5735': {'obsID': '4936','photcatname': 'rxj1053'},'V 1221+4918': {'obsID': '1662','photcatname': 'rxj1221'},'RX J1350.0+6007': {'obsID': '2229','photcatname': 'cl1350'},'RX J1716.9+6708': {'obsID': '548','photcatname': 'rxj1716'}}

cr_aim=np.loadtxt('/home/rumbaugh/Chandra/aimpnts.dat',dtype={'names':('ID','RA','DEC'),'formats':('|S16','f8','f8')})

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053","cl1324_north","cl1324_south"])

refdir='/home/rumbaugh/git/ORELSE/Catalogs/tomczak_catalogs'
reffile_dict={"cl0023":'sg0023+0423_v0.1.9','cl1604':'sc1604_v0.0.3','rxj1757':'nep200_v0.0.4','rxj1821':'nep5281_v0.0.1','rxj1716':'rxj1716+6708_v0.0.7','rxj0910':'cl0910+5422_v0.0.3','cl1324':'sc1324_v0.0.2'}

rfmt=('i8',)
for k in range(0,26):rfmt=rfmt+('f8',)
refdict={'names':('ID','z_spec','ra','dec','magaper_B','erraper_B','magaper_V','erraper_V','magaper_r','erraper_r','magaper_i','erraper_i','magaper_z','erraper_z','magaper_J','erraper_J','magaper_K','erraper_K','apercorr','weight_B','weight_V','weight_r','weight_i','weight_z','weight_J','weight_K','wmin'),'formats':rfmt}
for field in ['cl1324']:
    refcat='%s/%s/%s.mag.gz'%(refdir,reffile_dict[field],reffile_dict[field])
    crtmp=np.loadtxt(refcat,dtype=refdict)
    outtmp=np.zeros((np.shape(crtmp)[0],4))
    outtmp[:,3],outtmp[:,0],outtmp[:,1],outtmp[:,2]=crtmp['ID'],crtmp['ra'],crtmp['dec'],crtmp['magaper_i']+crtmp['apercorr']
    np.savetxt('tmp.dat',outtmp,fmt='%f %f %f %i')

    catin='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_xray_phot.%s.dat'%(field,field,field,ldate)
    outcat='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_optmatch_photz.%s.dat'%(field,field,field,date)
    outreg='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_optmatch_photz.%s.reg'%(field,field,field,date)
    g=np.where(cr_aim['ID']==field)[0][0]
    raaim,decaim=cr_aim['RA'][g],cr_aim['DEC'][g]
    #MatchCat(catin,refcat,outcat,outreg,raaim,decaim,ref_load_dict=refdict)

    load_dict={'names':('raX','decX','netcnts_corrX_soft','netcnts_corrX_hard','netcnts_corrX_full'),'formats':('f8','f8','f8','f8','f8')}
    MatchCat(catin,'tmp.dat',outcat,outreg,raaim,decaim,setup='xray',load_dict=load_dict,minsrch=1.5,useConcaveHull=True,reps=reps,usesig=False)
