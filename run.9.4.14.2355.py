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


date = '8.11.14'
ldate = '5.16.14'
color_arr = ['blue','red','green','purple']
ls_arr = ['solid','dashed','dotted','-.']
sizes = [6,6,6,9]
symbols = ["o","s","D","h"]
space_inbetweens = {'B1938': 0.1,'MG0414': 0.08,'B0712':0.1}

ylim_dict = {'MG0414': (0.84,1.23), 'B0712': (0.88,1.15), 'B1938': (0.88,1.15)}

for source in ['B1938','MG0414','B0712']:
    space_inbetween = space_inbetweens[source]
    fluxratio_err = 0.0043
    yticklocs,yticklabs = np.array([0.95,0.975,1.,1.025,1.05,1.075])+space_inbetween*(-0.5),np.array(['0.95','','1.00','','',''])
    yticklocs,yticklabs = np.append(yticklocs,np.array([0.925,0.95,0.975,1.,1.025,1.05,1.075])+space_inbetween*(0.5)),np.append(yticklabs,np.array(['','','','1.00','','1.05','']))
    if source == 'B1938':
        fluxratio_err = 0.0048
        imgnames = ['fluxC1','fluxC2','fluxB','fluxA']
        imgshnames = ['C','B','A']
        nimg=3
    if source == 'MG0414':
        nimg = 4
        imgnames = ['fluxA1','fluxA2','fluxB','fluxC']
        imgshnames = np.copy(imgnames)
        for k in range(0,nimg): imgshnames[k] = imgshnames[k][4:]
        yticklocs,yticklabs = np.array([0.96,0.98,1.,1.02,1.04])+space_inbetween*(-1.5),np.array(['','0.98','1.00','1.02',''])
        yticklocso,yticklabso = np.copy(yticklocs)-space_inbetween*(-1.5),np.copy(yticklabs)
        for i in range(1,4):
            yticklocs,yticklabs = np.append(yticklocs,yticklocso+space_inbetween*(i-1.5)),np.append(yticklabs,yticklabso)
        yticklocs,yticklabs = np.append(yticklocs,np.array([1.06,1.08])+space_inbetween*1.5),np.append(yticklabs,['',''])
    if source == 'B0712':
        imgnames = ['fluxA','fluxB','fluxC','fluxD']
        imgshnames = ['A+B','C','D']
        nimg = 3
    errnames = np.copy(imgnames)
    for n in np.arange(0,len(errnames)): errnames[n] = 'err%s'%errnames[n][4:]
    crS = LoadEVLA_2011(source,normalize=True,normalize_mean=False)
    if source == 'B1938': day0 = crS['day'][0]
    crS['day'] -= day0
    days = crS['day']
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    testlegs = []
    space_inbetween = space_inbetweens[source]
    for img in range(0,nimg):
        arb_offset = space_inbetween*(img-0.5*nimg+0.5)
        if (source == 'MG0414'): 
            S = crS[imgnames[img]]
            Serr = crS[errnames[img]]
        else: 
            S = np.copy(crS[imgnames[img+1]])
            Serr = np.copy(crS[errnames[img+1]])
        g = np.where(S > 0)[0]
        if ((source != 'MG0414') & (img == 0)):
            S2 = crS[imgnames[0]]
            S2err = crS[errnames[0]]
            g2 = np.where(S2 > 0)[0]
            S += S2
            Serr = np.sqrt(Serr**2+S2err**2)
            g = list(set(g) & set(g2))
        print '%6s %4s - %f'%(source,imgshnames[img],np.mean(S[g]))
        Serr /= np.mean(S[g])
        S /= np.mean(S[g])
        S += arb_offset
        plt.axhline(y=np.mean(S[g]),lw=2,ls='dashed',color='k')
        plt.errorbar(days[g],S[g],yerr=Serr[g],color=color_arr[img],fmt='ro',lw=1,capsize=3,mew=1,marker=symbols[img],ms=sizes[img],label=None)
        plt.scatter(days[g],S[g],color=color_arr[img],marker=symbols[img],label=None)
        testlegs = np.append(testlegs,plt.plot(days[g]+dayoffset*(img-1),S[g],color=color_arr[img],lw=2,ls=ls_arr[img]))
    plt.legend(testlegs[::-1],imgshnames[::-1],loc=2)
    plt.title('Normalized Lightcurve for Lens %s'%(source))
    plt.xlabel('Days',fontsize=14)
    plt.ylabel('Normalized Flux',fontsize=14)
    plt.xlim(-20,100)
    plt.ylim(ylim_dict[source])
    plt.yticks(yticklocs,yticklabs)
    #plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/%s.EVLA.lc_norm_plot_offset.%s.png'%(source,date))
    #print '%s - %3.1f(%3.1f)'%(source,(days[-1]-days[0])/len(days),(days[g][-1]-days[g][0])/len(g))
