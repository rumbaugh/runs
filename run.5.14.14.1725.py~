import matplotlib.pyplot as plt
execfile('/home/rumbaugh/LoadEVLA_2011.py')

try:
    fluxratio_err
except NameError:
    fluxratio_err = 0.0088
try:
    dayoffset
except NameError:
    dayoffset = 0.2


date = '5.11.14'
color_arr = ['blue','red','green','purple']
ls_arr = ['solid','dashed','dotted','-.']


for source,i_s in zip(['B1938','MG0414','B0712','B0712'],np.arange(4)):
nimg = 4
    if source == 'B1938':
        #imgnames = ['fluxC1','fluxC2','fluxB','fluxA']
        imgnames = ['fluxC','fluxB','fluxA']
        nimg = 3
    if source == 'MG0414':
        imgnames = ['fluxA1','fluxA2','fluxB','fluxC']
    if source == 'B0712':
        imgnames = ['fluxA','fluxB','fluxC','fluxD']
    imgshnames = np.copy(imgnames)
    for k in range(0,4): imgshnames[k] = imgshnames[k][4:]
    if i_s == 3: 
        nimg = 2
        imgshnames = ['A+B','C']
    crS = LoadEVLA_2011(source,normalize=True)
    crS['day'] -= crS['day'][0]
    space_inbetween = 0.08
    yticklocs,yticklabs = np.array([0.96,0.98,1.,1.02,1.04])+space_inbetween*(-1.5),np.array(['','0.98','1.00','1.02',''])
    yticklocso,yticklabso = np.copy(yticklocs)-space_inbetween*(-1.5),np.copy(yticklabs)
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    testlegs = []
    for img in range(0,nimg):
        arb_offset = space_inbetween*(img-1.5)
        if ((i_s != 3) & (i_s != 0)): S = crS[imgnames[img]]
        else: S = crS[imgnames[img+1]]
        g = np.where(S > 0)[0]
        if (((i_s == 3) | (i_s == 0)) & (img == 0)):
            S2 = crS[imgnames[0]]
            g2 = np.where(S2 > 0)[0]
            S += S2
            g = list(set(g) & set(g2))
        rms = np.zeros(len(S))
        Serr = np.sqrt(rms**2+(fluxratio_err*S)**2)
        Smean = np.mean(S[g])
        S /= Smean
        Serr /= Smean
        S += arb_offset
        plt.axhline(y=np.mean(S[g]),lw=2,ls='dashed',color='k')
        days = crS['day']
        plt.errorbar(days[g]+dayoffset*(img-1),S[g],yerr=Serr[g],color=color_arr[img],fmt='ro',lw=1,capsize=3,mew=1,label=None)
        plt.scatter(days[g]+dayoffset*(img-1),S[g],color=color_arr[img],label=None)
        testlegs = np.append(testlegs,plt.plot(days[g]+dayoffset*(img-1),S[g],color=color_arr[img],lw=2,ls=ls_arr[img]))
    plt.legend(testlegs,imgshnames,loc=2)
    plt.title('Normalized Lightcurve for Lens %s'%(source))
    plt.xlabel('Days',fontsize=14)
    plt.ylabel('Normalized Flux',fontsize=14)
    if i_s == 3:
        plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/%s_comb.EVLA.lc_norm_plot_offset.%s.png'%(source,date))
    else:
        plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/%s.EVLA.lc_norm_plot_offset.%s.png'%(source,date))
