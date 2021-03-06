import matplotlib
from numpy import *
from scipy import *
from pylab import *
import scipy.optimize
import leastsq
import fitmodel
import arrconv
import matplotlib.pylab as pylab

cr2=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clusters.dat',dtype={'names':('field','cluster','ra','dec','z','sig0.5mpc','sig0.5mpcerr','n0.5mpc','sig1mpc','sig1mpcerr','n1mpc','logMvir','LMVerr','nh'),'formats':('|S24','|S24','f8','f8','f8','f8','f8','i8','f8','f8','i8','f8','f8','f8')})
testfield2,testclus2=np.zeros(np.shape(cr2)[0],dtype='|S24'),np.zeros(np.shape(cr2)[0],dtype='|S24')
for i in range(0,len(testclus2)):
    testfield2[i]=cr2['field'][i].lower()
    testclus2[i]=cr2['cluster'][i].lower()

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
kpc = crc[:,12]#*0.7
Hz=crc[:,-3]*crc[:,3]
crc2 = loadtxt("/home/rumbaugh/cc_out_clusters.2.1.16.dat",usecols=(0,0),dtype='|S24')
ccID = crc2[:,0]
testclusc=np.zeros(np.shape(crc)[0],dtype='|S24')
for i in range(0,len(testclusc)):
    testclusc[i]=ccID[i].lower()



def fit_core_rad(cluster,field=None,band='soft'):
    gn=np.where(cluster.lower()==testclusn)[0][0]
    ga=np.where(cluster.lower()==testclusa)[0][0]
    gc=np.where(cluster.lower()==testclusc)[0][0]
    g2=np.where(cluster.lower()==testclus2)[0]
    if len(g2)!=0:
        g2=g2[0]
        sigma=cr2['sig1mpc'][g2]
    else:
        g2=None
        sigma=0
    r0 = 180./(kpc[gc])/.492
    r500 = 2*sigma/(sqrt(500)*Hz[gc])/(kpc[gc]/1000)/.492
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
    ann_step=5
    area_arr=np.copy(cum_area_arr)
    area_arr[1:]=area_arr[1:]-area_arr[:-1]
    SB_arr = cnts_arr/area_arr
    SB_err_arr = np.sqrt(cnts_arr)/area_arr
    cumSB_arr = cum_cnts/cum_area_arr
    cumSB_err_arr = np.sqrt(cum_cnts)/cum_area_arr

    xdummy = linspace(0,500,600)


    bkginit = average(SB_arr[len(SB_arr)-3:len(SB_arr)])
    guesspar=[r0,bkginit]
    def model4par(x,a1,bkg):
        return (NC/(2*pi*a1**2))/(1.0-1.0/sqrt(1+crn['specrad%s'%(band[0].upper())][gn]**2*a1**(-2)))*(1+x**2/(a1**2))**(-1.5)+bkg
        
    clf()
    scatter(ann_arr,SB_arr)
    plot(xdummy,model4par(xdummy,r0,bkginit))
    fit4par = fitmodel.FitModel(ann_arr-0.5*ann_step,SB_arr,5*SB_err_arr,model4par,fitmodel.ChiSqStat,guesspar)
    fit4par.fit()
    fit4par.uncert()
    if not fit4par.have_fit: print 'Failed fit for %s'%cluster

    
    bkgfit,r0fit = fit4par.par_vals['bkg'],fit4par.par_vals['a1']
    bkgerru,r0fiterru = fit4par.par_err['bkg'][1],fit4par.par_err['a1'][1]
    bkgerrl,r0fiterrl = fit4par.par_err['bkg'][0],fit4par.par_err['a1'][0]
    chisq2par = fit4par.statval

    #r500cnts = 2*pi*(NC/(2*pi*r0fit**2))/(1.0-1.0/sqrt(1+crn['specrad%s'%(band[0].upper())][gn]**2*r0fit**(-2)))*r0fit**2*(1-1.0/sqrt(1+r500**2*r0fit**(-2)))
    r500cnts = NC/(1.0-1.0/sqrt(1+crn['specrad%s'%(band[0].upper())][gn]**2*r0fit**(-2)))*(1-1.0/sqrt(1+r500**2*r0fit**(-2)))

    clf()
    rc('axes',linewidth=2)
    rc('font',size=16)
    tick_params(which='major',length=8,width=2,labelsize=16)
    tick_params(which='minor',length=4,width=1.5,labelsize=16)
    xlim(0,118)
    xlabel('Radius (pix)',fontsize=16)
    if i < 4: 
        ylabel('Surface Brightness',fontsize=16)
    else:
        ylabel('(counts per sq. pix)',fontsize=16)
    title(cluster)
    axvline(crn['specrad%s'%(band[0].upper())][gn],linestyle='dashed',color='black')
    errorbar(ann_arr-0.5*ann_step,SB_arr,SB_err_arr,fmt='ro',lw=2,capsize=3,mew=1,ms=8)
    scatter(ann_arr-0.5*ann_step,SB_arr,s=5)
    plot(xdummy,model4par(xdummy,r0fit,bkgfit),"b-",label='2-par Fit, fc2')
    xlim(0,300)
    savefig('/home/rumbaugh/fitted.DE_counts_profile.%s.2.2.16.png'%cluster)
    return r0fit,r0fiterrl,r0fiterru,bkgfit,bkgerrl,bkgerru,r500,r500cnts,NC

FILE=open('/home/rumbaugh/Chandra/ORELSE.soft_cluster_fits.dat','w')
FILE.write('# cluster r0 r0- r0+ bkg bkg- bkg+ r500 r500_NC NC\n')
for cluster in crn['cluster']:
    print cluster
    if cluster == 'Cluster_D':
        FILE.write('Cluster_D 0 0 0 0 0 0 0 0 0\n')
    else:
        r0fit,r0fiterrl,r0fiterru,bkgfit,bkgfiterrl,bkgfiterru,r500,r500cnts,NC=fit_core_rad(cluster)
        FILE.write('%12s %6.1f %6.1f %6.1f %E %E %E %6.1f %7.1f %7.1f\n'%(cluster,r0fit,r0fiterrl,r0fiterru,bkgfit,bkgfiterrl,bkgfiterru,r500,r500cnts,NC))
FILE.close()
