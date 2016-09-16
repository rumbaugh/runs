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

ymax = array([0.35,0.25,0.1,0.16,0.09,0.06,0.12,0.5,0.35])

anninner = array([120,100,160,100,160,150,100,100,100])*0.5
ai = arrconv.float2int(anninner/2.5-1)
names = array(['RXJ1821','RXJ1757','Cl1324+3059','Cl1324+3011','Cl1324+3013','Cl1604A','Cl1604B','0910+5422','0910+5419'])
crb = loadtxt('/home/rumbaugh/DE_counts.bkg_data.10.13.12.dat',dtype='string')
bgcnts = arrconv.str2float(crb[:,1])
bgSBas = arrconv.str2float(crb[:,3])
bgann1,bgann2 = arrconv.str2float(crb[:,6]),arrconv.str2float(crb[:,7])
bgSBas_err = zeros(len(bgSBas))

sigma = np.array([921,652,880,914,819,619,811,675,1028])
crc = loadtxt("/home/rumbaugh/cc_out.6.29.12.nh.dat")
mpc = crc[:,11]*0.7
Hz = crc[:,4]*0.7

#FILEfit = open('/home/rumbaugh/SBfits.10.19.12.dat','w')

for i in range(0,len(bgSBas)): 
    if ((names[i] != '0910+5419') & (names[i] != 'Cl1324+3013')):
        bgSBas_err[i] = sqrt(bgcnts[i])/(pi*(bgann2[i]**2-bgann1[i]**2))
    else:
        bgSBas_err[i] = sqrt(bgcnts[i])/(pi*(bgann2[i-1]**2-bgann1[i-1]**2))
