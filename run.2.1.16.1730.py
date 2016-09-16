import matplotlib
from numpy import *
from scipy import *
from pylab import *
import scipy.optimize
import leastsq
import fitmodel
import arrconv
import matplotlib.pylab as pylab

dictnames=('field','cluster','Xcen','Ycen')
annnames=()
dictfmts=('|S24','|S24','f8','f8')
annfmts=()
rads=np.arange(5,305,5)
for rad in rads:
    annnames=annnames+('%i'%rad,)
    annfmts=annfmts+('f8',)
dictnames=dictnames+annnames
dictfmts=dictfmts+annfmts

cr=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.cluster_ann_counts.dat',dtype={'names':dictnames,'formats':dictfmts})
cr2=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.cluster_ann_counts_noVC.dat',dtype={'names':dictnames,'formats':dictfmts})
testfielda,testclusa=np.zeros(np.shape(cr)[0],dtype='|S24'),np.zeros(np.shape(cr)[0],dtype='|S24')
for i in range(0,len(testclusa)):
    testfielda[i]=cr['field'][i].lower()
    testclusa[i]=cr['cluster'][i].lower()

crn=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.cluster_netcounts.dat',dtype={'names':('field','cluster','ncntsS','cntsS','bkgcntsS','ncnts_noVCS','cnts_noVCS','bkgcnts_noVCS','speccenXS','speccenYS','specradS','ncntsH','cntsH','bkgcntsH','ncnts_noVCH','cnts_noVCH','bkgcnts_noVCH','speccenXH','speccenYH','specradH','ncntsF','cntsF','bkgcntsF','ncnts_noVCF','cnts_noVCF','bkgcnts_noVCF','speccenXF','speccenYF','specradF','bkgcenXF','bkgcenYF','bkgradF'),'formats':('|S24','|S24','f8','f8','f8','f8','f8','f8','i8','i8','i8','f8','f8','f8','f8','f8','f8','i8','i8','i8','f8','f8','f8','f8','f8','f8','i8','i8','i8','i8','i8','i8')})
testfieldn,testclusn=np.zeros(np.shape(crn)[0],dtype='|S24'),np.zeros(np.shape(crn)[0],dtype='|S24')
for i in range(0,len(testclusn)):
    testfieldn[i]=crn['field'][i].lower()
    testclusn[i]=crn['cluster'][i].lower()

crx=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clusters_Xray.dat',dtype={'names':('field','cluster','ra','dec','z','nh'),'formats':('|S24','|S24','f8','f8','f8','f8')})
testfield,testclus=np.zeros(np.shape(crx)[0],dtype='|S24'),np.zeros(np.shape(crx)[0],dtype='|S24')
for i in range(0,len(testclus)):
    testfield[i]=crx['field'][i].lower()
    testclus[i]=crx['cluster'][i].lower()

crc = loadtxt("/home/rumbaugh/cc_out_clusters.2.1.16.dat",usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19))
kpc = crc[:,16]*0.7
crc2 = loadtxt("/home/rumbaugh/cc_out_clusters.2.1.16.dat",usecols=(0,0),dtype='|S24')
ccID = crc2[:,0]

FILEfit = open('/home/rumbaugh/Chandra/SBfits.2.1.16.dat','w')


