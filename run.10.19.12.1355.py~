import matplotlib
from numpy import *
from scipy import *
from pylab import *
import scipy.optimize
import leastsq
import fitmodel
import arrconv
import matplotlib.pylab as pylab

try:
    rewrite
except NameError:
    rewrite = False

anninner = array([120,100,160,100,160,150,100,100,100])*0.5
ai = arrconv.float2int(anninner/2.5-1)
names = array(['RXJ1821','RXJ1757','Cl1324+3059','Cl1324+3011','Cl1324+3013','Cl1604A','Cl1604B','0910+5422','0910+5419'])
crb = loadtxt('/home/rumbaugh/DE_counts.bkg_data.10.13.12.dat',dtype='string')
bgcnts = arrconv.str2float(crb[:,1])
bgSBas = arrconv.str2float(crb[:,3])
bgann1,bgann2 = arrconv.str2float(crb[:,6]),arrconv.str2float(crb[:,7])
bgSBas_err = zeros(len(bgSBas))

crc = loadtxt("/home/rumbaugh/cc_out.6.29.12.nh.dat")
mpc = crc[:,11]*0.7

FILEfit = open('/home/rumbaugh/SBfits.10.16.12.dat','w')

for i in range(0,len(bgSBas)): 
    if ((names[i] != '0910+5419') & (names[i] != 'Cl1324+3013')):
        bgSBas_err[i] = sqrt(bgcnts[i])/(pi*(bgann2[i]**2-bgann1[i]**2))
    else:
        bgSBas_err[i] = sqrt(bgcnts[i])/(pi*(bgann2[i-1]**2-bgann1[i-1]**2))
