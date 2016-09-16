execfile("FindCloseSources.py")

#path = '/home/rumbaugh/LFC'
path = '/scratch/rumbaugh/ciaotesting'
pathm = '/scratch/rumbaugh/ciaotesting'
path2 = 'opt_match/opt_Xray_matched_catalog_3high.corrected.twk.dat'
phots = 'xray_phot.soft_hard_full.dat'
names = np.array(['Cl1324','NEP5281','Cl0023','Cl1604','RXJ1757'])
names2 = np.array(['Cl1324','NEP5281','Cl0023','Cl1604','NEP200'])

files = np.array(['FINAL.cl1322.lrisplusdeimos.cat','FINAL.nep5281.deimos.gioia.feb2010.noheader.cat','FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.nov2010.noheader.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.noheader.cat'])

FILEnm = open('/home/rumbaugh/paperstuff/unmatched.log','w')
FILEnm.write("#RA        DEC        Sig(S)  Sig(H)  Sig(F)   Mask\n")

def dec2hms(ang):
    hour = m.floor(ang*24/(360.0))
    rem = ang*24/(360.0) - hour
    minute = m.floor(rem*60.0)
    sec = 60*(rem*60.0-minute)
    return int(hour),int(minute),sec

def dec2dms(ang):
    deg = m.floor(ang)
    rem = ang - deg
    minute = m.floor(rem*60.0)
    sec = 60*(rem*60.0-minute)
    return int(deg),int(minute),sec

def strmask(bmask):
    rstr = ''
    if bmask > 99:
        rstr = 'F'
        bmask -= 100
    if m.floor(bmask/10)*10 != bmask: rstr = 'H' + rstr
    if bmask > 9: rstr = 'S' + rstr
    return rstr

def splitExps(arr):
    exps,coef = np.zeros(len(arr)),np.zeros(len(arr))
    for ise in range(0,len(arr)):
        if arr[ise] != 0:
            exps[ise] = m.floor(m.log(arr[ise],10))
            coef[ise] = arr[ise]/(10**(exps[ise]))
        else:
            exps[ise],coef[ise] = 0,0
    return exps,coef

def setfstr(exp,c):
    f = c*10**(exp+15)
    zeros = -13-int(exp)
    if zeros < 0: zeros = 0
    fstr = '%3.*f'%(zeros,f)
    return fstr

def setzq(ra,dec):
    cic = FindCloseSources(ra,dec,1,sRA,sDec,0)
    if len(cic) > 0:
        sItemp = cic[0]
        zstr = str(sz[sItemp])
        qstr = str(int(sq[sItemp]))
    else:
        zstr = ''
        qstr = ''
    return zstr,qstr

