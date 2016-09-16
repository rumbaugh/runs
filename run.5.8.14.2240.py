execfile('/home/rumbaugh/LoadEVLA_2011.py')
CSOs_dict = LoadEVLA_2011('CSOs')
import matplotlib.pyplot as plt

date = '5.8.14'

CSOs_means = {'Late': dict(zip(CSOs_dict['Late'],np.zeros(len(CSOs_dict['Late'])))), 'Early': dict(zip(CSOs_dict['Early'],np.zeros(len(CSOs_dict['Late']))))}

markers = np.array(["o","<",">","D","s","p","*","h","x"])
colors = np.array(['b','r','c','m','k','b','r','c','m'])
lsarr = np.array(['','','','','','solid','dashed','','dotted'])
sizes = np.array([1.,1.,1.,1.,1.,1.,1.,1.,1.])*25


plt.figure(1)
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.clf()


for EorL in ['Late','Early']:
    if EorL == 'Late':
        for CSO,i in zip(['J1816+3457','J1823+7938','J1945+7055'],[5,6,8]):
            g = np.where(CSOs_dict[EorL][CSO] > 0)[0]
            CSOs_means[EorL][CSO] = np.mean(CSOs_dict[EorL][CSO][g])
            plt.plot(CSOs_dict['time'][EorL][g],CSOs_dict[EorL][CSO][g]/CSOs_means[EorL][CSO],color=colors[i],ls=lsarr[i],lw=2)
    for CSO,i in zip(np.sort(CSOs_dict[EorL].keys()),np.arange(len(CSOs_dict[EorL]))):
        g = np.where(CSOs_dict[EorL][CSO] > 0)[0]
        CSOs_means[EorL][CSO] = np.mean(CSOs_dict[EorL][CSO][g])
        plt.scatter(CSOs_dict['time'][EorL][g],CSOs_dict[EorL][CSO][g]/CSOs_means[EorL][CSO],marker=markers[i],color=colors[i],label=CSO,s=sizes[i])
    plt.xlabel('Days')
    plt.ylabel('Relative Flux')
    plt.legend(loc=2)
    plt.xlim(100,260)
    plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/CSOs_EVLA_2011.%s_block.fluxplot.%s.png'%(EorL,date))
    plt.clf()
