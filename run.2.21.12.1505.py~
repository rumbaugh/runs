execfile("/home/rumbaugh/FindCloseSources.py")
execfile("/home/rumbaugh/biweight.py")
import matplotlib
import matplotlib.pylab as pylab
import random as rand
c = 3.0*10**5

names2 = np.array(['RXJ1757','RXJ1821','Cl0910+5422'])
names = np.array(['nep200','nep5281','cl0910'])

for i in range(0,len(names)):
    cr = read_file('/home/rumbaugh/%s.info.1Mpc.withvels'%(names[i]))
    RA = copy_colvals(cr,'col2')
    Dec = copy_colvals(cr,'col3')
    z = copy_colvals(cr,'col4')
    vels = copy_colvals(cr,'col5')
    delta = np.zeros(len(z))
    avg_v = c*biweight_loc(z)
    avg_z = avg_v/c
    #sig = np.std(vels)
    sig = biweight_scale(vels)
    Del_MC = np.zeros(1000)
    g_arr = np.zeros((len(z),11),dtype='int8')
    zsig = sig*(1+avg_z)/c
    for j in range(0,len(z)):
        dists = np.zeros(len(z))
        for k in range(0,len(dists)): dists[k] = SphDist(RA[j],Dec[j],RA[k],Dec[k])
        ga = np.argsort(dists)
        g = ga[0:11]
        g_arr[j][0:11] = ga[0:11]
        if len(g) > 11: sys.exit("should be 0:11 instead of 0:12, or else something else went wrong")
        v_avg_loc = biweight_loc(c*z[g])
        sig_loc = biweight_scale(vels[g])
        delta[j] = m.sqrt((11.0/sig/sig)*((v_avg_loc-avg_v)**2+(sig_loc-sig)**2))
    Del = np.sum(delta)
    for k in range(0,1000):
        gr = np.arange(len(z))
        rand.shuffle(gr)
        delta_t = np.zeros(len(z))
        for j in range(0,len(z)):
            g = g_arr[j][0:11]
            v_avg_loc = biweight_loc(c*z[gr[g]])
            sig_loc = biweight_scale(vels[gr[g]])
            delta_t[j] = m.sqrt((11.0/sig/sig)*((v_avg_loc-avg_v)**2+(sig_loc-sig)**2))
        Del_MC[k] = np.sum(delta_t)
    gP = np.where(Del_MC > Del)
    P = len(gP[0])*0.001
    print '%s:\n sig = %f using %i gals\n Del = %f - P = %f\n'%(names[i],sig,len(z),Del,P)
    pylab.xlabel('R.A. (J2000)')
    pylab.ylabel('Dec. (J2000)')
    for j in range(0,len(delta)):
        circsize = 25*m.exp(delta[j])
        if ((z[j] > avg_z-zsig) & (z[j] < avg_z+zsig)): 
            pylab.scatter(RA[j],Dec[j],s=circsize,facecolors='none',color='red')
        elif ((z[j] < avg_z-sig/c) & (z[j] > avg_z+sig/c)): 
            pylab.scatter(RA[j],Dec[j],s=circsize,facecolors='none',color=html_orng,linestyle='dashed')
        else: 
            pylab.scatter(RA[j],Dec[j],s=circsize,facecolors='none',color='blue',linestyle='dotted')
    pylab.savefig('/home/rumbaugh/DSplot.%s.2.19.12.png'%(names2[i]))
    pylab.close('all')

    
