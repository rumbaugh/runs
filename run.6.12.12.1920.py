sfiles = np.array(['FINAL.nep5281.deimos.gioia.feb2012.nodups.nh.cat','FINAL.spectra.sc1604.wcompletenessmasks.feb2012.nodups.nh.cat','FINAL.spectroscopic.autocompile.N200.blemaux.feb2012.nh.cat','FINAL.cl1322.lrisplusdeimos.cat'])

zub= np.array([0.84,0.96,0.71,0.79])
zlb = np.array([0.8,0.84,0.68,0.65])

for i in range(0,len(zlb)):
    print '\n\n%s'%(sfiles[i])
    cr = read_file('/home/rumbaugh/%s'%(sfiles[i]))
    sID = copy_colvals(cr,'col1')
    mask = copy_colvals(cr,'col2')
    slit = copy_colvals(cr,'col3')
    RA,DEC = copy_colvals(cr,'col4'),copy_colvals(cr,'col5')
    z = copy_colvals(cr,'col9')
    q = copy_colvals(cr,'col11')
    gq = np.where((q < -0.3) | (q > 2.3))
    gq = gq[0]
    extras = 0
    alreadycounted = np.zeros(len(gq))
    for j in range(0,len(gq)):
        gid = np.where((sID[gq] == sID[gq[j]]) | ((RA[gq] == RA[gq[j]]) & (DEC[gq] == DEC[gq[j]])))
        gid = gid[0]
        if ((len(gid) > 1.1) & (np.sum(alreadycounted[gid]) < len(gid)-0.1)): 
            print gid
            if np.sum(alreadycounted[gid]) > 0.1: print alreadycounted[gid]
            alreadycounted[gid] = 1
            for k in range(0,len(gid)): print '%s %s %s %f %f %f %i'%(sID[gq[gid[k]]],mask[gq[gid[k]]],slit[gq[gid[k]]],RA[gq[gid[k]]],DEC[gq[gid[k]]],z[gq[gid[k]]],q[gq[gid[k]]])
            extras += len(gid)-1
    print 'Number of good spectra: %i(%i)'%(len(gq)-extras,len(gq))
    gz = np.where((z[gq] > zlb[i]) & (z[gq] < zub[i]))
    gz = gz[0]
    extras = 0
    for j in range(0,len(gz)):
        gid = np.where((sID[gq[gz]] == sID[gq[gz[j]]]) | ((RA[gq[gz]] == RA[gq[gz[j]]]) & (DEC[gq[gz]] == DEC[gq[gz[j]]])))
        gid = gid[0]
        if ((len(gid) > 1.1) & (np.sum(alreadycounted[gid]) < len(gid)-0.1)): 
            print gid
            if np.sum(alreadycounted[gid]) > 0.1: print alreadycounted[gid]
            alreadycounted[gid] = 1
            for k in range(0,len(gid)): print '%s %s %s %f %f %f %i'%(sID[gq[gz[gid[k]]]],mask[gq[gz[gid[k]]]],slit[gq[gz[gid[k]]]],RA[gq[gz[gid[k]]]],DEC[gq[gz[gid[k]]]],z[gq[gz[gid[k]]]],q[gq[gz[gid[k]]]])
            extras += len(gid)-1
    print 'Number of members: %i(%i)'%(len(gz)-extras,len(gz))
