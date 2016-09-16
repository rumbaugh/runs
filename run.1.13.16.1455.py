import numpy as np
import os
import matplotlib.pyplot as plt
import pyfits as py
execfile('/home/rumbaugh/angconvert.py')
execfile('/home/rumbaugh/SphDist.py')
ldate='1.5.16'
date='1.13.16'

#outfile='/home/rumbaugh/combined_match_catalog.1.7.16.dat'
#FILE=open(outfile,'w')
#FILE.write('# field number RA Dec flux_soft flux_hard flux_full ncnts_soft ncnts_hard ncnts_full redshift mask slit\n')

stol=1./3600.
specloaddict={'names':('ID','mask','slit','ra','dec','magR','magI','magZ','z','zerr','Q'),'formats':('|S16','|S16','|S8','f8','f8','f8','f8','f8','f8','f16','i8')}

obsdict={'RCS0224-0002': {'obsID': '3181+4987','photcatname': 'rcs0224'},'CL 0848.6+4453': {'obsID': '927+1708','photcatname': 'cl0849'},'RX J0910+5422': {'obsID': '2227+2452','photcatname': 'cl0910'},'RX J105343+5735': {'obsID': '4936','photcatname': 'rxj1053'},'V 1221+4918': {'obsID': '1662','photcatname': 'rxj1221'},'RX J1350.0+6007': {'obsID': '2229','photcatname': 'cl1350'},'RX J1716.9+6708': {'obsID': '548','photcatname': 'rxj1716'}}

namedict = {obsdict[x]['obsID']: x for x in obsdict.keys()}

band_dict={'soft': {'erange': '0.5-2.0','LB':0.5,'UB':2.0},'hard': {'erange': '2.0-8.0','LB':2.0,'UB':8.0},'full': {'erange': '0.5-8.0','LB':0.5,'UB':8.0}}

times=np.array([51730.160737324,125146.86866667,79084.755891771,61469.789688443,105735.52582365,58307.676632384,65311.025181476,14370.453707409,92237.849235535,88973.209339125])
nh = np.array([3.71,2.73,1.44,2.73,1.98,1.76,1.98,2.86,0.58,2.86])
obs = np.array(['548','927','1662','1708','2227','2229','2452','3181','4936','4987'])
obs_dict={obs[x]: {'exp': times[x], 'nh': nh[x]} for x in range(0,10)}

zfull=np.zeros(0)

