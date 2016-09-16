import numpy as np


date = '5.12.14'
ldate = '5.11.14'

quads = np.arange(158)+1
quadsA,quadsB = np.zeros(len(quads),dtype='|S4'),np.zeros(len(quads),dtype='|S4')
for q in range(0,len(quads)):
    quadsA[q],quadsB[q] = str(quads[q])+'A',str(quads[q])+'B'
quads = np.array([y for x in zip(quadsA,quadsB) for y in x])

noquads = ['11A','11B','15A','15B','67A','67B','94A','94B','126A','126B','138A','138B']
rungs=np.array([0,1,2,3,4])

for iteration,cutoff in zip(['Gold','Silver','Bronze'],[6,10,20]):
    FILE = open('/mnt/data2/rumbaugh/TDC/tdc1/results/TDCEvilTeam_tdc1_chi-squared-%s.dt'%(iteration),'w')
    FILE.write('# datafile   dt   dterr\n')
    for rung in rungs:
        cr = np.loadtxt('/mnt/data2/rumbaugh/TDC/tdc1/results/results.tdc1.rung%i.%s.dat'%(rung,ldate),dtype='string')
        dt,dterr = np.array(cr[:,1],dtype='float'),0.5*(np.array(cr[:,3],dtype='float')-np.array(cr[:,2],dtype='float'))
        g = np.where(dterr > cutoff)[0]
        dt[g],dterr[g] = -99,-99
        for i in range(0,720):
            datafile = 'tdc1_rung%i_double_pair%s.txt'%(rung,cr[:,0][i])
            FILE.write('%30s %6.1f %6.1f\n'%(datafile,dt[i],dterr[i]))
        for i in range(721,len(cr[:,0])):
            datafile = 'tdc1_rung%i_quad_pair%s.txt'%(rung,cr[:,0][i])
            FILE.write('%30s %6.1f %6.1f\n'%(datafile,dt[i],dterr[i]))
    FILE.close()
            
