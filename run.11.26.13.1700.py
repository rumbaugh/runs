import numpy as np
import matplotlib.pylab as py
execfile('/home/rumbaugh/Dispersion.py')

ref_dict = {'double_pair':  {'number':  6, 'range': np.array([30,60])},
'double_pair20':  {'number':  1, 'range': np.array([60,90])},
'double_pair30':  {'number':  1, 'range': np.array([60,90])},
'double_pair32':  {'number':  1, 'range': np.array([0,30])},
'double_pair34':  {'number':  1, 'range': np.array([0,30])},
'double_pair38':  {'number':  1, 'range': np.array([0,30])},
'double_pair40':  {'number':  1, 'range': np.array([30,60])},
'double_pair50':  {'number':  1, 'range': np.array([0,30])},
'quad_pairA': {'number':  6, 'range': np.array([0,30])},
'quad_pairB': {'number':  6, 'range': np.array([60,90])}}

prefix = 'tdc1_rung'
FILE = open('/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/Dispersion_output_extended.11.26.13.dat','w')
FILE.write('# pair   tau   mu\n')
for rung in range(0,5):
    for tdcbase in ref_dict:
        try:
            tdcfile = '%s%i_%s%i'%(prefix,rung,tdcbase,ref_dict[tdcbase]['number']+rung)
            if tdcbase[:len(tdcbase)-1] == 'quad_pair': 
                tdcfile = '%s%i_quad_pair%i%s'%(prefix,rung,ref_dict[tdcbase]['number']+rung,tdcbase[-1])
            infile = '/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung%i/output/%s.BA_extended.dat'%(rung,tdcfile)
            outfile = '/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung%i/output/conplot.%s.BA_extended.ps'%(rung,tdcfile)
            cr = np.loadtxt(infile)
            tau,mu,disp = cr[:,0],cr[:,1],cr[:,2]
            len_mu = len(tau[tau==tau[0]])
            len_tau = len(mu[mu==mu[0]])
            Z = np.reshape(disp,(len_tau,len_mu))
            Ztau = np.reshape(tau,(len_tau,len_mu))[:,0]
            Zmu = np.reshape(mu,(len_tau,len_mu))[0]
    #V = np.min(Z)+np.array([2.3,6.18,11.8])
            V = np.arange(10)/10.*(np.max(Z)-np.min(Z))+np.min(Z)
            g = np.where(disp == np.min(disp))[0]
    #print V
            py.clf()
            py.rc('axes',linewidth=2)
            py.fontsize = 14
            py.tick_params(which='major',length=8,width=2,labelsize=14)
            py.tick_params(which='minor',length=4,width=1.5,labelsize=14)
#py.contour(Ztau,Zmu,np.transpose(Z),V,colors='k')
            py.contour(Ztau,Zmu,np.transpose(Z))
            py.scatter(tau[g],mu[g],color='red')
            FILE.write('%28s %5.1f %7.3f\n'%(tdcfile,tau[g],mu[g]))
            py.ylabel('Magnification')
            py.xlabel('Time Delay (days)')
            py.fontsize = 14
            py.savefig(outfile)
            g = np.where(disp == np.min(disp))[0]
            print tdcfile,mu[g],tau[g]
        except:
            pass
FILE.close()
