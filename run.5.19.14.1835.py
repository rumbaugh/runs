import matplotlib.pyplot as plt
execfile('/home/rumbaugh/LoadEVLA_2011.py')

try:
    fluxratio_err
except NameError:
    fluxratio_err = 0.0088
try:
    dayoffset
except NameError:
    dayoffset = 0.0


date = '5.19.14'
ldate = '5.16.14'
color_arr = ['blue','red','green','purple']
ls_arr = ['solid','dashed','dotted','-.']
space_inbetweens = {'B1938': 0.1,'MG0414': 0.08,'B0712':0.1}

source = 'B1938'
space_inbetween = space_inbetweens[source]
fluxratio_err = 0.0048
imgnames = ['fluxC1','fluxC2','fluxB','fluxA']
errnames = np.copy(imgnames)
for n in np.arange(0,len(errnames)): errnames[n] = 'err%s'%errnames[n][4:]
nimg = 3
imgshnames = np.copy(imgnames)
imgshnames = ['C','B','A']
crS = LoadEVLA_2011(source,normalize=True)
crS['day'] -= crS['day'][0]
yticklocs,yticklabs = np.array([0.96,0.98,1.,1.02,1.04])+space_inbetween*(-1.5),np.array(['','0.98','1.00','1.02',''])
yticklocso,yticklabso = np.copy(yticklocs)-space_inbetween*(-1.5),np.copy(yticklabs)
testlegs = []
space_inbetween = space_inbetweens[source]
for tau,mu in zip([50],[0.195444]):
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    for img in range(0,2):
        S = crS[imgnames[img+1]]
        g = np.where(S > 0)[0]
        Serr = crS[errnames[img+1]]
        if (img == 0):
            S2 = crS[imgnames[0]]
            S2err = crS[errnames[0]]
            g2 = np.where(S2 > 0)[0]
            S += S2
            Serr = np.sqrt(Serr**2+S2err**2)
            g = list(set(g) & set(g2))
        if img == 1: 
            S /= mu
            Serr /= mu
        days = crS['day']
        if (img>0): days += tau
        plt.errorbar(days[g],S[g],yerr=Serr[g],color=color_arr[img],fmt='ro',lw=1,capsize=3,mew=1,label=None)
        plt.scatter(days[g],S[g],color=color_arr[img],label=None)
        testlegs = np.append(testlegs,plt.plot(days[g],S[g],color=color_arr[img],lw=2,ls=ls_arr[img]))
    plt.legend(testlegs,imgshnames,loc=2)
    plt.title('Normalized Lightcurve for Lens %s'%(source))
    plt.xlabel('Days',fontsize=14)
    plt.ylabel('Normalized Flux',fontsize=14)
    plt.ylim(0.144,0.1695)
    plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/%s.EVLA.lc_comp_tau_%2i.%s.png'%(source,tau,date))