def fit_core_rad(cluster,field=None,band='full'):
    gn=np.where(cluster.lower()==testclusn)[0][0]
    ga=np.where(cluster.lower()==testclusa)[0][0]
    r0 = 180./(kpc[i])/.492
    print cluster, r0
    NC = crn['ncnts%s'%(band[0].upper())][gn]
    cnts_arr=np.zeros(len(annnames))
    for ica in range(0,len(cnts_arr)):cnts_arr[ica]=cr[annnames[ica]][ga]
    cum_cnts = zeros(len(cnts_arr))
    for j in range(0,len(cnts_arr)): cum_cnts[j] = sum(cnts_arr[0:j])
    cum_area_arr=np.zeros(len(cum_cnts))
    ann_arr = np.zeros(len(cum_cnts))
    for j in range(0,len(cum_cnts)): 
        ann_arr[j]=float(annnames[j])
        cum_area_arr[j]=np.pi*(ann_arr[j]**2)
    area_arr=np.copy(cum_area_arr)
    area_arr[1:]-=area_arr[:-1]
    SB_arr = cnts_arr/area_arr
    SB_err_arr = np.sqrt(cnts_arr)/area_arr
    cumSB_arr = cum_cnts/cum_area_arr
    cumSB_err_arr = np.sqrt(cum_cnts)/cum_area_arr

    bkginit = average(SB_arr[len(SB_arr)-3:len(SB_arr)])
    def model1par(x,a0):
        return a0*(1+x**2/(r0**2))**(-1.5)+bkginit
    def model2par(x,a0,a1):
        return a0*(1+x**2/(a1**2))**(-1.5)+bkginit
    guess1par = 1.25*SB_arr[0]
    guess2par = [1.25*SB_arr[0],r0]
    ann_step=5
    fit1par = fitmodel.FitModel(ann_arr-0.5*ann_step,SB_arr,SB_err_arr,model1par,fitmodel.ChiSqStat,[guess1par])
    fit1par.fit()
    fit1par.uncert()
    if not fit1par.have_fit: print 'Failed 1-parameter fit for %s'%cluster
    fit2par = fitmodel.FitModel(ann_arr-0.5*ann_step,SB_arr,SB_err_arr,model2par,fitmodel.ChiSqStat,guess2par)
    fit2par.fit()
    fit2par.uncert()
    if not fit2par.have_fit: print 'Failed 2-parameter fit for %s'%cluster
    print fit1par.par_vals,fit2par.par_vals
    try:
        Afit1par,Aerr1paru,Aerr1parl,chisq1par = fit1par.par_vals['a0'],fit1par.par_err['a0'][1],fit1par.par_err['a0'][0],fit1par.statval
    except KeyError:
        Afit1par,Aerr1paru,Aerr1parl,chisq1par=0,0,0,0
    try:
        Afit2par,r0fit = fit2par.par_vals['a0'],fit2par.par_vals['a1']
        Aerr2paru,r0fiterru = fit2par.par_err['a0'][1],fit2par.par_err['a1'][1]
        Aerr2parl,r0fiterrl = fit2par.par_err['a0'][0],fit2par.par_err['a1'][0]
        chisq2par = fit2par.statval
    except KeyError:
        Afit2par,r0fit,Aerr2paru,r0fiterru,Aerr2parl,r0fiterrl,chisq2par=0,0,0,0,0,0,0

    def model3par(x,a0,a1):
        return a0*(1+x**2/(a1**2))**(-1.5)+2*a0*a1**2*anninner[i]**(-2)*(-1.0+1.0/sqrt(1+a1**(-2)*anninner[i]**2))+C/(pi*anninner[i]**2)
    def model4par(x,a0,a1):
        return a0*(1+x**2/(a1**2))**(-1.5)+2*a0*a1**2*anninner[i]**(-2)*(1.0-1.0/sqrt(1+a1**(-2)*anninner[i]**2))-NC/(pi*anninner[i]**2)
    fit3par,fit4par = fitmodel.FitModel(ann_arr-0.5*ann_step,SB_arr,SB_err_arr,model3par,fitmodel.ChiSqStat,guess2par),fitmodel.FitModel(ann_arr-0.5*ann_step,SB_arr,SB_err_arr,model4par,fitmodel.ChiSqStat,guess2par)
    fit3par.fit()
    fit3par.uncert()
    fit4par.fit()
    fit4par.uncert()
    if not fit3par.have_fit: print 'Failed second 2-parameter fit for %s'%cluster
    if not fit4par.have_fit: print 'Failed third 2-parameter fit for %s'%cluster
    try:
        Afit3par,r0fit2 = fit3par.par_vals['a0'],fit3par.par_vals['a1']
        Aerr3paru,r0fit2erru = fit3par.par_err['a0'][1],fit3par.par_err['a1'][1]
        Aerr3parl,r0fit2errl = fit3par.par_err['a0'][0],fit3par.par_err['a1'][0]
        chisq3par = fit3par.statval
    except KeyError:
        Afit3par,r0fit2,Aerr3paru,r0fit2erru,err3parl,r0fit2errl,chisq3par = 0,0,0,0,0,0,0
    try:
        Afit4par,r0fit3 = fit4par.par_vals['a0'],fit4par.par_vals['a1']
        Aerr4paru,r0fit3erru = fit4par.par_err['a0'][1],fit4par.par_err['a1'][1]
        Aerr4parl,r0fit3errl = fit4par.par_err['a0'][0],fit4par.par_err['a1'][0]
        chisq4par = fit4par.statval
    except KeyError:
        Afit4par,r0fit3,Aerr4paru,r0fit3erru,Aerr4parl,r0fit3errl,chisq4par=0,0,0,0,0,0,0
    FILEfit.write('%13s %f %f %f %f %f %f %f %f %f %f %f %4.1f %f\n'%(cluster,Afit1par,Aerr1parl,Aerr1paru,Afit2par,Aerr2parl,Aerr2paru,r0fit,r0fiterrl,r0fiterru,chisq1par,chisq2par,ann_step,r0))
    print '%12s:\n1-par: A: %f %f +%f \n2-par, fix. bkg: A: %f %f +%f r0: %f %f +%f\n2-par, fix. cnts: A: %f %f +%f r0: %f %f +%f\n2-par, fc2: A: %f %f +%f r0: %f %f +%f\nchisq 1par: %f 2par, fix. bkg: %f 2par, fix. cnts: %f 2par, fc2: %f\n step: %4.1f r0: %f\n'%(cluster,Afit1par,Aerr1parl,Aerr1paru,Afit2par,Aerr2parl,Aerr2paru,r0fit,r0fiterrl,r0fiterru,Afit3par,Aerr3parl,Aerr3paru,r0fit2,r0fit2errl,r0fit2erru,Afit4par,Aerr4parl,Aerr4paru,r0fit3,r0fit3errl,r0fit3erru,chisq1par,chisq2par,chisq3par,chisq4par,ann_step,r0)

    xdummy = linspace(0,ann_arr.max()+50,200)

    rc('axes',linewidth=2)
    rc('font',size=16)
    #tick_params(which='major',length=8,width=2,labelsize=16)
    #tick_params(which='minor',length=4,width=1.5,labelsize=16)
    #xlim(0,118)
    xlabel('Radius (arcseconds)',fontsize=25)
    if i < 4: 
        ylabel('Surface Brightness',fontsize=25)
    else:
        ylabel('(counts per sq. pixel)',fontsize=25)
    plot(xdummy,model1par(xdummy,Afit1par),"b-",label='1-par Fit')
    plot(xdummy,model2par(xdummy,Afit2par,r0fit),"r-",label='2-par Fit, fix. bkg')
    plot(xdummy,model3par(xdummy,Afit3par,r0fit2),"g-",label='2-par Fit, fix. cnts')
    plot(xdummy,model3par(xdummy,Afit4par,r0fit3),"y-",label='2-par Fit, fc2')
    legend()
    errorbar(ann_arr,SB_arr,SB_err_arr,fmt='ro',lw=2,capsize=3,mew=1,ms=8)
    scatter(ann_arr,SB_arr,s=5)
    savefig('/home/rumbaugh/Chandra/plots/fitted.DE_counts_profile.%s.2.1.16.png'%cluster)
    close()
FILEfit.close()