for i in range(0,len(names)):
    r0 = 0.18*(mpc[i]*60)
    r500 = (mpc[i]*60)*2*sigma[i]/(sqrt(500)*Hz[i])
    print names[i], r0
    cr = loadtxt('/home/rumbaugh/DE_counts_profile.%s.9.25.12.dat'%names[i])
    cnts_arro = cr[:,2]
    C = cnts_arro[ai[i]]
    NC = C-bgSBas[i]*pi*anninner[i]**2
    NCerr = sqrt(C+bgSBas_err[i]**2*pi**2*anninner[i]**2)
    SB_arro = cr[:,4]
    SB_err_arro = cr[:,6]
    ann_arro = cr[:,1]
    def model4par(x,a1,bkg):
        return (NC/(2*pi*a1**2))/(1.0-1.0/sqrt(1+anninner[i]**2*a1**(-2)))*(1+x**2/(a1**2))**(-1.5)+bkg
    bkgfit,r0fit,r0fiterru,r0fiterrl,tcntsarr,r500cntsarr = zeros(3),zeros(3),zeros(3),zeros(3),zeros(3),zeros(3)
    for k in range(0,3):
        ann_step = 5*(k+1)
        ann_arr = (arange(120/ann_step)+1)*ann_step
        cnts_arrt = copy(cnts_arro)
        cnts_arr,SB_arr,SB_err_arr = zeros(len(ann_arr)),zeros(len(ann_arr)),zeros(len(ann_arr))
        for j in range(0,len(ann_arr)): cnts_arr[j] = cnts_arrt[2*(k+1)*j+2*(k+1)-1]
        area_arr = zeros(len(ann_arr))
        area_arr[0] = pi*ann_arr[0]*ann_arr[0]
        for j in range(1,len(ann_arr)): area_arr[j] = pi*(ann_arr[j]*ann_arr[j]-ann_arr[j-1]*ann_arr[j-1])
        cnts2 = append(zeros(1),cnts_arr[0:len(cnts_arr)-1])
        SB_arr = (cnts_arr-cnts2)/area_arr
        for j in range(0,len(ann_arr)): SB_err_arr[j] = (sqrt(cnts_arr[j])+sqrt(cnts2[j]))/area_arr[j]
        if names[i] != 'Cl1324+3013':
            max_temp = [16,8,6]
            ann_temp,SB_temp,SB_err_temp = ann_arr[0:max_temp[k]],SB_arr[0:max_temp[k]],SB_err_arr[0:max_temp[k]]
        fit4par = fitmodel.FitModel(ann_temp-0.5*ann_step,SB_temp,SB_err_temp,model4par,fitmodel.ChiSqStat,[r0,bgSBas[i]])
        fit4par.fit()
        fit4par.uncert()
        if not fit4par.have_fit: print 'Failed third 2-parameter fit for %s'%names[i]
        if isscalar(fit4par.par_err['bkg']):
            bkgerr4paru = fit4par.par_err['bkg']
            bkgerr4parl = bkgerr4paru
        else:
            bkgerr4paru,bkgerr4parl = fit4par.par_err['bkg'][1],fit4par.par_err['bkg'][0]
        if isscalar(fit4par.par_err['a1']):
            r0fit3erru = fit4par.par_err['a1']
            r0fit3errl = r0fit3erru
        else:
            r0fit3erru,r0fit3errl = fit4par.par_err['a1'][1],fit4par.par_err['a1'][0]
        bkgfit4par,r0fit3 = fit4par.par_vals['bkg'],fit4par.par_vals['a1']
        if r0fit3 < 0:
            r0fit3 *= -1
            r0fit3erru,r0fit3errl = -r0fit3errl,-r0fit3erru
        tcnts4 = 2*pi*(NC/(2*pi*r0fit3**2))/(1.0-1.0/sqrt(1+anninner[i]**2*r0fit3**(-2)))*r0fit3**2
        r500cnts = 2*pi*(NC/(2*pi*r0fit3**2))/(1.0-1.0/sqrt(1+anninner[i]**2*r0fit3**(-2)))*r0fit3**2*(1-1.0/sqrt(1+r500**2*r0fit3**(-2)))
        Re = anninner[i]
        r0err = 0.5*(r0fit3erru+r0fit3errl)
        tcntserr = tcnts4*sqrt((NCerr/NC)**2+(Re**2*r0fit3**(-4)*(1+Re**2*r0fit3**(-2))**(-1.5)*(1-1.0/sqrt(1+Re**2*r0fit3**(-2)))**(-2)*r0err)**2)
        r500cntserr = r500cnts*sqrt((tcntserr/tcnts4)**2+(r500**2*r0fit3**(-4)*(1+r500**2*r0fit3**(-2))**(-1.5)*r0err)**2)
        bkgfit[k],r0fit[k],r0fiterru[k],r0fiterrl[k],tcntsarr[k],r500cntsarr[k] = bkgfit4par,r0fit3,r0fit3erru,r0fit3errl,tcnts4,r500cnts
    if names[i] == 'Cl1604A': print 'Cl1604A: %f %f %f\n'%(r0fit[1],r0fiterru[1],r0fiterrl[1])
    #FILEfit.write('%13s %f %f %f %f %f %f %f %4.1f %f %f %f %f %f %f %f %f\n'%(names[i],r0fit3,r0fit3errl,r0fit3erru,bkgfit4par,bkgerr4parl,bkgerr4paru,chisq4par,ann_step,r0,r500,NC,NCerr,r500cnts,r500cntserr,tcnts4,tcntserr))
    #print '%12s:\nannulus width: 5as    10as    15as\nr0 (kpc):    %4.0f    %4.0f    %4.0f\nerror on r0:+%2.0f/%3.0f +%2.0f/%3.0f +%2.0f/%3.0f\nr500 cnts:   %4.0f    %4.0f    %4.0f\ntotal cnts:  %4.0f    %4.0f    %4.0f\n'%(names[i],1000.*r0fit[0]/(mpc[i]*60.),1000.*r0fit[1]/(mpc[i]*60.),1000.*r0fit[2]/(mpc[i]*60.),1000.*r0fiterru[0]/(mpc[i]*60.),1000.*r0fiterrl[0]/(mpc[i]*60.),1000.*r0fiterru[1]/(mpc[i]*60.),1000.*r0fiterrl[1]/(mpc[i]*60.),1000.*r0fiterru[2]/(mpc[i]*60.),1000.*r0fiterrl[2]/(mpc[i]*60.),r500cntsarr[0],r500cntsarr[1],r500cntsarr[2],tcntsarr[0],tcntsarr[1],tcntsarr[2])

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
    plot(xdummy,model4par(xdummy,r0fit3,bkgfit4par),"b-",label='2-par Fit, fc2')
    #plot(xdummy,model5par(xdummy,r0fit4),color="b",label='2-par Fit, bkginit')
    #plot(xdummy,model6par(xdummy,r0fit5),color='g',label='2-par Fit, bgSB')
    #legend()
    errorbar(ann_arr-0.5*ann_step,SB_arr,SB_err_arr,fmt='ro',lw=2,capsize=3,mew=1,ms=8)
    scatter(ann_arr-0.5*ann_step,SB_arr,s=5)
    xlim(0,118)
    ylim(0,ymax[i])
    #savefig('/home/rumbaugh/fitted.DE_counts_profile.%s.10.21.12.png'%names[i])
    close()
#FILEfit.close()