spec_dict= { \
             'cl1324': {'file': 'FINAL.cl1322.lrisplusdeimos.jul2015.1322Ptmp.nodups.cat', 'loaddict': '','z':[0.756,0.65,0.79]}, \
             'cl1324_north': {'file': 'FINAL.cl1322.lrisplusdeimos.jul2015.1322Ptmp.nodups.cat', 'loaddict': '','z':[0.756,0.65,0.79]}, \
             'cl1324_south': {'file': 'FINAL.cl1322.lrisplusdeimos.jul2015.1322Ptmp.nodups.cat', 'loaddict': '','z':[0.756,0.65,0.79]}, \
             'rxj1821': {'file': 'FINAL.nep5281.deimos.gioia.aug2013.nodups.cat', 'loaddict': '','z':[0.818,0.8,0.83]}, \
             'cl0849': {'file': 'FINAL.onlysemifinal.autocompile.blemaux.0849.feb2013.nodups.cat', 'loaddict': '','z':[1.261,1.25,1.28]}, \
             'X3': {'file': 'FINAL.semifinal.spectroscopic.autocompile.blemaux.XL005.targetsonly.apr2014.cat', 'loaddict': '','z':[1.050,1,1.1]}, \
             'cl0023': {'file': 'FINAL.SG0023.deimos.lris.feb2012.nodups.cat', 'loaddict': '','z':[0.845,0.82,0.87]}, \
             'X5': {'file': 'FINAL.spectra.Cl0023.edit.cat', 'loaddict': '','z':[0.845,0.82,0.87]}, \
             'cl1604': {'file': 'FINAL.spectra.sc1604.wcompletenessmasks.feb2012.nodups.cat', 'loaddict': '','z':[0.900,0.84,0.96]}, \
             'cl1350': {'file': 'FINAL.spectroscopic.autocompile.blemaux.1350.dec2015.nodups.cat', 'loaddict': '','z':[0.804,0.79,0.81]}, \
             'X7': {'file': 'FINAL.spectroscopic.autocompile.blemaux.1429.may2015.nodups.cat', 'loaddict': '','z':[0.985,0.97,1.]}, \
             'X8': {'file': 'FINAL.spectroscopic.autocompile.blemaux.N2560.apr2012.nodups.cat', 'loaddict': '','z':[0,0,0]}, \
             'rcs0224': {'file': 'FINAL.spectroscopic.autocompile.blemaux.RCS0224.apr2012.nodups.cat', 'loaddict': '','z':[0.772,0.76,0.79]}, \
             'rxj1221': {'file': 'FINAL.spectroscopic.autocompile.blemaux.RXJ1221.dec2015.nodups.cat', 'loaddict': '','z':[0.700,0.69,0.71]}, \
             'rxj1716': {'file': 'FINAL.spectroscopic.autocompile.blemaux.RXJ1716.jul2015.nodups.cat', 'loaddict': '','z':[0.813,0.8,0.83]}, \
             'rxj0910': {'file': 'FINAL.spectroscopic.autocompile.blemaux.sc0910.may2015.plusT08.nodups.cat', 'loaddict': '','z':[1.110,1.08,1.15]}, \
             'rxj1757': {'file': 'FINAL.spectroscopic.autocompile.N200.blemaux.aug2013.nodups.cat', 'loaddict': '','z':[0.691,0.68,0.71]}, \
             'X10': {'file': 'spectroscopic.autocompile.blemaux.0943A.targetsonly.cat', 'loaddict': '','z':[0,0,0]}, \
             'cl1137': {'file': 'spectroscopic.autocompile.blemaux.1137.1137Ctmp.may2015.cat', 'loaddict': '','z':[0.959,0.94,0.97]}, \
             'rxj1053': {'file': 'FINAL.spectroscopic.autocompile.blemaux.RXJ1053.dec2015.BCDXtargetsonly.nodups.cat', 'loaddict': '','z':[1.140,1.1,1.15]}}

fullcat=np.loadtxt('/home/rumbaugh/Chandra/full_Xray_catalog.dat',dtype={'names':('obsID','xrayID','RAX','DecX','Xflux_soft','Xflux_hard','Xflux_full','Xnetcnts_soft','Xnetcnts_hard','Xnetcnts_full','Xsig_soft','Xsig_hard','Xsig_full','Xwd_sig_soft','Xwd_sig_hard','Xwd_sig_full','Xdetcode','Xerr','nummatch','raopt1','decopt1','optID1','Popt1','likeopt1','raopt2','decopt2','optID2','Popt2','likeopt2','raopt3','decopt3','optID3','Popt3','likeopt3','probnone','ci','redshift','zerr','magR','magI','magZ','Q'),'formats':('|S16','i8','f8','f8','e8','e8','e8','e8','e8','e8','f8','f8','f8','f8','f8','f8','f8','f8','i8','f8','f8','|S16','f8','f8','f8','f8','|S16','f8','f8','f8','f8','|S16','f8','f8','f8','f8','f8','f8','f8','f8','e8','i8')})

optmatchloaddict={'names':('indX','raX','decX','errX','nummatch','raopt1','decopt1','optID1','Popt1','likeopt1','raopt2','decopt2','optID2','Popt2','likeopt2','raopt3','decopt3','optID3','Popt3','likeopt3','probnone'),'formats':('i8','f8','f8','f8','i8','f8','f8','|S32','f8','f8','f8','f8','|S32','f8','f8','f8','f8','|S32','f8','f8','f8')}

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324_north","cl1324_south","rxj1821","cl1137","rxj1716","rxj1053"])

