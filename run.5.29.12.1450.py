import numpy as np
execfile("/home/rumbaugh/scale_estimators.py")

try:
    ntrials
except NameError:
    ntrials = 10000

names = np.array(['Cl1324+3011','Cl1324+3013','Cl1324+3059','RXJ1757','RXJ1821','Cl1604A','Cl1604B','RXJ0910+5419','RXJ0910+5422'])

for i in range(0,len(names)):
    FILE=open('/home/rumbaugh/temp/idl_clusprops.%s.5.31.12.dat'%(names[i]),'w')
    cr1 = read_file("/home/rumbaugh/temp/idl_clusprops.%s.4.10.12.dat"%(names[i]))
    sig = copy_colvals(cr1,'col1')
    cr = read_file("/home/rumbaugh/temp/idl_vels.%s.4.10.12.dat"%(names[i]))
    vels = copy_colvals(cr,'col1')
    isblu = copy_colvals(cr,'col3')
    gblu = np.where((isblu > 0.5) & (isblu < 1.4))
    gblu = gblu[0]
    gred = np.where(isblu < 0.3)
    gred = gred[0]
    if ((len(gred) > 9.5) & (len(gblu) > 9.8)):
        isblut = np.copy(isblu)
        blu_avg = np.average(vels[gblu])
        red_avg = np.average(vels[gred])
        blu_med = np.median(vels[gblu])
        red_med = np.median(vels[gred])
        blu_bwl = biweight_loc(vels[gblu])
        red_bwl = biweight_loc(vels[gred])
        diffs_avg,diffs_med,diffs_bwl = np.zeros(ntrials),np.zeros(ntrials),np.zeros(ntrials)
        for j in range(0,ntrials):
            np.random.shuffle(isblut)
            gblut = np.where((isblut > 0.5) & (isblut < 1.4))
            gblut = gblut[0]
            gredt = np.where(isblut < 0.3)
            gredt = gredt[0]    
            blut_avg = np.average(vels[gblut])
            redt_avg = np.average(vels[gredt])
            blut_med = np.median(vels[gblut])
            redt_med = np.median(vels[gredt])
            blut_bwl = biweight_loc(vels[gblut])
            redt_bwl = biweight_loc(vels[gredt])     
            diffs_avg[j],diffs_med[j],diffs_bwl[j] = np.fabs(blut_avg-redt_avg),np.fabs(blut_med-redt_med),np.fabs(blut_bwl-redt_bwl)
        sort_avg,sort_med,sort_bwl = np.sort(diffs_avg),np.sort(diffs_med),np.sort(diffs_bwl)
        gsavg,gsmed,gsbwl = np.where(sort_avg > np.fabs(blu_avg-red_avg)),np.where(sort_med > np.fabs(blu_med-red_med)),np.where(sort_bwl > np.fabs(blu_bwl-red_bwl))
        gsavg,gsmed,gsbwl = gsavg[0],gsmed[0],gsbwl[0] 
        perc_avg,perc_med,perc_bwl = len(gsavg)*1.0/ntrials,len(gsmed)*1.0/ntrials,len(gsbwl)*1.0/ntrials
        print '\n%12s - %2i red gals, %2i blue gals\nBlue avg: %4.0f km/s  Red avg: %4.0f km/s\nBlue med: %4.0f km/s  Red med: %4.0f km/s\nBlue BWL: %4.0f km/s  Red BWL: %4.0f km/s\nDiffs - avg: %4.0f km/s  perc higher: %5.1f\nmed: %4.0f km/s  perc higher: %5.1f\nBWL %4.0f km/s  perc higher: %5.1f\n'%(names[i],len(gred),len(gblu),blu_avg,red_avg,blu_med,red_med,blu_bwl,red_bwl,blu_avg-red_avg,100*perc_avg,blu_med-red_med,100*perc_med,blu_bwl-red_bwl,100*perc_bwl)
