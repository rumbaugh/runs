import numpy as np
import matplotlib.pyplot as plt

date = '5.12.14'
ldate = '5.11.14'

quads = np.arange(158)+1
quadsA,quadsB = np.zeros(len(quads),dtype='|S4'),np.zeros(len(quads),dtype='|S4')
for q in range(0,len(quads)):
    quadsA[q],quadsB[q] = str(quads[q])+'A',str(quads[q])+'B'
quads = np.array([y for x in zip(quadsA,quadsB) for y in x])

noquads = ['11A','11B','15A','15B','67A','67B','94A','94B','126A','126B','138A','138B']
cutoff = np.arange(1,100)*0.5
toterr = np.zeros(0)
rungs=np.array([0,1,2,3,4])
for rung in rungs:
    print 'Rung %i'%rung
    cr = np.loadtxt('/mnt/data2/rumbaugh/TDC/tdc1/results/results.tdc1.rung%i.%s.dat'%(rung,ldate),dtype='string')
    err = -0.5*(np.array(cr[:,2],dtype='float')-np.array(cr[:,3],dtype='float'))
    toterr = np.append(toterr,err)
    fracs = np.zeros(len(cutoff))
    for f in range(len(fracs)):
        fracs[f] = len(err[err < cutoff[f]])*1./len(err)
        if cutoff[f] in [5,6.,7.,7.5,10,12.5,15]: print '\nCutoff: %4.1f\nfrac: %f\n'%(cutoff[f],fracs[f]) 
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.plot(cutoff,fracs)
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.title('Acceptance fraction for rung %i'%(rung))
    plt.xlabel('Cutoff(days)',fontsize=14)
    plt.ylabel('Fraction Accepted',fontsize=14)
    plt.savefig('/mnt/data2/rumbaugh/TDC/tdc1/results/frac_vs_cutoff.rung%i.%s.png'%(rung,date))
fracs = np.zeros(len(cutoff))
for f in range(len(fracs)):
    fracs[f] = len(toterr[toterr < cutoff[f]])*1./len(toterr)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.plot(cutoff,fracs)
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.title('Acceptance fraction for all rungs')
plt.xlabel('Cutoff(days)',fontsize=14)
plt.ylabel('Fraction Accepted',fontsize=14)
plt.savefig('/mnt/data2/rumbaugh/TDC/tdc1/results/frac_vs_cutoff.total.%s.png'%(date))
    
