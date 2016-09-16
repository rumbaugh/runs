execfile('/home/rumbaugh/X-ray_lum_limit.py')
import time
import matplotlib.pyplot as plt
date='6.20.16'

zrange=np.arange(0.65,1.28,0.05)

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053"])
targets=np.array(["cl1324_north","cl1324_south","rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","rxj1821","cl1137","rxj1716","rxj1053"])
st=time.time()
times=np.zeros(len(targets)+1)
times[0]=st
try:
    truetarget
except NameError:
    truetarget=None
if truetarget!=None: targets=truetarget
for target,it in zip(targets,np.arange(0,len(targets))):
    print target
    Xll=Xray_lum_lim(target)
    plt.figure(1)
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    #plt.scatter(Xll.crxy[:,1:][Xll.crLum[:,0]>0][:,1],Xll.crxy[:,1:][Xll.crLum[:,0]>0][:,0],color='cyan')
    plt.scatter(Xll.crxy[:,1:][Xll.binimgs['full'].T.flatten()>0][:,0],Xll.crxy[:,1:][Xll.binimgs['full'].T.flatten()>0][:,1],color='cyan')
    try:
        x1,y1=Xll.specCH.exterior.xy
    except AttributeError:
        x1,y1=Xll.jointCH.exterior.xy
    x2,y2=Xll.xyCH.exterior.xy
    plt.plot(x1,y1,color='b',label='Spectroscopy')
    plt.plot(x2,y2,color='r',label='Chandra')
    p=Xll.jointCH.representative_point()
    p1,p2=p.bounds[0],p.bounds[1]
    plt.scatter([p1],[p2],marker='x',color='r',s=64)
    plt.legend()
    plt.savefig('/home/rumbaugh/Chandra/plots/X-ray_lum_testing.CH.%s.png'%target)
    