obj_dict=dict(zip(np.array(["548","1662","2229","4936","927+1708","2227+2452","3181+4987"]),np.zeros(7)))
names=obj_dict.keys()

#FILE=open('/home/rumbaugh/Chandra/full_Xray_catalog.dat','w')

tol=0.2

obsid_dict={'cl0023': '7914', 'cl1324_north': '9403+9840', 'cl1324_south': '9404+9836', 'rxj1757': '10443+11999', 'rxj1821': '10444+10924', 'cl1604': '6932+6933+7343'}

oldfile='/home/rumbaugh/Chandra/Rumbaugh_et_al_2012_Table8_woldflux.dat'

olddict={'names':('field','num','RA','Dec','RAH','RAM','RAS','DecD','DecM','DecS','redshift','soft_lum','hard_lum','full_lum','soft_ncnts','hard_ncnts','full_ncnts','soft_flux','hard_flux','full_flux','significance'),'formats':('|S32','i8','f8','f8','i8','i8','f8','i8','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')}
cro=np.loadtxt(oldfile,dtype=olddict)
indict={'names':('field','number','RA','Dec','lum_soft','lum_hard','lum_full','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit'),'formats':('|S32','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S32','|S32')}
crl=np.loadtxt('/home/rumbaugh/X-ray_lum_cat.1.13.16.dat',dtype=indict)