for i in range(0,len(names)):
    master = 'master'
    if i == 2: master = '7914'
    crp = read_file('%s/%s/%s/photometry/%s.%s'%(path,names[i],master,names[i],phots))
    pRAX = get_colvals(crp,'col1')
    pDecX = get_colvals(crp,'col2')
    fluxs = get_colvals(crp,'col3')
    fluxh = get_colvals(crp,'col4')
    fluxf = get_colvals(crp,'col5')
    ncnts = get_colvals(crp,'col6')
    ncnth = get_colvals(crp,'col7')
    ncntf = get_colvals(crp,'col8')
    sigs = get_colvals(crp,'col9')
    sigh = get_colvals(crp,'col10')
    sigf = get_colvals(crp,'col11')
    mask = get_colvals(crp,'col15')
    sfExps,sfC = splitExps(fluxs)
    hfExps,hfC = splitExps(fluxh)
    ffExps,ffC = splitExps(fluxf)
    HR = (ncnth-ncnts)/(ncnts+ncnth)

    mfile = '%s/%s/%s/%s'%(pathm,names[i],master,path2)
    crm = read_file(mfile)
    mRAX = get_colvals(crm,'col2')
    mDecX = get_colvals(crm,'col3')
    merr = get_colvals(crm,'col4')
    nm = get_colvals(crm,'col5')
    mRA = get_colvals(crm,'col6')
    mDec = get_colvals(crm,'col7')
    mRA2 = get_colvals(crm,'col11')
    mDec2 = get_colvals(crm,'col12')
    mRA3 = get_colvals(crm,'col16')
    mDec3 = get_colvals(crm,'col17')
    Prob1 = get_colvals(crm,'col9')
    Prob2 = get_colvals(crm,'col14')
    Prob3 = get_colvals(crm,'col19')
    ProbNS = get_colvals(crm,'col21')

    paths = '/home/rumbaugh/LFC'
    sfile = '%s/%s'%(paths,files[i])
    crs = read_file(sfile)
    sRA = get_colvals(crs,'col4')
    sDec = get_colvals(crs,'col5')
    sI = get_colvals(crs,'col7')
    sq = get_colvals(crs,'col11')
    sz = get_colvals(crs,'col9')

    FILEp = open('/home/rumbaugh/paperstuff/phot.table.%s.txt'%names[i],'w')
    FILEm = open('/home/rumbaugh/paperstuff/match.table.%s.txt'%names[i],'w')
    for j in range(0,len(pRAX)):
        cic = FindCloseSources(pRAX[j],pDecX[j],1,mRAX,mDecX,0)
        if len(cic) > 0: 
            mItemp = cic[0]
            rah,ram,ras = dec2hms(pRAX[j])
            decd,decm,decs = dec2dms(pDecX[j])
            xname = 'J%02i%02i%04.1f%+03i%02i%02i'%(rah,ram,ras,decd,decm,decs)
            if fluxs[j] != 0:
            #    sfstr = '%4.2f $\\times 10^{%i}$'%(sfC[j],sfExps[j])
                sfstr = setfstr(sfExps[j],sfC[j])
            else:
                sfstr = '0.00'
            if fluxh[j] != 0:
            #    hfstr = '%4.2f $\\times 10^{%i}$'%(hfC[j],hfExps[j])
                hfstr = setfstr(hfExps[j],hfC[j])
            else:
                hfstr = '0.00'
            if fluxf[j] != 0:
            #    ffstr = '%4.2f $\\times 10^{%i}$'%(ffC[j],ffExps[j])
                ffstr = setfstr(ffExps[j],ffC[j])
            else:
                ffstr = '0.00'
            FILEp.write('%s &  %02i\ %02i\ %04.1f &  %+03i\ %02i\ %02.0f  & %4.1f & %6.1f  & %6.1f  & %6.1f  & %s & %s & %s & %5.1f & %5.1f & %5.1f & %5.2f & %3s \\\\ \n'%(xname,rah,ram,ras,decd,decm,decs,merr[mItemp],ncnts[j],ncnth[j],ncntf[j],sfstr,hfstr,ffstr,sigs[j],sigh[j],sigf[j],HR[j],strmask(mask[j])))
            if nm[mItemp] > 0.1:
                orah,oram,oras=dec2hms(mRA[mItemp])
                odecd,odecm,odecs=dec2hms(mDec[mItemp])
                zstr,qstr = setzq(mRA[mItemp],mDec[mItemp])
                FILEm.write(' %s & %02i\ %02i\ %04.1f &  %+03i\ %02i\ %02.0f  &  %02i\ %02i\ %04.1f &  %+03i\ %02i\ %02.0f  & %5.3f & %5.3f & %s & %s \\\\ \n'%(xname,rah,ram,ras,decd,decm,decs,orah,oram,oras,odecd,odecm,odecs,Prob1[mItemp],1-ProbNS[mItemp],zstr,qstr))
            if nm[mItemp] > 1.1:
                orah,oram,oras=dec2hms(mRA2[mItemp])
                odecd,odecm,odecs=dec2hms(mDec2[mItemp])
                zstr,qstr = setzq(mRA2[mItemp],mDec2[mItemp])
                FILEm.write(' %s &  &   &  %02i\ %02i\ %04.1f &  %+03i\ %02i\ %02.0f  & %5.3f & %5.3f & %s & %s \\\\ \n'%(xname,orah,oram,oras,odecd,odecm,odecs,Prob2[mItemp],1-ProbNS[mItemp],zstr,qstr))
            if nm[mItemp] > 2.1:
                orah,oram,oras=dec2hms(mRA3[mItemp])
                odecd,odecm,odecs=dec2hms(mDec3[mItemp])
                zstr,qstr = setzq(mRA3[mItemp],mDec3[mItemp])
                FILEm.write(' %s &  &   &  %02i\ %02i\ %04.1f &  %+03i\ %02i\ %02.0f  & %5.3f & %5.3f & %s & %s \\\\ \n'%(xname,orah,oram,oras,odecd,odecm,odecs,Prob3[mItemp],1-ProbNS[mItemp],zstr,qstr))
        else:
            FILEnm.write('%10s %9.7f  %9.7f  %5.2f  %5.2f  %5.2f  %3i\n'%(names2[i], pRAX[j],pDecX[j],sigs[j],sigh[j],sigf[j],int(mask[j]))) 
    FILEp.close()
    FILEm.close()
FILEnm.close()
 