for i in range(0,len(names)):
    r0 = 0.18*(mpc[i]*60)
    print names[i], r0
    cr = loadtxt('/home/rumbaugh/DE_counts_profile.%s.9.25.12.dat'%names[i])
    cnts_arr = cr[:,2]
    C = cnts_arr[ai[i]]
    NC = C-bgSBas[i]*pi*anninner[i]**2
    cum_cnts = zeros(len(cnts_arr))
    for j in range(0,len(cnts_arr)): cum_cnts[j] = sum(cnts_arr[0:j])
    SB_arr = cr[:,4]
    SB_err_arr = cr[:,6]
    ann_arr = cr[:,1]
    if ((i == 0) | (i == 1) | (i == 2) | (i == 3) | (i == 6) | (i == 7) | (i == 8)):
        ann_step = 10
        ann_arr = arange(12)*10+10
        cnts_arrt = copy(cnts_arr)
        cnts_arr,SB_arr,SB_err_arr = zeros(len(ann_arr)),zeros(len(ann_arr)),zeros(len(ann_arr))
        for j in range(0,len(ann_arr)):
            cnts_arr[j] = cnts_arrt[4*j+3]
    elif ((i == 4)):
        ann_step = 10
        ann_arr = arange(12)*10+10
        cnts_arrt = copy(cnts_arr)
        cnts_arr,SB_arr,SB_err_arr = zeros(len(ann_arr)),zeros(len(ann_arr)),zeros(len(ann_arr))
        for j in range(0,len(ann_arr)):
            cnts_arr[j] = cnts_arrt[4*j+3]
    else:
        ann_step = 15
        ann_arr = arange(8)*15+15
        cnts_arrt = copy(cnts_arr)
        cnts_arr,SB_arr,SB_err_arr = zeros(len(ann_arr)),zeros(len(ann_arr)),zeros(len(ann_arr))
        for j in range(0,len(ann_arr)):
            cnts_arr[j] = cnts_arrt[6*j+5]
    cum_ncnts = zeros(len(cnts_arr))
    cum_ncnts_err = zeros(len(cnts_arr))
    for j in range(0,len(cnts_arr)): 
        cum_ncnts[j] = cnts_arr[j]-bgSBas[i]*pi*ann_arr[j]**2
        cum_ncnts_err[j] = sqrt(cum_cnts[j]+pi*pi*ann_arr[j]**4*bgSBas_err[i]**2)
    area_arr = zeros(len(ann_arr))
    area_arr[0] = pi*ann_arr[0]*ann_arr[0]
    for j in range(1,len(ann_arr)): area_arr[j] = pi*(ann_arr[j]*ann_arr[j]-ann_arr[j-1]*ann_arr[j-1])
    cnts2 = append(zeros(1),cnts_arr[0:len(cnts_arr)-1])
    SB_arr = (cnts_arr-cnts2)/area_arr
    for j in range(0,len(ann_arr)):
        SB_err_arr[j] = (sqrt(cnts_arr[j])+sqrt(cnts2[j]))/area_arr[j]
    if rewrite:
        FILE = open('/home/rumbaugh/DE_counts_profile.%s.10.16.12.dat'%names[i],'w')
        for j in range(0,len(ann_arr)): FILE.write('%3i %4.1f %f %f %f %f %f\n'%(ann_arr[j]*2,ann_arr[j],cnts_arr[j],0.25*SB_arr[j],SB_arr[j],0.25*SB_err_arr[j],SB_err_arr[j]))
        FILE.close()

    bkginit = average(SB_arr[len(SB_arr)-3:len(SB_arr)])
    if names[i] == 'Cl1324+3013': bkginit = SB_arr[7]
    def model1par(x,a0):
        return a0*(1+x**2/(r0**2))**(-1.5)+bkginit
    def model2par(x,a0,a1):
        return a0*(1+x**2/(a1**2))**(-1.5)+bkginit
    guess1par = 1.25*SB_arr[0]
    guess2par = [1.25*SB_arr[0],r0]
    if names[i] == 'Cl1604A': 
        guess2par[0] /= 10.0
        guess2par[1] /= 5.0
    ann_temp,SB_temp,SB_err_temp = copy(ann_arr),copy(SB_arr),copy(SB_err_arr)
    if names[i] == 'Cl1324+3013': ann_temp,SB_temp,SB_err_temp = ann_arr[0:8],SB_arr[0:8],SB_err_arr[0:8]
    fit1par = fitmodel.FitModel(ann_temp-0.5*ann_step,SB_temp,SB_err_temp,model1par,fitmodel.ChiSqStat,[guess1par])
    fit1par.fit()
    fit1par.uncert()
    if not fit1par.have_fit: print 'Failed 1-parameter fit for %s'%names[i]
    fit2par = fitmodel.FitModel(ann_temp-0.5*ann_step,SB_temp,SB_err_temp,model2par,fitmodel.ChiSqStat,guess2par)
    fit2par.fit()
    fit2par.uncert()
    if not fit2par.have_fit: print 'Failed 2-parameter fit for %s'%names[i]
    Afit1par,Afit2par,r0fit = fit1par.par_vals['a0'],fit2par.par_vals['a0'],fit2par.par_vals['a1']
    Aerr1paru,Aerr2paru,r0fiterru = fit1par.par_err['a0'][1],fit2par.par_err['a0'][1],fit2par.par_err['a1'][1]
    Aerr1parl,Aerr2parl,r0fiterrl = fit1par.par_err['a0'][0],fit2par.par_err['a0'][0],fit2par.par_err['a1'][0]
    chisq1par,chisq2par = fit1par.statval,fit2par.statval
    tcnts1,tcnts2 = 2*pi*Afit1par*r0**2,2*pi*Afit2par*r0fit**2

    def model3par(x,a0,a1):
        return a0*(1+x**2/(a1**2))**(-1.5)+2*a0*a1**2*anninner[i]**(-2)*(-1.0+1.0/sqrt(1+a1**(-2)*anninner[i]**2))+C/(pi*anninner[i]**2)
    def model4par(x,a1,bkg):
        return (NC/(2*pi*a1**2))/(1.0-1.0/sqrt(1+anninner[i]**2*a1**(-2)))*(1+x**2/(a1**2))**(-1.5)+bkg
    def model5par(x,a1):
        return (NC/(2*pi*a1**2))/(1.0-1.0/sqrt(1+anninner[i]**2*a1**(-2)))*(1+x**2/(a1**2))**(-1.5)+bkginit
    def model6par(x,a1):
        return (NC/(2*pi*a1**2))/(1.0-1.0/sqrt(1+anninner[i]**2*a1**(-2)))*(1+x**2/(a1**2))**(-1.5)+bgSBas[i]
    guess3 = [r0,bgSBas[i]]
    guess4par = [r0]
    fit3par,fit4par = fitmodel.FitModel(ann_temp-0.5*ann_step,SB_temp,SB_err_temp,model3par,fitmodel.ChiSqStat,guess2par),fitmodel.FitModel(ann_temp-0.5*ann_step,SB_temp,SB_err_temp,model4par,fitmodel.ChiSqStat,guess3)
    fit5par,fit6par = fitmodel.FitModel(ann_temp-0.5*ann_step,SB_temp,SB_err_temp,model5par,fitmodel.ChiSqStat,guess4par),fitmodel.FitModel(ann_temp-0.5*ann_step,SB_temp,SB_err_temp,model6par,fitmodel.ChiSqStat,guess4par)
    fit3par.fit()
    fit3par.uncert()
    fit4par.fit()
    fit4par.uncert()
    fit5par.fit()
    fit5par.uncert()
    fit6par.fit()
    fit6par.uncert()
    if not fit3par.have_fit: print 'Failed second 2-parameter fit for %s'%names[i]
    if not fit4par.have_fit: print 'Failed third 2-parameter fit for %s'%names[i]
    if not fit5par.have_fit: print 'Failed 4th 2-parameter fit for %s'%names[i]
    if not fit6par.have_fit: print 'Failed 5th 2-parameter fit for %s'%names[i]
    Afit3par,r0fit2 = fit3par.par_vals['a0'],fit3par.par_vals['a1']
    if names[i] != 'Cl1324+3013':
        Aerr3paru,r0fit2erru = fit3par.par_err['a0'][1],fit3par.par_err['a1'][1]
        Aerr3parl,r0fit2errl = fit3par.par_err['a0'][0],fit3par.par_err['a1'][0]
    else:
        Aerr3paru,r0fit2erru = fit3par.par_err['a0'],fit3par.par_err['a1']
        Aerr3parl,r0fit2errl = Aerr3paru,r0fit2erru
    chisq3par = fit3par.statval
    chisq4par = fit4par.statval
    bkgfit4par,r0fit3 = fit4par.par_vals['bkg'],fit4par.par_vals['a1']
    bkgerr4paru,r0fit3erru = fit4par.par_err['bkg'][1],fit4par.par_err['a1'][1]
    bkgerr4parl,r0fit3errl = fit4par.par_err['bkg'][0],fit4par.par_err['a1'][0]
    chisq5par,chisq6par = fit5par.statval,fit6par.statval
    r0fit4,r0fit5 = fit5par.par_vals['a1'],fit6par.par_vals['a1']
    r0fit4erru,r0fit5erru = fit5par.par_err['a1'][1],fit6par.par_err['a1'][1]
    r0fit4errl,r0fit5errl = fit5par.par_err['a1'][0],fit6par.par_err['a1'][0]
    tcnts3 = 2*pi*Afit3par*r0fit2**2
    tcnts4 = 2*pi*(NC/(2*pi*r0fit3**2))/(1.0-1.0/sqrt(1+anninner[i]**2*r0fit3**(-2)))*r0fit3**2
    tcnts5 = 2*pi*(NC/(2*pi*r0fit4**2))/(1.0-1.0/sqrt(1+anninner[i]**2*r0fit4**(-2)))*r0fit4**2
    tcnts6 = 2*pi*(NC/(2*pi*r0fit5**2))/(1.0-1.0/sqrt(1+anninner[i]**2*r0fit5**(-2)))*r0fit5**2

    FILEfit.write('%13s %f %f %f %f %f %f %f %f %f %f %f %4.1f %f\n'%(names[i],Afit1par,Aerr1parl,Aerr1paru,Afit2par,Aerr2parl,Aerr2paru,r0fit,r0fiterrl,r0fiterru,chisq1par,chisq2par,ann_step,r0))
    print '%12s:\n1-par: A: %f %f +%f \n2-par, fix. bkg: A: %f %f +%f r0: %f %f +%f\n2-par, fix. cnts: A: %f %f +%f r0: %f %f +%f\n2-par, fc2: bkg: %f %f +%f r0: %f %f +%f\n1-par, fc3: r0: %f %f +%f\n1-par, fc4: r0: %f %f +%f\nchisq 1par: %f 2par, fix. bkg: %f 2par, fix. cnts: %f 2par, fc2: %f 1par, fc3: %f 1par, fc4: %f\ntcnts 1par: %f 2par, fix. bkg: %f 2par, fix. cnts: %f 2par, fc2: %f 1par, fc3: %f 1par, fc4: %f\n step: %4.1f r0: %f bkginit: %f bgSB: %f\n'%(names[i],Afit1par,Aerr1parl,Aerr1paru,Afit2par,Aerr2parl,Aerr2paru,r0fit,r0fiterrl,r0fiterru,Afit3par,Aerr3parl,Aerr3paru,r0fit2,r0fit2errl,r0fit2erru,bkgfit4par,bkgerr4parl,bkgerr4paru,r0fit3,r0fit3errl,r0fit3erru,r0fit4,r0fit4errl,r0fit4erru,r0fit5,r0fit5errl,r0fit5erru,chisq1par,chisq2par,chisq3par,chisq4par,chisq5par,chisq6par,tcnts1,tcnts2,tcnts3,tcnts4,tcnts5,tcnts6,ann_step,r0,bkginit,bgSBas[i])

    xdummy = linspace(0,ann_arr.max()+50,200)

    rc('axes',linewidth=2)
    rc('font',size=16)
    #tick_params(which='major',length=8,width=2,labelsize=16)
    #tick_params(which='minor',length=4,width=1.5,labelsize=16)
    xlim(0,118)
    xlabel('Radius (arcseconds)',fontsize=25)
    if i < 4: 
        ylabel('Surface Brightness',fontsize=25)
    else:
        ylabel('(counts per sq. arcsecond)',fontsize=25)
    #plot(xdummy,model1par(xdummy,Afit1par),"y-",label='1-par Fit')
    #plot(xdummy,model2par(xdummy,Afit2par,r0fit),"r-",label='2-par Fit, fix. bkg')
    #plot(xdummy,model3par(xdummy,Afit3par,r0fit2),"g-",label='2-par Fit, fix. cnts')
    plot(xdummy,model4par(xdummy,r0fit3,bkgfit4par),"r-",label='2-par Fit, fc2')
    plot(xdummy,model5par(xdummy,r0fit4),color="b",label='2-par Fit, bkginit')
    plot(xdummy,model6par(xdummy,r0fit5),color='g',label='2-par Fit, bgSB')
    legend()
    errorbar(ann_arr-0.5*ann_step,SB_arr,SB_err_arr,fmt='ro',lw=2,capsize=3,mew=1,ms=8)
    scatter(ann_arr-0.5*ann_step,SB_arr,s=5)
    xlim(0,118)
    savefig('/home/rumbaugh/fitted.DE_counts_profile.%s.10.17.12.png'%names[i])
    close()
FILEfit.close()