cro=np.loadtxt(oldfile,dtype=olddict)
ofield=cro['field']
for j in range(0,len(ofield)): ofield[j]=ofield[j].lower()
for field in targets: 
    if ((field in ofield)|(field[:6] in ofield)):
        lra,ldec,lz=cro['RA'][ofield==field],cro['Dec'][ofield==field],cro['redshift'][ofield==field]
    if field[:6]=='cl1324': 
        lra,ldec,lz=cro['RA']['cl1324'==ofield],cro['Dec']['cl1324'==ofield],cro['redshift']['cl1324'==ofield]
    crp=py.open('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/SRCv1/%s_srclist_v1.fits'%(field,field,field))
    pdata=crp[1].data
    crs=np.loadtxt('/home/rumbaugh/git/ORELSE/Catalogs/Spec_z/%s'%spec_dict[field]['file'],dtype=specloaddict)
    matchcat='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_optmatch.%s.dat'%(field,field,field,ldate)
    if field=='cl1604':matchcat='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_optmatch.%s.dat'%(field,field,field,'1.11.16')
    crm=np.loadtxt(matchcat,dtype=optmatchloaddict)
    numX=len(crm['indX'])
    mras,mdecs=crm['raopt1'],crm['decopt1']
    nummatch=crm['nummatch']
    try:
        matchcat2='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_optmatch.%s_min5.dat'%(field,field,field,ldate)
        crm2=np.loadtxt(matchcat2,dtype=optmatchloaddict)
        numX2=len(crm2['indX'])
        mras2,mdecs2=crm2['raopt1'],crm2['decopt1']
        nummatch2=crm2['nummatch']
    except:
        crm2=np.zeros(0)
    zcur,magrcur,magicur,magzcur,zerrcur,qcur=-99.*np.ones(numX),-99.*np.ones(numX),-99.*np.ones(numX),-99.*np.ones(numX),-99.*np.ones(numX),-99*np.ones(numX,dtype='i8')
    maskcur,slitcur=np.zeros(numX,dtype='|S64'),np.zeros(numX,dtype='|S64')
    all_ra,all_decs=crs['ra'][crs['Q']>2.5],crs['dec'][crs['Q']>2.5]
    matched_ncntsS,matched_ncntsH,matched_ncntsF,matched_fluxS,matched_fluxH,matched_fluxF = np.zeros(numX),np.zeros(numX),np.zeros(numX),np.zeros(numX),np.zeros(numX),np.zeros(numX)
    for j in range(0,len(crm['indX'])):
        gz=np.where((crs['ID']==crm['optID1'][j]))[0]
        if len(gz)==0:
            try:
                if field=='rxj1757':
                    gz=np.where(crs['ID']=='F%05i'%(int(crm['optID1'][j])-1))[0]
                else:
                    gz=np.where(crs['ID']=='F%05i'%int(crm['optID1'][j]))[0]
            except:
                pass
        if field[:6]=='cl1324':
            gtmp=np.where((np.abs(mras[j]-crs['ra'])/np.cos(mdecs[j])<stol)&(np.abs(mdecs[j]-crs['dec'])<stol))[0]
            if len(gtmp)!=0: 
                disttmp=SphDist(mras[j],mdecs[j],crs['ra'][gtmp],crs['dec'][gtmp])
                gas=np.argsort(disttmp)
                gz=gtmp[gas[:1]]
        if nummatch[j]<1: gz=np.zeros(0)
        if ((field=='cl1324_south')&(len(gz)==0)):
            gtmp=np.where((np.abs(mras2[j]-crs['ra'])/np.cos(mdecs2[j])<stol)&(np.abs(mdecs2[j]-crs['dec'])<stol))[0]
            if ((len(gtmp)!=0)&(nummatch2[j]>0)): 
                disttmp=SphDist(mras2[j],mdecs2[j],crs['ra'][gtmp],crs['dec'][gtmp])
                gas=np.argsort(disttmp)
                gz=gtmp[gas[:1]]
        if len(gz)>0:
            if len(gz)>1: 
                print 'More than 1 entry for %s matched to %s - %s: '%(crm['optID1'][j],field,crm['indX'][j])
                print crs['z'][gz]
                zcur[j],magrcur[j],magicur[j],magzcur[j],zerrcur[j],qcur[j],maskcur[j],slitcur[j]=crs['z'][gz[0]],crs['magR'][gz[0]],crs['magI'][gz[0]],crs['magZ'][gz[0]],crs['zerr'][gz[0]],crs['Q'][gz[0]],crs['mask'][gz[0]],crs['slit'][gz[0]]
            else:
                zcur[j],magrcur[j],magicur[j],magzcur[j],zerrcur[j],qcur[j],maskcur[j],slitcur[j]=crs['z'][gz[0]],crs['magR'][gz[0]],crs['magI'][gz[0]],crs['magZ'][gz[0]],crs['zerr'][gz[0]],crs['Q'][gz[0]],crs['mask'][gz[0]],crs['slit'][gz[0]]
    all_zs=crs['z'][crs['Q']>2.5]
    g_az=np.arange(len(all_zs))[np.abs(all_zs-0.5*(spec_dict[field]['z'][1]+spec_dict[field]['z'][2]))<0.5*(spec_dict[field]['z'][2]-spec_dict[field]['z'][1])]
    zoom_zs=all_zs[g_az]
    zoom_ras,zoom_decs=all_ra[g_az],all_decs[g_az]
    x_zs=zcur[qcur>2.5]
    g_zs=np.arange(len(x_zs))[np.abs(x_zs-0.5*(spec_dict[field]['z'][1]+spec_dict[field]['z'][2]))<0.5*(spec_dict[field]['z'][2]-spec_dict[field]['z'][1])]
    x_zoom_zs=x_zs[g_zs]
    ra_zs,dec_zs = crm['raX'][qcur>2.5][g_zs],crm['decX'][qcur>2.5][g_zs]
    mask_zs,slit_zs=maskcur[qcur>2.5][g_zs],slitcur[qcur>2.5][g_zs]
    print '\nMatches for %s:'%field
    nncF,nfF,nncS,nfS,nncH,nfH= pdata['Full_net_cts'][qcur>2.5][g_zs],pdata['Full_flux'][qcur>2.5][g_zs],pdata['Soft_net_cts'][qcur>2.5][g_zs],pdata['Soft_flux'][qcur>2.5][g_zs],pdata['Hard_net_cts'][qcur>2.5][g_zs],pdata['Hard_flux'][qcur>2.5][g_zs]
    oncF,ofF,oncS,ofS,oncH,ofH= matched_ncntsF[qcur>2.5][g_zs],matched_fluxF[qcur>2.5][g_zs],matched_ncntsS[qcur>2.5][g_zs],matched_fluxS[qcur>2.5][g_zs],matched_ncntsH[qcur>2.5][g_zs],matched_fluxH[qcur>2.5][g_zs]
    pdncF,pdfF,pdncS,pdfS,pdncH,pdfH= (oncF-nncF)*100./nncF,(ofF-nfF)*100./nfF,(oncS-nncS)*100./nncS,(ofS-nfS)*100./nfS,(oncH-nncH)*100./nncH,(ofH-nfH)*100./nfH
    
    gz=np.zeros(0,dtype='i8')
    newlz=np.zeros(0)
    for k in range(0,len(lz)):
        tempdist=SphDist(lra[k],ldec[k],ra_zs,dec_zs)*60
        gtmp=np.argsort(tempdist)
        if tempdist[gtmp[0]]<5: 
            gz=np.append(gz,k)
            newlz=np.append(newlz,x_zoom_zs[gtmp[0]])

    for k in np.argsort(x_zoom_zs):
        rah,ram,ras=deg2hms(ra_zs[k])
        decd,decm,decs=deg2dms(dec_zs[k])
        zfull=np.append(zfull,x_zoom_zs[k])
    plt.figure(1)
    if field!='cl1324_south':plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    if field!='cl1324_south':plt.hist(zoom_zs,bins=80,range=(spec_dict[field]['z'][1],spec_dict[field]['z'][2]),color='k')
    plt.hist(x_zoom_zs,bins=80,range=(spec_dict[field]['z'][1],spec_dict[field]['z'][2]),color='cyan')
    if ((field in ofield)|(field[:6] in ofield)):
        plt.hist(newlz,bins=80,range=(spec_dict[field]['z'][1],spec_dict[field]['z'][2]),color='red')
    plt.xlabel('Redshift')
    plt.ylabel('Number of sources')
    if field[:6]=='cl1324': 
        plt.title('cl1324')
    else: plt.title(field)
    if field!='cl1324_north':plt.savefig('/home/rumbaugh/Chandra/plots/z_hist_zoom.%s.%s.png'%(field,date))

    plt.figure(2)
    if field!='cl1324_south':plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    if field!='cl1324_south':plt.hist(all_zs,bins=200,range=(0,2),color='k')
    plt.hist(x_zs,bins=200,range=(0,2),color='cyan')
    if ((field in ofield)|(field[:6] in ofield)):
        plt.hist(newlz,bins=200,range=(0,2),color='red')
    plt.xlabel('Redshift')
    plt.ylabel('Number of sources')
    if field[:6]=='cl1324': 
        plt.title('cl1324')
    else: plt.title(field)
    if field!='cl1324_north':plt.savefig('/home/rumbaugh/Chandra/plots/z_hist.%s.%s.png'%(field,date))

    plt.figure(3)
    if field!='cl1324_south':plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    if field!='cl1324_south':plt.scatter(zoom_ras,zoom_decs,s=4,color='k')
    #plt.scatter(crm['raX'],crm['decX'],s=14,color='b')
    plt.scatter(ra_zs,dec_zs,s=40,color='blue')
    if ((field in ofield)|(field[:6] in ofield)):
        plt.scatter(lra[gz],ldec[gz],s=48,color='red')
    xlims=plt.xlim()
    plt.xlim(xlims[1],xlims[0])
    plt.xlabel('RA')
    plt.ylabel('Dec')
    if field[:6]=='cl1324': 
        plt.title('cl1324')
    else: plt.title(field)
    if field!='cl1324_north':plt.savefig('/home/rumbaugh/Chandra/plots/spatial_plot.xray_matches.%s.%s.png'%(field,date))
#FILE.close()
